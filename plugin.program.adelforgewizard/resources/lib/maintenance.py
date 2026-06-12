import os
import shutil
import time

BACKUP_DIR = "special://profile/addon_data/plugin.program.adelforgewizard/backups/"

DNS_PROBES = [("1.1.1.1", 53), ("8.8.8.8", 53)]


def _translate(special_path):
    import xbmcvfs

    return xbmcvfs.translatePath(special_path)


def backup_dir_path():
    return _translate(BACKUP_DIR)


def clear_general_cache():
    import xbmcvfs

    path = _translate("special://temp/")
    if xbmcvfs.exists(path):
        xbmcvfs.rmdir(path, force=True)


def clear_thumbnail_cache():
    import xbmcvfs

    path = _translate("special://thumbnails/")
    if xbmcvfs.exists(path):
        xbmcvfs.rmdir(path, force=True)

    database_dir = _translate("special://database/")
    if xbmcvfs.exists(database_dir):
        _, files = xbmcvfs.listdir(database_dir)
        for name in files:
            if name.lower().startswith("texture"):
                xbmcvfs.delete(os.path.join(database_dir, name))


def clear_addon_packages():
    import xbmcvfs

    path = _translate("special://home/addons/packages/")
    if xbmcvfs.exists(path):
        xbmcvfs.rmdir(path, force=True)


def reset_cache_tuning():
    import xbmcvfs

    path = _translate("special://userdata/advancedsettings.xml")
    if xbmcvfs.exists(path):
        xbmcvfs.delete(path)


def backup_userdata():
    import xbmcvfs

    userdata_dir = _translate("special://userdata/")
    backup_dir = backup_dir_path()
    if not xbmcvfs.exists(backup_dir):
        xbmcvfs.mkdirs(backup_dir)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    archive_base = os.path.join(backup_dir, "adelforge-backup-" + timestamp)
    archive_path = shutil.make_archive(archive_base, "zip", userdata_dir)
    return archive_path


def list_backups():
    import xbmcvfs

    backup_dir = backup_dir_path()
    if not xbmcvfs.exists(backup_dir):
        return []

    _, files = xbmcvfs.listdir(backup_dir)
    return sorted((name for name in files if name.lower().endswith(".zip")), reverse=True)


def repair_addon_database():
    import xbmcvfs

    database_dir = _translate("special://database/")
    if not xbmcvfs.exists(database_dir):
        return

    _, files = xbmcvfs.listdir(database_dir)
    for name in files:
        if name.lower().startswith("addons"):
            xbmcvfs.delete(os.path.join(database_dir, name))


def reset_skin_settings():
    import xbmc
    import xbmcvfs

    skin_id = xbmc.getSkinDir()
    path = _translate("special://profile/addon_data/" + skin_id + "/")
    if xbmcvfs.exists(path):
        xbmcvfs.rmdir(path, force=True)


def _format_size(num_bytes):
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return "{:.1f} {}".format(size, unit)
        size /= 1024
    return "{:.1f} TB".format(size)


def _dir_size(path):
    import xbmcvfs

    total = 0
    if not xbmcvfs.exists(path):
        return total

    dirs, files = xbmcvfs.listdir(path)
    for name in files:
        stat = xbmcvfs.Stat(os.path.join(path, name))
        total += stat.st_size()
    for name in dirs:
        total += _dir_size(os.path.join(path, name) + "/")
    return total


def storage_report():
    lines = []

    try:
        usage = shutil.disk_usage(_translate("special://userdata/"))
        lines.append("Storage free: {} of {}".format(
            _format_size(usage.free), _format_size(usage.total)
        ))
    except OSError:
        lines.append("Storage free: unavailable")

    cache_size = _dir_size(_translate("special://temp/"))
    lines.append("General cache size: " + _format_size(cache_size))

    thumbnails_size = _dir_size(_translate("special://thumbnails/"))
    lines.append("Thumbnail cache size: " + _format_size(thumbnails_size))

    packages_size = _dir_size(_translate("special://home/addons/packages/"))
    lines.append("Add-on packages size: " + _format_size(packages_size))

    return "\n".join(lines)


def network_diagnostics():
    import socket

    lines = []
    for host, port in DNS_PROBES:
        try:
            socket.create_connection((host, port), timeout=3).close()
            lines.append("{}: reachable".format(host))
        except OSError:
            lines.append("{}: unreachable".format(host))
    return "\n".join(lines)
