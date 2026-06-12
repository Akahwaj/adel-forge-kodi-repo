ADDON_SOURCES = {
    "Umbrella": "https://umbrellaplug.github.io",
    "The Crew": "https://team-crew.github.io",
    "SALTS": "https://repo.redwizard.xyz",
    "The Gears": "https://unhingedthemes.github.io",
    "Seren": "https://nixgates.github.io/packages",
    "POV": "https://kodifitzwell.github.io/repo/",
    "FEN Light": "https://repo.redwizard.xyz",
    "FenSkeleton": "https://fenskeleton.github.io/zips/repository.fenskeleton/",
    "COSMOS": "https://teamenigma.xyz/repo/",
    "Red Light": "https://repo.redwizard.xyz",
    "VIDSRC": "https://repo.redwizard.xyz",
    "Scrubs V2": "http://jewbmx.github.io",
    "Diggz Free99": "https://tinyurl.com/diggz123",
    "Gratis Red": "https://repo.redwizard.xyz",
    "Chains": "https://unhingedthemes.github.io",
    "Elementum": "Downloader code: 444801",
    "Jacktook": "https://sam-max.github.io/repository.jacktook",
    "MediaFusion": "https://mhdzumair.github.io/MediaFusion",
}

PREMIUM_SERVICES = ["Real-Debrid", "TorBox", "Premiumize", "AllDebrid", "Trakt"]

PROFILES = {
    "lite": {
        "name": "Sentinel Lite",
        "description": (
            "Fastest configuration for Fire TV and low-storage devices. "
            "Minimal cache footprint with a lightweight add-on set."
        ),
        "skin": "FENtastic (Default)",
        "addons": ["FEN Light", "Umbrella", "Scrubs V2", "VIDSRC"],
        "cache": {"memorysize": 20971520, "readfactor": 4, "buffermode": 1},
    },
    "premium": {
        "name": "Sentinel Premium",
        "description": (
            "Balanced premium setup using curated movie and TV add-ons "
            "with a moderate Fire TV safe buffer."
        ),
        "skin": "FENtastic or Arctic Fuse",
        "addons": ["FEN Light", "Umbrella", "POV", "Seren", "FenSkeleton"],
        "cache": {"memorysize": 41943040, "readfactor": 4, "buffermode": 1},
    },
    "max": {
        "name": "Sentinel Max",
        "description": (
            "Full Sentinel add-on reference set for higher-end Android TV, "
            "Shield-style devices, or final build testing after Lite/Premium passes."
        ),
        "skin": "Arctic Fuse (Premium)",
        "addons": [
            "Umbrella",
            "The Crew",
            "SALTS",
            "The Gears",
            "Seren",
            "POV",
            "FEN Light",
            "FenSkeleton",
            "COSMOS",
            "Red Light",
            "VIDSRC",
            "Scrubs V2",
            "Diggz Free99",
            "Gratis Red",
            "Chains",
            "Elementum",
            "Jacktook",
            "MediaFusion",
        ],
        "cache": {"memorysize": 62914560, "readfactor": 5, "buffermode": 1},
    },
    "sports": {
        "name": "Sentinel Sports",
        "description": (
            "Sports-focused edition with a larger live-buffer for sports and live TV add-ons."
        ),
        "skin": "FENtastic (Default)",
        "addons": ["The Crew", "Chains", "Umbrella", "Scrubs V2"],
        "cache": {"memorysize": 41943040, "readfactor": 5, "buffermode": 1},
    },
    "safe": {
        "name": "Sentinel Safe Mode",
        "description": (
            "Stability-first configuration with conservative cache settings, "
            "the default Kodi skin, and no third-party add-on recommendations. "
            "Useful for troubleshooting."
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


def format_addon_manifest(addons):
    lines = []
    for name in addons:
        source = ADDON_SOURCES.get(name, "Source to verify during live Kodi testing")
        lines.append("- {name}\n  Source: {source}".format(name=name, source=source))
    return "\n".join(lines)


def apply_profile(profile_key):
    import xbmcvfs

    profile = PROFILES.get(profile_key)
    if not profile:
        return False

    path = xbmcvfs.translatePath("special://userdata/advancedsettings.xml")
    xml = build_advancedsettings_xml(profile["cache"])
    with xbmcvfs.File(path, "w") as handle:
        return bool(handle.write(xml.encode("utf-8")))
