# Repository Guidelines

## Project Structure & Module Organization

This is a React 19, TypeScript, and Vite demo for four photo-based cursor mascots.

- `src/App.tsx` defines the gallery; `src/App.css` and `src/index.css` contain page and global styles.
- `src/components/cursor-buddy.tsx` implements pointer tracking, click reactions, and keyboard activation.
- `public/mascots/` contains served WebP atlases. Reference them through `/mascots/...` URLs.
- `characters/<name>/` stores generated artwork, normalized PNG sheets, prompts, and visual checks. Read `characters/README.md` before rebuilding assets.
- `.agents/skills/cursor-buddy/` contains the bundled component, artwork instructions, and Python build helpers.
- `dist/` is generated output; do not edit it directly. No dedicated test directory currently exists.

## Build, Test, and Development Commands

Use pnpm and preserve `pnpm-lock.yaml`. On Windows PowerShell, use `pnpm.cmd` if script execution blocks `pnpm`.

- `pnpm install --frozen-lockfile`: install locked dependencies.
- `pnpm dev`: start the local Vite development server.
- `pnpm build`: run TypeScript checks and generate `dist/`.
- `pnpm lint`: run Oxlint, including React Hooks rules.
- `pnpm preview`: serve the production build locally.
- `python .agents/skills/cursor-buddy/scripts/mascot.py nik --skip-generate`: rebuild and validate Nik's atlases. Requires Pillow, NumPy, and SciPy.

## Coding Style & Naming Conventions

Match existing TypeScript: two-space indentation, single quotes, and generally no semicolons. Use function components, PascalCase component names, camelCase variables, and explicit prop types. Keep imports and code free of unused declarations. Oxlint is configured in `.oxlintrc.json`; no dedicated formatter is configured.

Use lowercase character slugs and paired filenames: `<name>-directions.webp` and `<name>-reactions.webp`. Keep both normalized source sheets at identical dimensions and preserve real transparency.

## Testing Guidelines

No automated test framework, `test` script, or coverage threshold is configured. Run build and lint before submitting changes. For mascot changes, run the bundled validation pipeline and visually inspect left/right orientation, transparency, alignment, and symbol clipping. Check pointer tracking, click reactions, Tab/Enter/Space activation, narrow layouts, and reduced-motion behavior in the browser. Report checks that could not be completed.

## Commit & Pull Request Guidelines

This checkout has no Git metadata, so historical commit conventions cannot be verified. Use concise imperative commit subjects, optionally prefixed with `feat:`, `fix:`, or `docs:`. Keep commits focused.

PRs should explain the change, link relevant issues, list validation performed, and include screenshots for visual changes. Retain source artwork and prompts needed to reproduce new atlases. Never commit secrets, `node_modules/`, or generated `dist/` output.
