def load_text(path: str) -> str:
    with open(path) as file:
        return file.read()
