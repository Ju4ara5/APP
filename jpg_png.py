"""JPG => PNG"""
# "E:/testimage/jpg_44-2.jpg.png"
from PIL import Image

way = input(str("Input absolute way to JPG file: "))
png_convert = ".png"


def jpg_png():
    try:
        with Image.open(way) as img:
            img.load()
        assert img.fp is None
        img.save(way[:-4] + png_convert)
        print('Completed successfully!')
    except:
        print('Problems with way to file')


jpg_png()
