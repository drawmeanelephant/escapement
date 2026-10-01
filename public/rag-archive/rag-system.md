<file path=".github/workflows/deploy.yml">
<content>
name: Deploy to GitHub Pages

on:
  push:
    branches: ["main", "master"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build-and-deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5
        with:
          enablement: true

      - name: Install La Famille
        run: |
          REPO="drawmeanelephant/la-famille"
          TAG=$(curl -s "https://api.github.com/repos/$REPO/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')
          if [ -z "$TAG" ]; then TAG="v0.1.0-prealpha"; fi
          VERSION="${TAG#v}"
          ARCHIVE="la-famille_${VERSION}_linux_amd64.tar.gz"
          URL="https://github.com/$REPO/releases/download/$TAG/$ARCHIVE"
          echo "Downloading La Famille $TAG..."
          curl -sL "$URL" -o /tmp/la-famille.tar.gz
          tar -xzf /tmp/la-famille.tar.gz -C /usr/local/bin la-famille
          chmod +x /usr/local/bin/la-famille
          la-famille --version

      - name: Build site
        env:
          SITE_URL: ${{ steps.pages.outputs.base_url }}
        run: |
          la-famille build --site-url "$SITE_URL"
          la-famille publish-check --site-url "$SITE_URL"

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: public

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4

</content>
</file>

<file path="README.md">
<content>
# Escapement

**How a mechanical watch actually works** — an exhaustive, cross-linked
explainer site: 53 pages covering the anatomy series (8 parts), the escapement
family tree, the physics of rate and amplitude, complications, landmark
calibres, a chronological history archive (1656–1983), maintenance, and a
glossary.

Built with [La Famille](https://github.com/drawmeanelephant/la-famille)
(layout-editorial theme). Everything is self-contained: no CDNs, no external
fonts, no trackers, hand-drawn SVG diagrams only.

## Layout

| Path | What |
| --- | --- |
| `content/` | 53 markdown pages (the whole site) |
| `assets/img/` | SVG diagrams (gear train, escapement cycle, balance, tourbillon) |
| `templates/layout-editorial.html` | the bundled layout, copied for independence |
| `public/` | **the complete build** — deploy this directory |
| `public/rag-archive/` | machine-readable corpus (`rag-content.md`) for LLM prompts |
| `public/graph/` | self-contained interactive knowledge graph |
| `HOMESTEAD.md` | every place the build fought back (generator backlog) |

## Deploy

`public/` is a complete static artifact. Serve it from a **domain root** on
any static host (GitHub Pages, Netlify, Cloudflare Pages, S3, plain nginx):

```bash
# example: rsync to a web root
rsync -a public/ user@host:/var/www/escapement/
```

Two notes for portability:

1. **Subpath hosting** (e.g. `user.github.io/escapement/`): image references
   are root-absolute (`/assets/...`), so either serve from the root or adjust
   those few paths. Set `siteurl` in `config.yaml` first so canonical links,
   `sitemap.xml`, and `robots.txt` resolve.
2. **RAG archive publishing:** the export lives in `public/rag-archive/`, and
   `build` cleans `public/`. The publish order is **build, then rag** (see
   `HOMESTEAD.md`).

## Rebuild from source

```bash
la-famille --project-root . build   # writes public/
la-famille --project-root . rag     # writes public/rag-archive/
la-famille --project-root . check   # links, orphans, metadata
la-famille --project-root . serve   # local preview
```

The site builds from any checkout or release binary of la-famille — nothing in
this directory depends on the generator repository.

## Colophon

Written by Buffy (AI agent), September 2026. Corrections are markdown edits
away. See [About & Colophon](content/about.md) for the editorial policy.

</content>
</file>

