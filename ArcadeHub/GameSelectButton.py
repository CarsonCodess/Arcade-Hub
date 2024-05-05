from typing import Tuple

from Button import Button


class GameSelectButton(Button):
    fPath: str

    def __init__(self, text: str, position: Tuple[int, int], fontSize: int, path):
        super().__init__(text, position, fontSize)
        self.fPath = path

    def getFilePath(self):
        return self.fPath
