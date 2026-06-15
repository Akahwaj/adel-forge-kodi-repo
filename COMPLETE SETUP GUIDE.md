# 🎯 SENTINEL BUILD - COMPLETE SETUP PACKAGE

**Everything You Need to Deploy SENTINEL BUILD to GitHub**

-----

## 📦 What's Included

This package contains:

1. ✅ **Complete Script** - `sentinel-build-complete.sh`
- Generates all files automatically
- Smart wizard with maintenance center
- All 18 add-ons configured
- Complete documentation
1. ✅ **GitHub Actions Workflow** - `.github/workflows/validate-kodi-repo.yml`
- Auto-validates repository
- Auto-creates releases
- Deploys to GitHub Pages
- Sends notifications
1. ✅ **Setup Instructions** - This file
- Step-by-step deployment guide
- Verification checklist
- Testing instructions
1. ✅ **Generated Files** (created by script)
- `README.md` - Complete with all services
- `ADDON_MANIFEST.md` - Full documentation
- `addons.xml` - All 18 add-ons
- `addons.xml.md5` - Integrity checksum
- `repository.sentinel.build-1.0.0.zip` - Repository addon
- `plugin.sentinel.wizard-1.0.0.zip` - Wizard + maintenance
- `LICENSE` - GPL-3.0

-----

## 🚀 DEPLOYMENT STEPS (10 Minutes)

### STEP 1: Prepare Your GitHub Repository

```bash
# Option A: Use existing repo
cd /path/to/adel-forge-kodi-repo
git pull origin main
git checkout main

# Option B: Clone fresh
git clone https://github.com/Akahwaj/adel-forge-kodi-repo.git
cd adel-forge-kodi-repo
```

### STEP 2: Clean Existing Files (if needed)

```bash
# Remove old files but keep .git
find . -maxdepth 1 -type f ! -name ".gitignore" -delete
find . -maxdepth 1 -type d ! -name ".git" -delete 2>/dev/null || true

# Verify cleanup
ls -la  # Should only show .git folder
```

### STEP 3: Run SENTINEL BUILD Setup Script

```bash
# Download or copy the script
bash sentinel-build-complete.sh

# This creates:
# - LICENSE
# - README.md
# - ADDON_MANIFEST.md
# - addons.xml
# - addons.xml.md5
# - plugin.sentinel.wizard-1.0.0.zip
# - repository.sentinel.build-1.0.0.zip
# - plugin.sentinel.wizard/ (folder)
# - repository.sentinel.build/ (folder)
```

### STEP 4: Create GitHub Actions Workflow

```bash
# Create workflow directory
mkdir -p .github/workflows

# Use the included workflow file:
# .github/workflows/validate-kodi-repo.yml
```

### STEP 5: Stage and Commit

```bash
# Add all files
git add -A

# Verify changes
git status

# Commit
git commit -m "SENTINEL BUILD - Complete Setup with Real-Debrid, TorBox, Premiumize, Trakt"

# Push to GitHub
git push origin main
```

### STEP 6: Verify Workflow Execution

```bash
# Go to GitHub Actions
# https://github.com/Akahwaj/adel-forge-kodi-repo/actions

# Wait for workflow to complete (2-3 minutes)
# Should show:
# ✅ Validate - Check Required Files
# ✅ Validate - Validate addons.xml
# ✅ Validate - Verify MD5 Checksum
# ✅ Build - Create Release Artifacts
# ✅ Build - Generate Build Report
# ✅ Deploy - Create GitHub Pages Index
# ✅ Deploy - Deploy to GitHub Pages
# ✅ Deploy - Create Release
# ✅ Notify - Send Notifications
```

-----

## ✅ VERIFICATION CHECKLIST

After deployment, verify everything:

### Repository Files

- [ ] LICENSE (1KB)
- [ ] README.md (6KB+)
- [ ] ADDON_MANIFEST.md (3KB+)
- [ ] addons.xml (8KB)
- [ ] addons.xml.md5 (45 bytes)
- [ ] plugin.sentinel.wizard-1.0.0.zip (7KB)
- [ ] repository.sentinel.build-1.0.0.zip (900 bytes)

### Directories

- [ ] .github/workflows/ folder exists
- [ ] plugin.sentinel.wizard/ folder exists
- [ ] repository.sentinel.build/ folder exists

### GitHub Pages

- [ ] GitHub Pages enabled
- [ ] GitHub Pages showing index.html
- [ ] Visit: <https://akahwaj.github.io/adel-forge-kodi-repo/>

### GitHub Releases

- [ ] Release created: v1.1.0-SENTINEL
- [ ] All ZIPs available for download
- [ ] Release notes present

### GitHub Actions

- [ ] Workflow file present: `.github/workflows/validate-kodi-repo.yml`
- [ ] All jobs passing (green checkmarks)
- [ ] No failed validations

-----

## 🧪 TEST IN KODI (5 Minutes)

### Test the Repository

1. **Open Kodi** on Fire Stick, Shield, or Android TV
1. **Settings** → **File Manager** → **Add Source**
1. **URL:** `https://akahwaj.github.io/adel-forge-kodi-repo/`
1. **Name:** `sentinel-build`
1. Click **OK**

### Install Repository

1. **Add-ons** → **Install from Zip File**
1. Select source: `sentinel-build`
1. Find: `repository.sentinel.build-1.0.0.zip`
1. Install it
1. Wait for success notification

### Install Wizard

1. **Add-ons** → **Install from Repository**
1. Select: **SENTINEL Build Repository**
1. Go to: **Program Add-ons**
1. Find: **SENTINEL Wizard**
1. Click **Install**
1. Wait for success

### Launch Wizard

