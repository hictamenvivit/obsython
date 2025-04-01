"""
A fiction (novel or scenario) based on a canvas
"""

from pathlib import Path
import json
import os


class Node:

    def __init__(self, vault_root: str, content: dict[str, str | int]) -> None:
        self.content = content
        self.vault_root = vault_root
        self.path = Path(vault_root) / self.content["file"]

    def read_text(self):
        return self.path.read_text()

    @property
    def x(self):
        return self.content["x"]

    @property
    def y(self):
        return self.content["y"]


class Fiction:

    def __init__(self, vault_root: str, path: str) -> None:
        self.path = os.path.join(vault_root, path)
        self.vault_root = vault_root
        with open(self.path) as f:
            self.nodes = sorted(
                [
                    Node(
                        vault_root=vault_root,
                        content=x,
                    )
                    for x in json.load(f)["nodes"]
                ],
                key=lambda node: (node.y, node.x),
            )
