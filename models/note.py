from yaml import load, Loader


class Note:

    @staticmethod
    def parse_metadata(raw):
        if raw.startswith("---"):
            to_parse = raw.split("---", 1)[1].split("---", 1)[0]
            return load(to_parse, Loader=Loader)
        return {}

    def __init__(self, path, content):
        self.path = path
        self.content = content
        self.meta = self.parse_metadata(content)
