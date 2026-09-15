# Reaction artwork refresh — 2026-09-15

Regenerated Nik, Thinh, Nemo, Phuong and Hung with the built-in image generation tool, using each character's existing directions sheet as the identity reference. Nolan was added concurrently and is outside this refresh.

Each sheet contains nine expressions with the updated icons: sun, heart, three sparkles, exclamation mark, shooting star, flower, z z z, spiral and party popper. Corner choices in row-major order: left, right, right, left, right, left, left, right, left.

For each character, `reactions-v2-prompt.txt` preserves the exact prompt, `reactions-generated-v2.png` preserves the generated artwork, `reactions.png` is the build input and `reactions-before-v2.png` preserves the previous input. Public atlas paths remain `/mascots/<name>-reactions.webp`.

Hung's existing directions and previous reactions were copied from `D:/projects/hunghg.me/characters/hung/` to make this project's artwork reproducible locally.

## Normalization

For Nik, Nemo and Phuong:

```powershell
python characters/normalize_rows.py characters/<name>/reactions-generated-v2.png characters/<name>/reactions.png 443 831 560
```

For Thinh, use tile size 565. Hung's generated sheet already matches the 1254 × 1254 source layout and is used directly.

Rebuild each character with:

```powershell
python .agents/skills/cursor-buddy/scripts/mascot.py <name> --skip-generate
```

## Verification

| Character | Shift at 140 px | Shoulder width change | Palette match |
| --- | ---: | ---: | ---: |
| Nik | 0.00 px | 1.2% | 75.8% |
| Thinh | 0.00 px | 0.7% | 84.2% |
| Nemo | 0.00 px | 0.3% | 78.4% |
| Phuong | 0.00 px | 1.4% | 85.5% |
| Hung | 0.00 px | 0.1% | 88.3% |

All five pipelines pass alpha, edge contact and alignment checks. Generated artwork and built atlases were visually inspected for expression order and icon clipping. Existing direction sheets were visually checked for left/right orientation.

Browser checks: pointer-facing heads observed, click and Tab/Enter/Space reactions observed, 390 px layout and Nik's reaction icon checked. Reduced-motion behavior was reviewed in the existing component but was not emulated in the browser. TypeScript/Vite build and Oxlint pass.
