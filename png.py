"""PNG"""

from PIL import Image

way = input(str("Input absolute way to file: "))
png_convert = ".png"


def png():
    try:
        with Image.open(way) as img:
            img.load()
        assert img.fp is None
        img.save(way[:-4] + png_convert)
        print('Completed successfully!')
    except:
        print('Problems with way to file or this file is in selected format.')


png()
