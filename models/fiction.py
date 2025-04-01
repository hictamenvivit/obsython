"""
A fiction (novel or scenario) based on a canvas
"""

from pathlib import Path
import json


class Node:

    def __init__(self, content: dict[str, str | int]) -> None:
        self.content = content


class Fiction:

    def __init__(self, path: str) -> None:
        self.path = path
        with open(self.path) as f:
            self.nodes = [Node(x) for x in json.load(f)["nodes"]]
