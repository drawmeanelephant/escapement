# HOMESTEAD — where the build fought back

Recorded during the Escapement build ([issue #579](https://github.com/drawmeanelephant/la-famille/issues/579)
Phase 1), per the "record, don't silently fix" discipline. Ranked by how many
pages hit each item. Repros are against master @ bb9c495.

## 1. Category case is normalized with per-page warnings — hit: 53/53 pages

Frontmatter `categories: ["Anatomy"]` is rewritten to `"anatomy"`, emitting a
`Content warning` per page. A well-formed site with capitalized category names
gets 53 warnings on its first build.

- **Workaround used:** rewrote every frontmatter value to lowercase (content-side).
- **Possible fixes:** preserve case for display while slugging lowercase;
  or fold case silently (a pure case fold is not a content error).
- **Repro:** `categories: ["Test"]` on any page → warning + normalized slug.

## 2. The RAG archive can't be published by `build` — hit: every publish

The issue's contract wants `public/rag-archive/rag-content.md`. `rag` exports
to `rag_dir`, which defaults *outside* `output_dir`; pointing `rag_dir` inside
`public/` works only until the next `build`, which cleans `output_dir` and
silently deletes the archive.

- **Workaround used:** `rag_dir: "public/rag-archive"` + strict publish order
  **build → rag**, documented in the site README.
- **Possible fixes:** warn when `rag_dir` is inside `output_dir`; or have
  `build` re-emit the rag archive when configured inside it.

## 3. No asset URL rewriting for subpaths — hit: every page with media (4 today, growing)

Image sources pass through unchanged (`internal/transform/figure.go` only
promotes figures). Root-absolute `/assets/...` works at a domain root; subpath
hosts (GitHub Pages project sites) break all images without hand-editing.
`siteurl` is used for canonical/sitemap/robots but not for asset rewriting.

- **Workaround used:** root-absolute paths + README caveat.
- **Possible fixes:** rewrite `/assets/...` with `siteurl`, or emit
  depth-relative asset URLs.

## 4. `check` orphans ignore `site_links` — hit: 1 page (about.md)

A page linked only from `config.yaml` `site_links` is reported as
`orphaned page: no inbound links`. The nav link is a real inbound link.

- **Workaround used:** added a content link from the home page.
- **Possible fix:** count `site_links` targets as inbound links in orphan detection.

## 5. No series/ordering metadata — hit: the 8-part Anatomy series

`FileMeta` has no `Series`/`order` field (as the moonshot review notes). A long
series is a naming convention (`01-…`, `02-…`) plus a hand-maintained index on
the reading-path page.

- **Workaround used:** numbered filenames + manual series index in
  `content/start-here/read-me-first.md`.
- **Possible fixes:** optional `series`/`series_order` frontmatter feeding
  prev/next navigation and a series landing page.

## Not friction (recorded as fine)

- `siteurl` unset warning from `check` is correct and useful for portable sites.
- Graph explorer renders fine at 53 content nodes / 109 SVG elements; search,
  filters, and focus mode all respond, no console errors.
- Cold vs incremental cache behavior works exactly as documented (see
  `sites/README.md` for timings).
