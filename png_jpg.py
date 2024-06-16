"""PNG => JPG"""
# "E:/testimage/png-24-primer.png"
from PIL import Image

way = input(str("Input absolute way to PNG file: "))
jpg_convert = ".jpg"


def png_jpg():
    try:
        with Image.open(way) as img:
            img.load()
        assert img.fp is None
        img.save(way[:-4] + jpg_convert)
        print('Completed successfully!')
    except:
        print('Problems with way to file')


png_jpg()
