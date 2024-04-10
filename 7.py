def z1():
    from PIL import Image

    image = Image.open("cat.png")
    image.show()
    print("Размер изображения:", image.size)
    print("Формат изображения:", image.format)
    print("Цветовая модель:", image.mode)

def z2():
    from PIL import Image

    orig = Image.open("cat.png")
    small = orig.reduce(3)
    small.save('small_cat.jpg')

    horizontal = orig.transpose(Image.FLIP_LEFT_RIGHT)
    vertical = orig.transpose(Image.FLIP_TOP_BOTTOM)
    horizontal.save('horizontal.jpg')
    vertical.save('vertical.jpg')

def z3():
    from pathlib import Path
    from PIL import Image, ImageFilter

    Path("filtered_images")
    for i in range(1, 6):
        original_image = Image.open(f'{i}.jpg')
        filtered_image = original_image.filter(ImageFilter.CONTOUR)
        filtered_image.save(f'filtered_images/filtered_{i}.jpg')


def z4():
    from PIL import Image, ImageDraw

    watermark = Image.open("watermark.png")
    position = (0, 0)
    for i in range(1, 6):
        original_image = Image.open(f'{i}.jpg')
        watermarked_image = original_image.copy()
        watermarked_image.paste(watermark, position, watermark)
        watermarked_image.save(f'watermarked_{i}.jpg')


z4()