"""JPG"""

from PIL import Image

way = input(str("Input absolute way to file: "))
jpg_convert = ".jpg"


def jpg():
    try:
        with Image.open(way) as img:
            img.load()
        assert img.fp is None
        img.save(way[:-4] + jpg_convert)
        print('Completed successfully!')
    except:
        print('Problems with way to file or this file is in selected format.')


jpg()
