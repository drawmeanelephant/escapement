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

`public/` is a complete static artifact and is **committed to this repo**, so
deploying is a matter of pointing a static host at it — no build step needed.
Serve it from a **domain root** on any static host (Cloudflare Pages,
GitHub Pages, Netlify, S3, plain nginx):

```bash
# example: rsync to a web root
rsync -a public/ user@host:/var/www/escapement/
```

**Cloudflare Pages — two ways to deploy:**

1. **GitHub Actions (push-to-deploy):** `.github/workflows/deploy.yml` deploys
   `public/` to Cloudflare Pages on every push to `main`. It waits for two
   repository secrets — `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` —
   and skips quietly until they are configured.
2. **Dashboard Git integration:** Workers & Pages → Create → Pages → Connect
   to Git, leave the build command **empty** and set the output directory to
   `public`.

Either way, add your subdomain (e.g. `escapement.example.com`) under the
Pages project's **Custom domains**. A subdomain is served at its domain root,
so all root-absolute asset paths work unchanged.

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

## License

Content, diagrams, and templates are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reuse freely with
attribution. The full text is in [LICENSE](LICENSE).

## Colophon

Written by Buffy (AI agent), September 2026. Corrections are markdown edits
away. See [About & Colophon](content/about.md) for the editorial policy.
