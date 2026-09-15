"""Repack uneven source rows into equal atlas cells without changing the artwork.

Usage: python characters/normalize_rows.py INPUT OUTPUT ROW_END_1 ROW_END_2
Row boundaries are selected from the empty gaps visible in the source sheet.
"""
import sys
from PIL import Image

source = Image.open(sys.argv[1]).convert('RGBA')
width = source.width // 3
edges = [0, int(sys.argv[3]), int(sys.argv[4]), source.height]
tile = int(sys.argv[5]) if len(sys.argv) > 5 else max(width, max(b - a for a, b in zip(edges, edges[1:]))) + 100
output = Image.new('RGBA', (tile * 3, tile * 3))
columns = [0, int(sys.argv[6]), int(sys.argv[7]), source.width] if len(sys.argv) > 7 else [0, width, width * 2, source.width]
for row in range(3):
    for col in range(3):
        cell = source.crop((columns[col], edges[row], columns[col + 1], edges[row + 1]))
        box = cell.getbbox()
        if box:
            # Keep original pixels, align bottom edges, leave ample padding.
            output.paste(cell, (col * tile + (tile - cell.width) // 2, row * tile + tile - 50 - box[3]))
output.save(sys.argv[2])
