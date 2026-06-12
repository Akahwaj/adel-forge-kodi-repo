#!/usr/bin/env python3
"""Regenerate addons.xml / addons.xml.md5 and package each add-on into a zip."""

import hashlib
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADDON_IDS = ["plugin.program.adelforgewizard", "repo.adelforgewizard"]

EXCLUDE_DIRS = {".git", "__pycache__"}


def read_addon_xml(addon_id):
    path = os.path.join(ROOT, addon_id, "addon.xml")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r"<\?xml[^>]*\?>\s*", "", content, count=1)
    return content.strip()


def get_version(addon_id):
    match = re.search(r'version="([^"]+)"', read_addon_xml(addon_id))
    return match.group(1)


def write_addons_xml():
    parts = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', "<addons>"]
    parts.extend(read_addon_xml(addon_id) for addon_id in ADDON_IDS)
    parts.append("</addons>")
    content = "\n".join(parts) + "\n"

    addons_xml_path = os.path.join(ROOT, "addons.xml")
    with open(addons_xml_path, "w", encoding="utf-8") as f:
        f.write(content)

    digest = hashlib.md5(content.encode("utf-8")).hexdigest()
    with open(os.path.join(ROOT, "addons.xml.md5"), "w", encoding="utf-8") as f:
        f.write(digest)

    return digest


def build_zip(addon_id):
    version = get_version(addon_id)
    addon_dir = os.path.join(ROOT, addon_id)
    zip_path = os.path.join(addon_dir, "{}-{}.zip".format(addon_id, version))

    if os.path.exists(zip_path):
        os.remove(zip_path)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for dirpath, dirnames, filenames in os.walk(addon_dir):
            dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
            for filename in filenames:
                if filename.endswith(".zip"):
                    continue
                file_path = os.path.join(dirpath, filename)
                arcname = os.path.join(addon_id, os.path.relpath(file_path, addon_dir))
                zf.write(file_path, arcname)

    return zip_path


def main():
    digest = write_addons_xml()
    print("addons.xml.md5:", digest)
    for addon_id in ADDON_IDS:
        print("Built", build_zip(addon_id))


if __name__ == "__main__":
    main()
