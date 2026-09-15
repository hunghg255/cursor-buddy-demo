"""Contact sheet for inspecting built sprites on the actual demo colors."""
from PIL import Image, ImageDraw

names = ['nik', 'thinh', 'nemo', 'phuong']
colors = ['#e9e6fa', '#e5eedf', '#e2ecf7', '#f8e6dc']
preview = Image.new('RGB', (1000, 550), '#faf9f6')
draw = ImageDraw.Draw(preview)
for column, (name, color) in enumerate(zip(names, colors)):
    for row, (kind, index) in enumerate([('directions', 4), ('reactions', 1)]):
        atlas = Image.open(f'public/mascots/{name}-{kind}.webp').convert('RGBA')
        size = atlas.width // 3
        x, y = index % 3 * size, index // 3 * size
        sprite = atlas.crop((x, y, x + size, y + size)).resize((220, 220), Image.Resampling.LANCZOS)
        card = Image.new('RGBA', (220, 220), color)
        card.alpha_composite(sprite)
        preview.paste(card.convert('RGB'), (column * 250 + 15, row * 275 + 15))
        draw.text((column * 250 + 20, row * 275 + 242), f'{name} / {kind}', fill='#252625')
preview.save('characters/atlas-preview.png')
