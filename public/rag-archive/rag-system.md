<file path=".github/workflows/attach-domain.yml">
<content>
name: Attach custom domain

on:
  workflow_dispatch:
    inputs:
      domain:
        description: "Custom domain to attach to the escapement Pages project"
        required: true
        default: "escapement.filed.fyi"

jobs:
  attach:
    runs-on: ubuntu-latest
    env:
      HAS_CF_SECRETS: ${{ secrets.CLOUDFLARE_API_TOKEN != '' && secrets.CLOUDFLARE_ACCOUNT_ID != '' }}
    steps:
      - name: Skip until secrets are configured
        if: env.HAS_CF_SECRETS != 'true'
        run: echo "::notice::CLOUDFLARE_API_TOKEN / CLOUDFLARE_ACCOUNT_ID repo secrets not configured yet — skipping."

      - name: Diagnose and attach domain via Cloudflare API
        if: env.HAS_CF_SECRETS == 'true'
        env:
          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          DOMAIN: ${{ inputs.domain }}
        run: |
          set +e
          API="https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/pages"
          AUTH="Authorization: Bearer ${CLOUDFLARE_API_TOKEN}"

          echo "=== Pages projects in account ==="
          curl -sS "${API}/projects" -H "$AUTH" \
            | jq -r '.result[]? | "\(.name) -> \(.subdomain)  domains: \(.domains | join(", "))"'

          echo "=== Attach ${DOMAIN} to escapement ==="
          curl -sS -X POST "${API}/projects/escapement/domains" \
            -H "$AUTH" -H "Content-Type: application/json" \
            --data "{\"name\": \"${DOMAIN}\"}"
          echo

</content>
</file>

<file path=".github/workflows/check.yml">
<content>
name: Check

on:
  push:
  pull_request:
  workflow_dispatch:

jobs:
  links:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      # public/ is generator output (builds wipe it), so the hand-written 404
      # page lives in static/ and is staged in at ship time. deploy.yml does
      # the same copy before uploading.
      - name: Stage static extras into public/
        run: cp static/404.html public/404.html

      - name: Check internal links
        run: python3 scripts/check-links.py public

</content>
</file>

<file path=".github/workflows/deploy.yml">
<content>
name: Deploy to Cloudflare Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

concurrency:
  group: "cloudflare-pages"
  cancel-in-progress: false

jobs:
  deploy:
    runs-on: ubuntu-latest
    env:
      # Flip to "true" automatically once the repo secrets exist.
      HAS_CF_SECRETS: ${{ secrets.CLOUDFLARE_API_TOKEN != '' && secrets.CLOUDFLARE_ACCOUNT_ID != '' }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      # public/ is generator output (builds wipe it), so the hand-written 404
      # page lives in static/ and is staged in at ship time.
      - name: Stage static extras into public/
        run: cp static/404.html public/404.html

      - name: Skip until secrets are configured
        if: env.HAS_CF_SECRETS != 'true'
        run: echo "::notice::CLOUDFLARE_API_TOKEN / CLOUDFLARE_ACCOUNT_ID repo secrets not configured yet — skipping deploy."

      - name: Ensure Pages project exists
        if: env.HAS_CF_SECRETS == 'true'
        continue-on-error: true
        uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          command: pages project create escapement --production-branch=main

      - name: Deploy public/ to Cloudflare Pages
        if: env.HAS_CF_SECRETS == 'true'
        uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          command: pages deploy public --project-name=escapement --branch=main --commit-dirty=true

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

</content>
</file>

