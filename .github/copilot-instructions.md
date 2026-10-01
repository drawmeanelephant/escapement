# GitHub Copilot Instructions for La Famille Site

This project is a static website built with [La Famille](https://github.com/drawmeanelephant/la-famille).

## Key Instructions for Copilot
- **Content**: Markdown source files live in `content/`. Every page must have YAML frontmatter with `title`, `description`, and `date`.
- **Links**: Use relative markdown links between content files (e.g. `[About](about.md)` or `[Post](../posts/my-post.md)`). Do not write `.html` links.
- **Templates**: Layouts live in `templates/` using Go `html/template` syntax. Page layouts can be customized via frontmatter `layout: <theme>`.
- **Validation**: After editing content or templates, run `la-famille check` to verify internal links, slugs, and metadata.
- **Build**: Run `la-famille build` to compile the static site into `public/`. Never edit `public/` directly.
- **Full Agent Manual**: Refer to `AGENTS.md` for detailed rules of engagement and conventions.
