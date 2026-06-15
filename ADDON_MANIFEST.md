# SENTINEL Build Add-on Manifest

This repository currently publishes these installable Kodi packages:

| Add-on ID | Version | Package |
| --- | --- | --- |
| `repository.sentinel.build` | `1.0.0` | `repository.sentinel.build-1.0.0.zip` |
| `plugin.sentinel.wizard` | `1.0.0` | `plugin.sentinel.wizard-1.0.0.zip` |

## Kodi Source

Use this source URL in Kodi 21.3:

```text
https://raw.githubusercontent.com/Akahwaj/adel-forge-kodi-repo/main/
```

## Install Flow

1. In Kodi, go to **Settings > File Manager > Add Source**.
2. Add the source URL above and name it `sentinel-build`.
3. Go to **Add-ons > Install from zip file**.
4. Open `sentinel-build` and install `repository.sentinel.build-1.0.0.zip`.
5. Go to **Add-ons > Install from repository > SENTINEL Build Repository > Program add-ons**.
6. Install `SENTINEL Wizard`.

## Published Repository Metadata

Kodi reads:

- `addons.xml`
- `addons.xml.md5`
- `repository.sentinel.build/addon.xml`
- `plugin.sentinel.wizard/addon.xml`

The package archives must keep the top-level add-on folders inside the zip files. For example, the repository zip must contain:

```text
repository.sentinel.build/addon.xml
```

and the wizard zip must contain:

```text
plugin.sentinel.wizard/addon.xml
```

The same package files are also published in Kodi repository layout:

```text
repository.sentinel.build/repository.sentinel.build-1.0.0.zip
plugin.sentinel.wizard/plugin.sentinel.wizard-1.0.0.zip
```
