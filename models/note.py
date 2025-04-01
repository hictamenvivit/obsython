from yaml import load, Loader
from typing import cast


class Note:

    @staticmethod
    def parse_metadata(raw: str) -> dict[str, str | int]:
        if raw.startswith("---"):
            to_parse = raw.split("---", 1)[1].split("---", 1)[0]
            return cast(
                dict[str, str | int],
                load(to_parse, Loader=Loader),
            )
        return {}

    def __init__(self, path: str, content: str) -> None:
        self.path = path
        self.content = content
        self.meta = self.parse_metadata(content)
