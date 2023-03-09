import io

from PIL import Image


def show_image(data):
    buffer = io.BytesIO(data)
    image = Image.open(buffer)
    image.show()
