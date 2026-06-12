import os
import shutil
import time

BACKUP_DIR = "special://profile/addon_data/plugin.program.adelforgewizard/backups/"


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
