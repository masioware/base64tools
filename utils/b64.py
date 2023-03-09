from base64 import b64decode, b64encode


def encode_b64(content):
    return b64encode(content).decode()


def decode_b64(content):
    return b64decode(content)
