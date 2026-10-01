#!/usr/bin/env python3
"""Dependency-free internal link checker for the generated site in public/.

Usage: python3 scripts/check-links.py [public]

Verifies that:
  - every internal href/src/srcset reference in a shipped .html file resolves
    to a shipped file (exact case, so macOS matches ubuntu CI),
  - every <loc> in sitemap.xml resolves to a shipped page,
  - the 404 page and home page are present.

Exits 1 and lists every broken reference if anything fails.
"""

import os
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit

ATTR_REF = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
SRCSET = re.compile(r"""srcset\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
SKIP_SCHEMES = ("http:", "https:", "mailto:", "tel:", "data:", "javascript:")


def collect_files(root):
    files = set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        rel_dir = os.path.relpath(dirpath, root)
        for name in filenames:
            if name.startswith("."):
                continue
            rel = name if rel_dir == "." else posixpath.join(rel_dir.replace(os.sep, "/"), name)
            files.add(rel)
    return files


def resolve(ref, from_file):
    """Return the normalized site-relative path a reference points at,
    or None when the reference is external or empty."""
    ref = ref.strip()
    if not ref or ref.startswith("#") or ref.startswith(SKIP_SCHEMES) or ref.startswith("//"):
        return None
    path = ref if ref.startswith("/") else posixpath.join(posixpath.dirname(from_file), ref)
    path = path.split("#", 1)[0].split("?", 1)[0]
    path = posixpath.normpath(path)
    if path in (".", "/"):
        return "index.html"
    return path.lstrip("/")


def target_exists(path, files):
    """A URL path resolves to a file, a directory index, or a .html sibling."""
    if path.startswith(".."):
        return False
    if path in files:
        return True
    if path.endswith(".html"):
        return False
    return (path + "/index.html") in files or (path + ".html") in files


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "public"
    if not os.path.isdir(root):
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 2

    files = collect_files(root)
    problems = []

    for required in ("index.html", "404.html"):
        if required not in files:
            problems.append(f"{root}/{required} is missing")

    for rel in sorted(files):
        if not rel.endswith(".html"):
            continue
        with open(os.path.join(root, rel), encoding="utf-8") as handle:
            text = handle.read()
        refs = ATTR_REF.findall(text)
        for srcset in SRCSET.findall(text):
            refs.extend(part.strip().split()[0] for part in srcset.split(",") if part.strip())
        for ref in refs:
            path = resolve(ref, rel)
            if path is None:
                continue
            if not target_exists(path, files):
                problems.append(f"{rel}: broken reference {ref!r} -> {path}")

    sitemap = os.path.join(root, "sitemap.xml")
    if os.path.isfile(sitemap):
        tree = ET.parse(sitemap)
        for loc in tree.iter():
            if not loc.tag.endswith("loc") or not loc.text:
                continue
            url = loc.text.strip()
            # <loc> entries are absolute URLs; validate their path portion.
            path = resolve(urlsplit(url).path, "sitemap.xml")
            if path is None:
                continue
            if not target_exists(path, files):
                problems.append(f"sitemap.xml: broken <loc> {url}")
    else:
        problems.append(f"{root}/sitemap.xml is missing")

    if problems:
        print(f"FAIL: {len(problems)} problem(s)")
        for problem in problems:
            print("  " + problem)
        return 1

    html_count = sum(1 for f in files if f.endswith(".html"))
    print(f"OK: {html_count} HTML files, {len(files)} shipped files, all internal references resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
