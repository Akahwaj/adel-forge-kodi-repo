PROFILES = {
    "lite": {
        "name": "Sentinel Lite",
        "description": (
            "Fastest configuration for Fire Stick and low-storage devices. "
            "Minimal cache footprint with a lightweight add-on set."
        ),
        "skin": "FENtastic (Default)",
        "addons": ["FEN Light", "Umbrella", "Scrubs V2"],
        "cache": {"memorysize": 20971520, "readfactor": 4, "buffermode": 1},
    },
    "premium": {
        "name": "Sentinel Premium",
        "description": (
            "Balanced premium setup using curated movie and TV add-ons "
            "with a moderate buffer for smoother playback."
        ),
        "skin": "FENtastic or Arctic Fuse",
        "addons": ["FEN Light", "Umbrella", "POV", "Seren"],
        "cache": {"memorysize": 41943040, "readfactor": 4, "buffermode": 1},
    },
    "max": {
        "name": "Sentinel Max",
        "description": (
            "Expanded feature set and larger cache for higher-end Android "
            "TV and Shield-style devices."
        ),
        "skin": "Arctic Fuse (Premium)",
        "addons": [
            "FEN Light",
            "Umbrella",
            "POV",
            "Seren",
            "The Crew",
            "Chains",
            "Scrubs V2",
            "VIDSRC",
        ],
        "cache": {"memorysize": 104857600, "readfactor": 6, "buffermode": 1},
    },
    "sports": {
        "name": "Sentinel Sports",
        "description": (
            "Sports-focused edition with a larger live-buffer for "
            "streaming sports and live TV add-ons."
        ),
        "skin": "FENtastic (Default)",
        "addons": ["FEN Light", "The Crew", "Chains"],
        "cache": {"memorysize": 62914560, "readfactor": 6, "buffermode": 1},
    },
    "safe": {
        "name": "Sentinel Safe Mode",
        "description": (
            "Stability-first configuration with conservative cache "
            "settings, the default Kodi skin, and no third-party add-on "
            "recommendations. Useful for troubleshooting."
        ),
        "skin": "Kodi Default (Estuary)",
        "addons": [],
        "cache": {"memorysize": 20971520, "readfactor": 4, "buffermode": 0},
    },
}

PROFILE_ORDER = ["lite", "premium", "max", "sports", "safe"]


def build_advancedsettings_xml(cache):
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        "<advancedsettings>\n"
        "  <cache>\n"
        "    <memorysize>{memorysize}</memorysize>\n"
        "    <readfactor>{readfactor}</readfactor>\n"
        "    <buffermode>{buffermode}</buffermode>\n"
        "  </cache>\n"
        "</advancedsettings>\n"
    ).format(**cache)


def apply_profile(profile_key):
    import xbmcvfs

    profile = PROFILES.get(profile_key)
    if not profile:
        return False

    path = xbmcvfs.translatePath("special://userdata/advancedsettings.xml")
    xml = build_advancedsettings_xml(profile["cache"])
    handle = xbmcvfs.File(path, "w")
    handle.write(xml.encode("utf-8"))
    handle.close()
    return True
