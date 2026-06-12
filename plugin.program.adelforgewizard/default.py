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
    add_item("Sentinel Update Center", {"mode": "update_center"})
    add_item("Sentinel Repair Center", {"mode": "repair_center"})
    add_item(_(30001), {"mode": "maintenance"})
    add_item(_(30003), {"mode": "backup"})
    add_item("Premium Services Manager", {"mode": "premium_services"}, is_folder=False, icon="DefaultAddonInfo.png")
    add_item("18 Add-on Manifest", {"mode": "addon_manifest"}, is_folder=False, icon="DefaultAddonInfo.png")
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

    add_item(_(30010), {"mode": "apply_profile", "profile": profile_key}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item(_(30011), {"mode": "profile_addons", "profile": profile_key}, is_folder=False, icon="DefaultAddonInfo.png")
    xbmcplugin.endOfDirectory(HANDLE)


def apply_profile(profile_key):
    profile = profiles.PROFILES.get(profile_key)
    if not profile:
        xbmcplugin.endOfDirectory(HANDLE, succeeded=False)
        return

    success = profiles.apply_profile(profile_key)
    if success:
        ADDON.setSetting("last_profile", profile["name"])
        xbmcgui.Dialog().notification(ADDON.getAddonInfo("name"), _(30014) % profile["name"], xbmcgui.NOTIFICATION_INFO)
    else:
        xbmcgui.Dialog().notification(ADDON.getAddonInfo("name"), _(30015) % profile["name"], xbmcgui.NOTIFICATION_ERROR)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=success)


