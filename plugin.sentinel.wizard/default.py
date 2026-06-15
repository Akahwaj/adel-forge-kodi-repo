import sys
import urllib.parse

import xbmcgui
import xbmcplugin


HANDLE = int(sys.argv[1])
BASE_URL = sys.argv[0]


def plugin_url(action):
    return BASE_URL + "?" + urllib.parse.urlencode({"action": action})


def add_directory_item(label, action, description):
    item = xbmcgui.ListItem(label=label)
    item.setInfo("video", {"title": label, "plot": description})
    xbmcplugin.addDirectoryItem(
        HANDLE,
        plugin_url(action),
        item,
        isFolder=False,
    )


def show_home():
    add_directory_item(
        "Installation Profiles",
        "profiles",
        "View SENTINEL profile options for different Kodi devices.",
    )
    add_directory_item(
        "Service Setup",
        "services",
        "View setup notes for supported accounts and tracking services.",
    )
    add_directory_item(
        "Maintenance",
        "maintenance",
        "Open cache, update, and troubleshooting guidance.",
    )
    xbmcplugin.endOfDirectory(HANDLE)


def show_dialog(title, lines):
    xbmcgui.Dialog().textviewer(title, "\n".join(lines))


def run_action(action):
    if action == "profiles":
        show_dialog(
            "SENTINEL Profiles",
            [
                "Lite: for low-storage devices.",
                "Premium: balanced setup for 4K streaming devices.",
                "Max: full setup for high-performance devices.",
                "Sports: focused setup for sports-oriented builds.",
            ],
        )
    elif action == "services":
        show_dialog(
            "Service Setup",
            [
                "Configure accounts only through each provider's official website.",
                "After account setup, authorize supported add-ons from their own settings screens.",
                "Use Trakt from trakt.tv for watch history and progress sync.",
            ],
        )
    elif action == "maintenance":
        show_dialog(
            "Maintenance",
            [
                "Use Kodi settings to clear cache and packages when storage is low.",
                "Use Add-ons > Available updates to update installed add-ons.",
                "Check Settings > System > Logging when troubleshooting install failures.",
            ],
        )
    else:
        show_home()


params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
run_action(params.get("action"))