1. **Add-ons** → **Program Add-ons**
1. Find: **SENTINEL Wizard**
1. Click **SENTINEL Wizard** to launch

### Wizard Menu

You should see:

- **Installation Wizard** - Choose profile
- **Maintenance Center** - Cache, updates, troubleshooting
- **About SENTINEL BUILD** - Version info

### Test Features

**Installation Wizard:**

- [ ] Choose "Premium" profile
- [ ] Confirm installation
- [ ] Review 13 repos being added

**Maintenance Center:**

- [ ] Clear Cache & Data
- [ ] Update & Refresh
- [ ] Configuration Guides (Real-Debrid, TorBox, Premiumize, Trakt)
- [ ] Troubleshooting

**Configuration Guides:**

- [ ] Real-Debrid setup guide shows
- [ ] TorBox setup guide shows
- [ ] Premiumize setup guide shows
- [ ] Trakt (FREE) setup guide shows
- [ ] VPN configuration guide shows

-----

## 📊 WORKFLOW FILE (`.github/workflows/validate-kodi-repo.yml`)

[Complete workflow file provided above - copy the entire YAML content]

### What the Workflow Does

1. **Validates** - Checks all required files exist
1. **Validates XML** - Ensures addons.xml is valid
1. **Verifies MD5** - Confirms integrity checksum
1. **Builds** - Creates release artifacts
1. **Deploys** - Pushes to GitHub Pages
1. **Creates Release** - Makes downloadable release
1. **Notifies** - Shows completion status

### Workflow Triggers

- **On every push to main**
- **Manual trigger** (workflow_dispatch)
- **When key files change** (addons.xml, README.md, etc.)

-----

## 🎯 FINAL CHECKLIST

### Before Pushing

- [ ] All files generated by script
- [ ] README.md shows Real-Debrid, TorBox, Premiumize, Trakt
- [ ] addons.xml lists the installable SENTINEL packages
- [ ] Both ZIP files present
- [ ] Directory structure correct

### After Pushing

- [ ] GitHub Actions workflow running
- [ ] All validation steps passing
- [ ] GitHub Pages deployed
- [ ] Release created
- [ ] Can add source to Kodi

### Testing in Kodi

- [ ] Source adds without error
- [ ] Repository ZIP installs
- [ ] Wizard installs
- [ ] Wizard launches
- [ ] All menus work

-----

## 🔗 IMPORTANT URLS

**GitHub Repository:**

```
https://github.com/Akahwaj/adel-forge-kodi-repo
```

**GitHub Pages:**

```
https://akahwaj.github.io/adel-forge-kodi-repo/
```

**Kodi Repository URL:**

```
https://akahwaj.github.io/adel-forge-kodi-repo/
```

**GitHub Actions:**

```
https://github.com/Akahwaj/adel-forge-kodi-repo/actions
```

**GitHub Releases:**

```
https://github.com/Akahwaj/adel-forge-kodi-repo/releases
```

-----

## 📝 SERVICES INCLUDED

All 4 services have complete setup guides in the wizard:

|Service    |Price      |Status            |
|-----------|-----------|------------------|
|Real-Debrid|€8/month   |✅ Full Setup Guide|
|TorBox     |$7/month   |✅ Full Setup Guide|
|Premiumize |€9.99/month|✅ Full Setup Guide|
|Trakt      |FREE       |✅ Full Setup Guide|

-----

## 🆘 TROUBLESHOOTING

### "Workflow failed"

- Check the Actions tab for error details
- Common: Missing files, invalid XML
- Solution: Run script again, verify all files exist

### "Can't add source in Kodi"

- Check internet connection
- Verify GitHub repo is public
- Try with different URL format
- Clear Kodi cache and retry

### "MD5 checksum mismatch"

- Run script again
- It auto-regenerates correct checksum
- Verify addons.xml hasn't been modified

### "No streams in add-ons"

- Need debrid account (Real-Debrid, TorBox, or Premiumize)
- Read setup guides in wizard
- Test debrid account on their website first

### "Wizard doesn't launch"

- Clear Kodi cache
- Restart Kodi
- Reinstall wizard
- Check Kodi version (21.0+)

-----

## 🎉 YOU'RE DONE!

Your SENTINEL BUILD is now:

✅ **Complete** - All files generated
✅ **Validated** - Workflow checking everything
✅ **Deployed** - Live on GitHub
✅ **Published** - Available on GitHub Pages
✅ **Released** - Downloadable release created
✅ **Ready** - Working in Kodi

-----

## 📞 SUPPORT

**Issues:** Create GitHub issue
**Questions:** Check README.md and ADDON_MANIFEST.md
**Feedback:** Use GitHub Discussions

**Repository:**
<https://github.com/Akahwaj/adel-forge-kodi-repo>

-----

## 📋 FILES REFERENCE

|File                               |Size|Purpose                      |
|-----------------------------------|----|-----------------------------|
|sentinel-build-complete.sh         |38KB|Generation script            |
|.github/workflows/validate-kodi-repo.yml       |12KB|CI/CD workflow               |
|README.md                          |6KB |Installation guide + services|
|ADDON_MANIFEST.md                  |3KB |Full documentation           |
|addons.xml                         |8KB |Installable repository manifest          |
|addons.xml.md5                     |45B |Integrity checksum           |
|plugin.sentinel.wizard-1.0.0.zip   |7KB |Wizard + maintenance         |
|repository.sentinel.build-1.0.0.zip|900B|Repository addon             |

**Total: ~75KB** (Very lightweight!)

-----

**SENTINEL BUILD v1.1.0 - The Most Complete Kodi Setup**

© 2026 Akahwaj | Licensed GNU GPL-3.0

Ready to stream! 🎬✨
