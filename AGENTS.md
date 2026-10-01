# La Famille Site — Agent Operating Manual

Welcome to the family. This repository contains a handcrafted, local-first static website generated with [La Famille](https://github.com/drawmeanelephant/la-famille). AI agents (Claude, Cursor, Copilot, Antigravity, Gemini) and human authors work collaboratively here as digital gardeners tending this web homestead.

## 1. System Philosophy & Architecture
- **Digital Homestead**: A personal corner of the web celebrating clean prose, local-first control, and craft aesthetics (*"eight arms, one burger, infinite enthusiasm"*).
- **Static Output**: La Famille compiles Markdown from `content/` and HTML templates from `templates/` into static files in `public/`.
- **Never Edit `public/`**: The `public/` directory is generated output. All edits belong in source files under `content/`, `templates/`, `assets/`, or `config.yaml`.
- **Direct Implementation**: Agents have ownership to create new posts, refine copywriting, adjust themes, fix broken links, and validate changes before handoff.

## 2. Directory Structure & File Conventions
- `content/`: Markdown (`.md`) source files.
- `templates/`: HTML templates using Go `html/template` syntax.
  - Bundled themes: `layout-octoburger.html` (flagship soul theme), `layout.html`, `layout-terminal.html`, `layout-editorial.html`, `layout-midnight.html`.
- `assets/`: Static assets (`css/`, `js/`, `img/`).
- `config.yaml`: Central site configuration.
- `public/`: Generated static site (committed in this repo for direct static hosting; never edit by hand).
- `static/`: Hand-written files staged into `public/` at ship time (e.g. `404.html`), because generator builds clean `public/`.
- `.agents/plans/`: Recommended directory for agent task plans and scratchpads.

## 3. Content Authoring Rules
- **Frontmatter Standard**:
  Every content file must begin with valid YAML frontmatter:
  ```yaml
---
title: "A Descriptive Title"
description: "A concise summary for search engines and social cards."
date: "YYYY-MM-DD"
tags:
  - tag-name
categories:
  - category-name
layout: layout-editorial  # optional: override default theme for this page
---
```
- **Slug & File Naming**: Use lowercase alphanumeric characters and hyphens (e.g. `content/my-post.md` or `content/blog/announcement.md`). Avoid uppercase letters, spaces, or special characters in filenames.
- **Internal Linking**:
  - Always link using relative markdown filenames: `[About](about.md)` or `[Overview](../guides/overview.md)`.
  - Never use `.html` extensions in internal links; the generator resolves markdown paths to clean URL directories automatically.
  - Avoid broken internal links; run `la-famille check` to detect them.
- **Images & Figures**:
  - Place images in `assets/img/` and reference them with `/assets/img/<filename>`.
  - Standalone images with titles automatically become HTML `<figure>` tags with `<figcaption>`.

## 4. CLI Commands & Workflow
Always use the `la-famille` CLI to author and verify content:

- **Preview Site**:
  ```bash
la-famille serve --watch
  ```
  Starts local preview server at `http://localhost:8080` with auto-rebuild and live reload.

- **Scaffold New Content**:
  ```bash
la-famille new <slug> --title "<Title>" --description "<Summary>"
  ```
  Normalizes slug and populates valid frontmatter.

- **Diagnostic Check (Mandatory Verification)**:
  ```bash
la-famille check
  ```
  Verifies internal links, dates, metadata descriptions, and URL safety. Agents must ensure `check` reports 0 errors before finishing tasks.

- **Compile Static Output**:
  ```bash
la-famille build
  ```
  Generates static pages, sitemap.xml, RSS feed, and search index.

- **Export RAG Knowledge Bundles**:
  ```bash
la-famille rag
  ```
  Exports site content into RAG-friendly markdown bundles under `public/rag-archive/`. Note: `build` cleans `public/`, so always publish in the order **build, then rag, then stage `static/` extras** (`cp static/404.html public/404.html`; deploy CI does the same automatically).

- **Explore Bundled Themes**:
  ```bash
la-famille themes
  ```

- **Ship-Time Link Check**:
  ```bash
python3 scripts/check-links.py public
  ```
  Verifies every internal reference in `public/` resolves (also run by `.github/workflows/check.yml` on every push and PR).

## 5. Execution Guardrails for Agents
1. **Planning**: Before complex refactoring or multi-file changes, create a brief plan in `.agents/plans/<task-id>.md`.
2. **Quality Gate**: Before declaring any content authoring or theme task complete, run `la-famille check` and `la-famille build` locally. Both must succeed with zero errors. Also run `python3 scripts/check-links.py public`.
3. **Keep Source and Build in Sync**: The cache (`.la-famille-cache.json`) is gitignored, but `public/` is committed so static hosts can serve the repo directly. After content changes, rebuild (build → rag → stage `static/`) and commit the refreshed `public/` alongside the source edits.
