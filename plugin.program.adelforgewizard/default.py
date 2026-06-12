#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from urllib.parse import parse_qsl, urlencode

import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib import maintenance, profiles

ADDON = xbmcaddon.Addon()
HANDLE = int(sys.argv[1])
BASE_URL = sys.argv[0]

_ = ADDON.getLocalizedString

SENTINEL_SOURCE_URL = "https://akahwaj.github.io/adel-forge-kodi-repo/"
SENTINEL_REPO_ZIP = "repo.zip"
SENTINEL_WIZARD_ZIP = "wizard.zip"


def build_url(**params):
    return BASE_URL + "?" + urlencode(params)


def get_params():
    paramstring = sys.argv[2][1:]
    return dict(parse_qsl(paramstring))


def add_item(label, params, is_folder=True, icon="DefaultFolder.png"):
    list_item = xbmcgui.ListItem(label=label)
    list_item.setArt({"icon": icon, "thumb": icon})
    xbmcplugin.addDirectoryItem(HANDLE, build_url(**params), list_item, is_folder)


def list_main_menu():
    add_item(_(30000), {"mode": "profiles"})
    add_item(_(30001), {"mode": "maintenance"})
    add_item(_(30003), {"mode": "backup"})
    add_item("Premium Services Manager", {"mode": "premium_services"}, is_folder=False, icon="DefaultAddonInfo.png")
    add_item("Sentinel Install Guide", {"mode": "install_guide"}, is_folder=False, icon="DefaultAddonInfo.png")
    add_item(_(30005), {"mode": "legal_addons"}, is_folder=False, icon="DefaultAddonInfo.png")
    add_item(_(30004), {"mode": "about"}, is_folder=False, icon="DefaultAddonInfo.png")
    xbmcplugin.setContent(HANDLE, "files")
    xbmcplugin.endOfDirectory(HANDLE)


def list_profiles():
    for key in profiles.PROFILE_ORDER:
        profile = profiles.PROFILES[key]
        add_item(profile["name"], {"mode": "profile", "profile": key})
    xbmcplugin.endOfDirectory(HANDLE)


def list_profile(profile_key):
    if profile_key not in profiles.PROFILES:
        xbmcplugin.endOfDirectory(HANDLE, succeeded=False)
        return

    add_item(
        _(30010),
        {"mode": "apply_profile", "profile": profile_key},
        is_folder=False,
        icon="DefaultAddonProgram.png",
    )
    add_item(
        _(30011),
        {"mode": "profile_addons", "profile": profile_key},
        is_folder=False,
        icon="DefaultAddonInfo.png",
    )
    xbmcplugin.endOfDirectory(HANDLE)


def apply_profile(profile_key):
    profile = profiles.PROFILES.get(profile_key)
    if not profile:
        xbmcplugin.endOfDirectory(HANDLE, succeeded=False)
        return

    success = profiles.apply_profile(profile_key)
    if success:
        ADDON.setSetting("last_profile", profile["name"])
        xbmcgui.Dialog().notification(
            ADDON.getAddonInfo("name"),
            _(30014) % profile["name"],
            xbmcgui.NOTIFICATION_INFO,
        )
    else:
        xbmcgui.Dialog().notification(
            ADDON.getAddonInfo("name"),
            _(30015) % profile["name"],
            xbmcgui.NOTIFICATION_ERROR,
        )
    xbmcplugin.endOfDirectory(HANDLE, succeeded=success)


