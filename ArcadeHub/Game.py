class Game:
    def __init__(self, filePath):
        self.path = filePath
    def startGame(self):
        raise NotImplementedError("Subclasses must override the startGame() method.")