def show_profile_addons(profile_key):
    profile = profiles.PROFILES.get(profile_key)
    if not profile:
        xbmcplugin.endOfDirectory(HANDLE, succeeded=False)
        return

    addon_list = profiles.format_addon_manifest(profile["addons"]) if profile["addons"] else _(30053)
    text = "{}\n\n{}\n\n{}\n{}".format(profile["description"], _(30013) % profile["skin"], _(30012) % profile["name"], addon_list)
    xbmcgui.Dialog().textviewer(profile["name"], text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def list_update_center():
    add_item("Refresh Repositories", {"mode": "refresh_repos"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item("Force Check for Add-on Updates", {"mode": "force_updates"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item("Open Available Updates", {"mode": "open_available_updates"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item("Open My Add-ons", {"mode": "open_my_addons"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item("Update Rules / Auto-Update Guide", {"mode": "update_guide"}, is_folder=False, icon="DefaultAddonInfo.png")
    xbmcplugin.endOfDirectory(HANDLE)


def list_repair_center():
    add_item("Backup Before Repair", {"mode": "do_backup"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item("Clear Failed Install Packages", {"mode": "clear_packages"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item("Clear Cache", {"mode": "clear_cache"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item("Clear Thumbnails", {"mode": "clear_thumbnails"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item("Reset AdvancedSettings.xml", {"mode": "reset_cache"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item("Broken Source Fix Guide", {"mode": "broken_source_guide"}, is_folder=False, icon="DefaultAddonInfo.png")
    add_item("Broken Repository Fix Guide", {"mode": "broken_repo_guide"}, is_folder=False, icon="DefaultAddonInfo.png")
    add_item("Safe Mode Recovery Guide", {"mode": "safe_mode_guide"}, is_folder=False, icon="DefaultAddonInfo.png")
    xbmcplugin.endOfDirectory(HANDLE)


def list_maintenance():
    add_item(_(30020), {"mode": "clear_cache"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item(_(30021), {"mode": "clear_thumbnails"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item(_(30022), {"mode": "clear_packages"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item(_(30023), {"mode": "reset_cache"}, is_folder=False, icon="DefaultAddonProgram.png")
    xbmcplugin.endOfDirectory(HANDLE)


def run_maintenance_action(confirm_string_id, done_string_id, func):
    if xbmcgui.Dialog().yesno(ADDON.getAddonInfo("name"), _(confirm_string_id)):
        func()
        xbmcgui.Dialog().notification(ADDON.getAddonInfo("name"), _(done_string_id), xbmcgui.NOTIFICATION_INFO)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def list_backup_menu():
    add_item(_(30024), {"mode": "do_backup"}, is_folder=False, icon="DefaultAddonProgram.png")
    add_item(_(30025), {"mode": "view_backups"}, is_folder=False, icon="DefaultAddonInfo.png")
    add_item(_(30026), {"mode": "restore_backup"}, is_folder=False, icon="DefaultAddonInfo.png")
    xbmcplugin.endOfDirectory(HANDLE)


def do_backup():
    archive_path = maintenance.backup_userdata()
    xbmcgui.Dialog().notification(ADDON.getAddonInfo("name"), _(30044), xbmcgui.NOTIFICATION_INFO)
    xbmcgui.Dialog().textviewer(_(30044), archive_path)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def view_backups():
    backups = maintenance.list_backups()
    text = "\n".join(backups) if backups else _(30045)
    xbmcgui.Dialog().textviewer(_(30046), text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def restore_backup():
    backups = maintenance.list_backups()
    listing = "\n".join(backups) if backups else _(30045)
    text = "{}\n\n{}\n\n{}".format(listing, _(30047), maintenance.backup_dir_path())
    xbmcgui.Dialog().textviewer(_(30026), text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def refresh_repos():
    import xbmc
    xbmc.executebuiltin("UpdateAddonRepos")
    xbmcgui.Dialog().notification("Sentinel Update Center", "Repository refresh started", xbmcgui.NOTIFICATION_INFO)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def force_updates():
    import xbmc
    xbmc.executebuiltin("UpdateLocalAddons")
    xbmc.executebuiltin("UpdateAddonRepos")
    xbmcgui.Dialog().notification("Sentinel Update Center", "Add-on update check started", xbmcgui.NOTIFICATION_INFO)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def open_available_updates():
    import xbmc
    xbmc.executebuiltin("ActivateWindow(AddonBrowser,addons://updates/,return)")
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def open_my_addons():
    import xbmc
    xbmc.executebuiltin("ActivateWindow(AddonBrowser,addons://user/,return)")
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_addon_manifest():
    lines = ["Sentinel 18 Add-on Manifest", "", "Use only content, add-ons, and services you are authorized to access.", ""]
    lines.append(profiles.format_addon_manifest(list(profiles.ADDON_SOURCES.keys())))
    xbmcgui.Dialog().textviewer("18 Add-on Manifest", "\n".join(lines))
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_premium_services():
    text = """Sentinel Premium Services Manager\n\nRecommended account services for Sentinel Custom Kodi Build:\n\n- Real-Debrid\n- TorBox\n- Premiumize\n- AllDebrid\n- Trakt\n\nBest add-ons for these services:\n\n- FEN Light\n- Umbrella\n- POV\n- Seren\n- FenSkeleton\n\nSetup notes:\n\n1. Install and open your preferred video add-on.\n2. Open the add-on settings.\n3. Go to Accounts / My Services.\n4. Authorize Real-Debrid, TorBox, Premiumize, AllDebrid, and/or Trakt where supported.\n5. Restart Kodi after account authorization.\n6. Rebuild widgets if menus do not update.\n\nSentinel does not store your account credentials. Authorization is handled by each supported add-on or service manager."""
    xbmcgui.Dialog().textviewer("Premium Services Manager", text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_install_guide():
    text = """Sentinel Custom Kodi Build Install Guide\n\nKodi Source URL:\n{source}\n\nRepository ZIP:\n{repo_zip}\n\nWizard ZIP:\n{wizard_zip}\n\nInstall from Kodi File Manager:\n\n1. Open Kodi.\n2. Go to Settings.\n3. Go to File Manager.\n4. Select Add Source.\n5. Enter the source URL above.\n6. Name it Sentinel.\n7. Go back to the Kodi home screen.\n8. Go to Add-ons.\n9. Select Install from zip file.\n10. Choose Sentinel.\n11. Install repo.zip.\n12. Go to Install from repository.\n13. Open the Sentinel / Adel Forge repository.\n14. Go to Program add-ons.\n15. Install the Sentinel Wizard.\n16. Open Sentinel Wizard from Program add-ons.\n17. Select Lite, Premium, Max, Sports, or Safe Mode.\n18. Configure Real-Debrid, TorBox, Premiumize, AllDebrid, and Trakt inside the supported add-ons.\n\nRecommended first profile for your 50-inch Insignia Fire TV:\nSentinel Lite\n\nIf Kodi becomes slow:\nUse Sentinel Safe Mode, clear cache, clear thumbnails, clear packages, and reduce widgets.""".format(source=SENTINEL_SOURCE_URL, repo_zip=SENTINEL_REPO_ZIP, wizard_zip=SENTINEL_WIZARD_ZIP)
    xbmcgui.Dialog().textviewer("Sentinel Install Guide", text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_update_guide():
    text = """Sentinel Update Center Guide\n\nFor automatic updates:\n\nKodi Settings > System > Add-ons\n- Updates: Install updates automatically\n- Show notifications: On\n- Unknown sources: On, only for sources you trust\n\nHow updates work:\n\n1. Sentinel Wizard updates from the Sentinel GitHub Pages repository.\n2. Third-party add-ons update from their own installed repositories.\n3. Use Refresh Repositories when an update is not appearing.\n4. Use Force Check for Add-on Updates after adding or repairing repositories.\n5. Clear failed install packages if updates repeatedly fail.\n\nSentinel repo maintenance steps after code changes:\n\n1. Increase add-on version.\n2. Rebuild wizard.zip and/or repo.zip.\n3. Regenerate addons.xml.\n4. Regenerate addons.xml.md5.\n5. Push to GitHub.\n6. Run Refresh Repositories inside Kodi."""
    xbmcgui.Dialog().textviewer("Update Guide", text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_broken_source_guide():
    text = """Broken Source Fix Guide\n\n1. Go to Kodi Settings > File Manager.\n2. Open the source that is failing.\n3. Confirm the URL is spelled correctly.\n4. Confirm it opens in Downloader or a browser.\n5. If the source is dead, remove it.\n6. Add the updated source URL.\n7. Go to Add-ons > Install from zip file and retest.\n8. Run Sentinel Update Center > Refresh Repositories.\n\nDo not delete working repositories blindly. Backup first."""
    xbmcgui.Dialog().textviewer("Broken Source Fix Guide", text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_broken_repo_guide():
    text = """Broken Repository Fix Guide\n\n1. Open Add-ons > My Add-ons > Add-on repository.\n2. Find the repository that is failing.\n3. Open Information.\n4. Try Update.\n5. If still broken, disable it first.\n6. Clear failed install packages in Sentinel Repair Center.\n7. Reinstall the current repository ZIP from its source.\n8. Run Refresh Repositories.\n9. Try installing/updating the add-on again.\n\nIf one repository breaks the build, disable it and continue testing the others."""
    xbmcgui.Dialog().textviewer("Broken Repository Fix Guide", text)
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True)


def show_safe_mode_guide():
    text = """Sentinel Safe Mode Recovery\n\nUse this when Kodi becomes slow, unstable, or add-ons fail repeatedly.\n\n1. Open Sentinel Wizard.\n2. Go to Build Profiles.\n3. Apply Sentinel Safe Mode.\n4. Fully close Kodi.\n5. Reopen Kodi.\n6. Go to Sentinel Repair Center.\n7. Clear cache, thumbnails, and failed install packages.\n8. Refresh repositories.\n9. Reapply Sentinel Lite before adding more add-ons.\n\nFor Insignia Fire TV, never jump straight back to Max after a crash. Start with Lite."""
    xbmcgui.Dialog().textviewer("Safe Mode Recovery Guide", text)
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
    elif mode == "update_center":
        list_update_center()
    elif mode == "repair_center":
        list_repair_center()
    elif mode == "refresh_repos":
        refresh_repos()
    elif mode == "force_updates":
        force_updates()
    elif mode == "open_available_updates":
        open_available_updates()
    elif mode == "open_my_addons":
        open_my_addons()
    elif mode == "update_guide":
        show_update_guide()
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
    elif mode == "addon_manifest":
        show_addon_manifest()
    elif mode == "install_guide":
        show_install_guide()
    elif mode == "broken_source_guide":
        show_broken_source_guide()
    elif mode == "broken_repo_guide":
        show_broken_repo_guide()
    elif mode == "safe_mode_guide":
        show_safe_mode_guide()
    elif mode == "legal_addons":
        show_legal_addons()
    elif mode == "about":
        show_about()
    else:
        xbmcplugin.endOfDirectory(HANDLE, succeeded=False)


if __name__ == "__main__":
    router()
