---
title: "About & Colophon"
description: "Who writes Escapement, how it is built, and why every claim on this site is meant to be checkable."
date: "2026-09-30"
author: "Buffy"
categories: ["orientation"]
tags: ["colophon", "guide"]
---

**Escapement** is an independent explainer site about mechanical horology: how
watches work, why they work *that* way, and what the last four hundred years of
timekeeping got right and wrong.

## Who writes this

Every page was written by **Buffy**, an AI coding agent, as part of an exercise in
building a real, self-contained publication with
[La Famille](https://github.com/drawmeanelephant/la-famille), a Go static site
generator. No page is placeholder text. Where a claim is contested in horology —
the [balance-spring priority dispute](history/1675-the-balance-spring-race.md),
for instance, or whether a [tourbillon](complications/tourbillon.md) helps a
wristwatch at all — the page says so instead of picking a winner silently.

## How it is built

- **Generator:** La Famille, from source or a release binary. The whole site is
  markdown, a config file, and hand-drawn SVG diagrams — no external fonts, no
  CDNs, no trackers,no runtime JavaScript dependencies beyond the self-contained
[graph explorer](/graph/) page the build emits.
- **Diagrams:** every illustration is an SVG drawn for this site, stored in
  `assets/img/`, and rebuildable by editing the file with a text editor.
- **Portability:** the built `public/` directory is a complete static artifact.
  Drop it on any static host. Serve it from a domain root (image paths are
  root-absolute `/assets/...`); from a subpath, adjust those few references.
- **Machine-readable corpus:** each build publishes a `rag-archive/` whose
  `rag-content.md` is the entire site flattened into one coherent document,
  designed to be pasted into a prompt.

## Corrections

Horology writing is full of confident myths (Breguet invented everything,
the Swiss invented the lever, quartz killed mechanical forever). This site tries
to date and attribute its claims; if you find one that is wrong, the fix is a
markdown edit away.

Continue with [Read Me First](start-here/read-me-first.md) for the guided tour,
or [The Five-Minute Watch](start-here/the-five-minute-watch.md) for the whole
machine in one page.
