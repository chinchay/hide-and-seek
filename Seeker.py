from Agent import Agent

class Seeker(Agent):
    def __init__(self, filename, x, y, ID, movesFileName) -> None:
        super().__init__(filename, x, y, ID, movesFileName)
        self.rightFilename = "images/hider50a.png"
        self.leftFilename  = "images/hider50b.png"
        pass

        

    