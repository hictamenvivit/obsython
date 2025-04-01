from models.note import Note
from utils import load_text

NOTE = Note(
    "path",
    """---
 foo: bar   
 ---
""",
)
NOTE2 = Note(
    "path",
    load_text("tests/res/Taper l'atelier Keylight.md"),
)


def test_note() -> None:
    assert NOTE.meta["foo"] == "bar"
    assert NOTE2.meta["type"] == "atHome"
