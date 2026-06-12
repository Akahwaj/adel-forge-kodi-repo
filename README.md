# Sentinel Build 2026

Sentinel Build 2026 is a premium Kodi repository and wizard ecosystem optimized for Fire TV and Android TV devices.

## Features
- Sentinel Wizard
- Fire TV optimization profiles
- Buffer/cache tuning
- Premium FENtastic-based experience
- Backup and restore guidance
- Curated add-on ecosystem
- Lite, Premium, Max, Sports, and Safe Mode profiles

## Build Editions
### Sentinel Lite
Fastest configuration for Fire Stick and low-storage devices.

### Sentinel Premium
Balanced premium setup using curated movie and TV add-ons.

### Sentinel Max
Expanded feature set for higher-end Android TV and Shield-style devices.

### Sentinel Sports
Sports-focused edition with live and sports integrations.

## Install Flow
1. Install Kodi 21 Omega
2. In Kodi File Manager, choose **Install from zip** and enter the short URL directly:
   - Repository (recommended, enables auto-updates): `https://akahwaj.github.io/adel-forge-kodi-repo/repo.zip`
   - Wizard only (one-time install): `https://akahwaj.github.io/adel-forge-kodi-repo/wizard.zip`
3. Open **Adel Forge Wizard** from the Programs add-ons
4. Apply Lite, Premium, Max, Sports, or Safe profile
5. Configure preferred services and add-ons

## Adel Forge Wizard
The `plugin.program.adelforgewizard` add-on (in this repo) provides:
- **Build Profiles** &mdash; Lite, Premium, Max, Sports, and Safe Mode, each applying a
  tuned `advancedsettings.xml` cache profile and listing its recommended add-on set
- **Maintenance Tools** &mdash; clear general cache, clear thumbnail cache, clear add-on
  packages, reset cache tuning
- **Backup & Restore** &mdash; back up `userdata` to a zip, view available backups, and
  see restore instructions
- **Legal Streaming Add-ons** &mdash; an info screen pointing to official, legal
  streaming options (Plex, Pluto TV, YouTube, Tubi, PBS Kids, Netflix/Disney+/Prime
  Video apps, and PVR IPTV Simple Client for your own licensed M3U)

### Building the repository
Run `python3 tools/build_repo.py` after changing any `addon.xml` to regenerate
`addons.xml`, `addons.xml.md5`, and the per-addon zip packages.

## Core Experience
- FEN Light
- Umbrella
- POV
- Seren
- The Crew
- Chains
- Scrubs V2
- VIDSRC

## Official Repository
https://github.com/Akahwaj/adel-forge-kodi-repo
