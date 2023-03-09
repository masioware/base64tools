from clipboard import copy, paste

from utils.b64 import decode_b64, encode_b64
from utils.image import show_image


def encode(file=None):
    file = file or paste()

    with open(file, "rb") as file:
        content = file.read()

    base64 = encode_b64(content)
    copy(base64)

    return base64


def decode(base64=None, image=True, output=None):
    content = base64 or paste()
    result = decode_b64(content)

    if image:
        show_image(result)

    if output:
        with open(output, "wb") as file:
            file.write(result)

    return result
