# Four photo-based cursor buddies

Created in order: Nik, Thịnh, Nemo, Phương, using the built-in `image_gen` tool.
Each directory contains the generated PNG artwork, the normalized source sheets,
the generation prompts, and a left/right crop for visual direction checks.

The source photos remain at their original locations; the website serves only the
generated WebP atlases in `public/mascots`.

## Rebuild an atlas

From the project root, with Pillow, NumPy and SciPy installed:

```powershell
python .agents/skills/cursor-buddy/scripts/mascot.py nik --skip-generate
python .agents/skills/cursor-buddy/scripts/mascot.py thinh --skip-generate
python .agents/skills/cursor-buddy/scripts/mascot.py nemo --skip-generate
python .agents/skills/cursor-buddy/scripts/mascot.py phuong --skip-generate
```

## Source layout normalization

Some generated sheets have uneven row spacing. `normalize_rows.py` repacks them
without redrawing the art. Both sheets of a character must have the same tile size
because the bundled builder assumes equal source dimensions. The first two numbers
are row boundaries, the third is output tile size, and optional final numbers are
column boundaries selected from visible empty gaps.

```powershell
python characters/normalize_rows.py characters/nik/directions-generated.png characters/nik/directions.png 418 836 560
python characters/normalize_rows.py characters/nik/reactions-generated.png characters/nik/reactions.png 460 815 560
python characters/normalize_rows.py characters/thinh/directions-generated.png characters/thinh/directions.png 418 836 565
python characters/normalize_rows.py characters/thinh/reactions-generated.png characters/thinh/reactions.png 465 833 565
python characters/normalize_rows.py characters/nemo/directions-generated.png characters/nemo/directions.png 410 817 560
python characters/normalize_rows.py characters/nemo/reactions-generated.png characters/nemo/reactions.png 463 842 560 450 840
python characters/normalize_rows.py characters/phuong/directions-generated.png characters/phuong/directions.png 418 828 560
python characters/normalize_rows.py characters/phuong/reactions-generated.png characters/phuong/reactions.png 443 821 560
```

To regenerate visual direction checks:

```powershell
python characters/check_directions.py nik thinh nemo phuong
```

Keep the normalized source PNGs to rebuild without another image-generation call.

## Final validation

`pnpm build` and `pnpm lint` passed. All eight served WebP URLs returned HTTP 200
with `image/webp`. Left/right source crops were visually checked for all four.
`atlas-preview.png` shows center and heart frames on the demo's background colors.

| Character | Measured shift at 140px | Shoulder width change | Palette match |
| --- | ---: | ---: | ---: |
| Nik | 0.00px | 2.0% | 87.8% |
| Thịnh | 0.00px | 1.3% | 86.5% |
| Nemo | 0.00px | 1.7% | 83.9% |
| Phương | 0.00px | 1.7% | 87.7% |

The page layout and Nik's pointer-facing rendering were observed in Chrome during
development. Browser control disconnected before the final click, keyboard, and
responsive interaction checks; these final browser checks remain unverified.
