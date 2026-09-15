# Nolan cursor buddy

Created from the supplied nolan.png photo with the built-in image_gen tool. Generation prompts are in prompts.md; original generated artwork and normalized transparent PNG sources are retained here.

## Rebuild

```powershell
python characters/normalize_rows.py characters/nolan/directions-generated.png characters/nolan/directions.png 410 810 560
python characters/normalize_rows.py characters/nolan/reactions-generated.png characters/nolan/reactions.png 430 830 560 440 850
python .agents/skills/cursor-buddy/scripts/mascot.py nolan --skip-generate
python characters/check_directions.py nolan
```

Served files: public/mascots/nolan-directions.webp and public/mascots/nolan-reactions.webp.

## Validation

- Both sheets have real alpha, with no edge contact. Directions shoulder spread: 2.3%.
- Atlas swap shift: 0.00px at 140px; shoulder width change: 1.9%; palette match: 87.3%.
- Visually inspected left/right orientation and all nine reaction icons for clipping.
- Both served URLs returned HTTP 200 with image/webp.
- Build and lint passed; production build rerun after atlas creation.
- Browser checks passed for pointer-facing direction, click, Tab/Enter, Space, and 390px mobile layout.
- Reduced-motion behavior was reviewed in the existing component but not exercised in the browser.
