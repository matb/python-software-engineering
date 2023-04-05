import logging
from typing import Any
import xml.etree.ElementTree


class XMLAdapter:
    def __init__(self, tree: xml.etree.ElementTree) -> None:
        self.xml = tree

    def get(self, key: str, default: Any = None) -> Any | None:

        root = self.xml.getroot()
        try:
            value = root.find(key).text
        except NameError:
            logging.warning(f"Could not find {key} in config- return default")
            value = default
        return value

