from typing import NamedTuple, Union


class GenericMessage(NamedTuple):
    role: str
    content: list[Union[str, dict]]

def image_message(image_name: str) -> GenericMessage:
    return GenericMessage(
        role = 'user',
        content = [{"type": "image_url", 
                    "image_url": {"url": "data:image/jpeg;base64,{"+ image_name + "}"},}]
    )