def show_profile_addons(profile_key):
    profile = profiles.PROFILES.get(profile_key)
    if not profile:
        xbmcplugin.endOfDirectory(HANDLE, succeeded=False)
        return

    addon_list = "\n".join("- " + name for name in profile["addons"]) or _(30053)
    text = "{}\n\n{}\n\n{}\n{}".format(
        profile["description"],
        _(30013) % profile["skin"],
        _(30012) % profile["name"],
        addon_list,
    )
    xbmcgui.Dialog().textviewer(profile["name"], text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def list_maintenance():
    add_item(_(30020), {"mode": "clear_cache"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item(_(30021), {"mode": "clear_thumbnails"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item(_(30022), {"mode": "clear_packages"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item(_(30023), {"mode": "reset_cache"}, is_folder=False, icon="DefaultAddonProgram.png")
    xbmcplugin.endOfDirectory(HANDLE)


def run_maintenance_action(confirm_string_id, done_string_id, func):
    if xbmcgui.Dialog().yesno(ADDON.getAddonInfo("name"), _(confirm_string_id)):
        func()
        xbmcgui.Dialog().notification(
            ADDON.getAddonInfo("name"), _(done_string_id), xbmcgui.NOTIFICATION_INFO
        )
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def list_backup_menu():
    add_item(_(30024), {"mode": "do_backup"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item(_(30025), {"mode": "view_backups"}, is_folder=False, icon="DefaultAddonInfo.png")
    add_item(_(30026), {"mode": "restore_backup"}, is_folder=False, icon="DefaultAddonInfo.png")
    xbmcplugin.endOfDirectory(HANDLE)


def do_backup():
    archive_path = maintenance.backup_userdata()
    xbmcgui.Dialog().notification(
        ADDON.getAddonInfo("name"), _(30044), xbmcgui.NOTIFICATION_INFO
    )
    xbmcgui.Dialog().textviewer(_(30044), archive_path)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def view_backups():
    backups = maintenance.list_backups()
    if backups:
        text = "\n".join(backups)
    else:
        text = _(30045)
    xbmcgui.Dialog().textviewer(_(30046), text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def restore_backup():
    backups = maintenance.list_backups()
    listing = "\n".join(backups) if backups else _(30045)
    text = "{}\n\n{}\n\n{}".format(listing, _(30047), maintenance.backup_dir_path())
    xbmcgui.Dialog().textviewer(_(30026), text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_premium_services():
    text = """Sentinel Premium Services Manager\n\nRecommended account services for Sentinel Custom Kodi Build:\n\n- Real-Debrid\n- TorBox\n- Premiumize\n- AllDebrid\n- Trakt\n\nBest add-ons for these services:\n\n- FEN Light\n- Umbrella\n- POV\n- Seren\n- FenSkeleton\n\nSetup notes:\n\n1. Install and open your preferred video add-on.\n2. Open the add-on settings.\n3. Go to Accounts / My Services.\n4. Authorize Real-Debrid, TorBox, Premiumize, AllDebrid, and/or Trakt where supported.\n5. Restart Kodi after account authorization.\n6. Rebuild widgets if menus do not update.\n\nSentinel does not store your account credentials. Authorization is handled by each supported add-on or service manager."""
    xbmcgui.Dialog().textviewer("Premium Services Manager", text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_install_guide():
    text = """Sentinel Custom Kodi Build Install Guide\n\nKodi Source URL:\n{source}\n\nRepository ZIP:\n{repo_zip}\n\nWizard ZIP:\n{wizard_zip}\n\nInstall from Kodi File Manager:\n\n1. Open Kodi.\n2. Go to Settings.\n3. Go to File Manager.\n4. Select Add Source.\n5. Enter the source URL above.\n6. Name it Sentinel.\n7. Go back to the Kodi home screen.\n8. Go to Add-ons.\n9. Select Install from zip file.\n10. Choose Sentinel.\n11. Install repo.zip.\n12. Go to Install from repository.\n13. Open the Sentinel / Adel Forge repository.\n14. Go to Program add-ons.\n15. Install the Sentinel Wizard.\n16. Open Sentinel Wizard from Program add-ons.\n17. Select Lite, Premium, Max, Sports, or Safe Mode.\n18. Configure Real-Debrid, TorBox, Premiumize, AllDebrid, and Trakt inside the supported add-ons.\n\nRecommended first profile:\nSentinel Premium\n\nFire TV recommendation:\nUse Sentinel Lite or Sentinel Premium for best performance.\n\nIf Kodi becomes slow:\nUse Sentinel Safe Mode, clear cache, clear thumbnails, and reduce widgets.""".format(
        source=SENTINEL_SOURCE_URL,
        repo_zip=SENTINEL_REPO_ZIP,
        wizard_zip=SENTINEL_WIZARD_ZIP,
    )
    xbmcgui.Dialog().textviewer("Sentinel Install Guide", text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_legal_addons():
    xbmcgui.Dialog().textviewer(_(30005), _(30070))
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_about():
    last_profile = ADDON.getSetting("last_profile")
    status = (_(30052) % last_profile) if last_profile else _(30053)
    text = "{}\n\n{}\n\n{}".format(ADDON.getAddonInfo("name"), _(30051), status)
    xbmcgui.Dialog().textviewer(_(30050), text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def router():
    params = get_params()
    mode = params.get("mode")

    if mode is None:
        list_main_menu()
    elif mode == "profiles":
        list_profiles()
    elif mode == "profile":
        list_profile(params["profile"])
    elif mode == "apply_profile":
        apply_profile(params["profile"])
    elif mode == "profile_addons":
        show_profile_addons(params["profile"])
    elif mode == "maintenance":
        list_maintenance()
    elif mode == "clear_cache":
        run_maintenance_action(30030, 30040, maintenance.clear_general_cache)
    elif mode == "clear_thumbnails":
        run_maintenance_action(30031, 30041, maintenance.clear_thumbnail_cache)
    elif mode == "clear_packages":
        run_maintenance_action(30032, 30042, maintenance.clear_addon_packages)
    elif mode == "reset_cache":
        run_maintenance_action(30033, 30043, maintenance.reset_cache_tuning)
    elif mode == "backup":
        list_backup_menu()
    elif mode == "do_backup":
        do_backup()
    elif mode == "view_backups":
        view_backups()
    elif mode == "restore_backup":
        restore_backup()
    elif mode == "premium_services":
        show_premium_services()
    elif mode == "install_guide":
        show_install_guide()
    elif mode == "legal_addons":
        show_legal_addons()
    elif mode == "about":
        show_about()
    else:
        xbmcplugin.endOfDirectory(HANDLE, succeeded=False)


if __name__ == "__main__":
    router()
