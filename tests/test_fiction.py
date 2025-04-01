from models.fiction import Fiction


class TestFiction:

    def test_init(self) -> None:
        fiction = Fiction(
            "tests/res",
            "lebug.canvas",
        )
        assert fiction.path == "tests/res/lebug.canvas"
        assert len(fiction.nodes) == 4
        assert "Younes" in fiction.nodes[0].read_text()
