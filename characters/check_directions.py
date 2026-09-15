"""Create a left/right contact sheet for visual direction verification."""
import sys
from pathlib import Path
from PIL import Image

for name in sys.argv[1:]:
    directory = Path('characters') / name
    source = Image.open(directory / 'directions.png')
    tile = source.width // 3
    contact = Image.new('RGBA', (tile * 2, tile))
    contact.paste(source.crop((0, tile, tile, 2 * tile)), (0, 0))
    contact.paste(source.crop((2 * tile, tile, 3 * tile, 2 * tile)), (tile, 0))
    contact.save(directory / 'left-right-check.png')
