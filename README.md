SENTINEL Build Kodi Repository

Automated Kodi 21.3 repository and wizard deployment powered by GitHub Pages and GitHub Actions.

Overview

This repository hosts the SENTINEL Kodi Build installation packages, repository files, wizard installer, and automated deployment workflows.

The project supports:

* Kodi 21.3 installs
* Direct Downloader installation
* GitHub Pages hosting
* Automated artifact publishing
* Auto-generated MD5 manifests
* Short install URLs
* Kodi repository deployment automation

⸻

Direct Install

Downloader Code

5075635

Short URL

https://aftv.news/5075635

TinyURL

https://tinyurl.com/sentinelkodi

⸻

GitHub Pages Repository

Main Repository URL

https://akahwaj.github.io/adel-forge-kodi-repo/

Repository ZIP

https://akahwaj.github.io/adel-forge-kodi-repo/repo.zip

Wizard ZIP

https://akahwaj.github.io/adel-forge-kodi-repo/wizard.zip

Addons Manifest

https://akahwaj.github.io/adel-forge-kodi-repo/addons.xml

MD5 Checksum

https://akahwaj.github.io/adel-forge-kodi-repo/addons.xml.md5

⸻

Kodi File Manager Source

Add this source in Kodi File Manager:

https://akahwaj.github.io/adel-forge-kodi-repo/

Suggested source name:

SENTINEL

⸻

Installation Methods

Method 1 — Downloader App

1. Open Downloader
2. Enter code:

5075635

3. Download the wizard ZIP
4. Install from ZIP in Kodi

⸻

Method 2 — Kodi File Manager

1. Open Kodi
2. Go to Settings
3. File Manager
4. Add Source
5. Enter:

https://akahwaj.github.io/adel-forge-kodi-repo/

6. Install repository ZIP
7. Install wizard ZIP

⸻

Repository Structure

.github/workflows/
plugin.sentinel.wizard/
repository.sentinel.build/
addons.xml
addons.xml.md5
repo.zip
wizard.zip
index.html

⸻

Automated GitHub Actions Workflow

The repository includes automated workflows for:

* Kodi artifact publishing
* GitHub Pages deployment
* MD5 generation
* Repository validation
* Artifact alias generation

Workflow file:

.github/workflows/kodi-publish.yml

⸻

Included Artifacts

Repository Package

repository.sentinel.build-1.0.0.zip

Wizard Package

plugin.sentinel.wizard-1.0.0.zip

Shortcut Aliases

repo.zip
wizard.zip

⸻

Validation & Testing

Automated tests verify:

* Required Kodi artifacts exist
* addons.xml structure is valid
* MD5 checksum correctness
* Workflow commands are correct
* GitHub Pages install endpoints exist

Test command:

pytest -q

⸻

GitHub Pages Deployment

GitHub Pages is configured to deploy from:

main branch / (root)

Live site:

https://akahwaj.github.io/adel-forge-kodi-repo/

⸻

Notes

* .nojekyll is included to prevent GitHub Pages processing issues.
* Root install artifacts are committed directly for immediate install availability.
* GitHub Actions automatically updates generated artifacts after repository changes.

⸻

License

MIT License

⸻

Maintainer

Akahwaj / SENTINEL Build Project