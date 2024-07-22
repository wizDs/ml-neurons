import io
import base64
import os
import httpx
from PIL import Image
from typing import NamedTuple, Union


class GenericMessage(NamedTuple):
    role: str
    content: list[Union[str, dict]]


def local_image_to_base64(path: str) -> str:
    im = Image.open(path, mode='r')
    buf = io.BytesIO()
    im.save(buf, format='PNG')
    byte_im = buf.getvalue()
    base64_im = base64.b64encode(byte_im).decode("utf-8")
    return base64_im


def url_image_to_base64(image_url: str) -> str:
    base64_im = base64.b64encode(httpx.get(image_url).content).decode("utf-8")
    return base64_im

def image_to_base64(path: str) -> str:
    try:
        if path.startswith("http"):
            return url_image_to_base64(path)
        
        if os.path.isfile(path):
            return local_image_to_base64(path)
    
    except:
        raise FileNotFoundError(f"could not be found: {path}")

def image_message(image_name: str) -> GenericMessage:
    return GenericMessage(
        role = 'user',
        content = [{"type": "image_url", 
                    "image_url": {"url": "data:image/jpeg;base64,{"+ image_name + "}"},}]
    )

