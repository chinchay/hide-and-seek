import pygame
from Agent import Agent

class Hider(Agent):
    def __init__(self, filename, x, y, ID) -> None:
        super().__init__(filename, x, y, ID)
        self.rightFilename = "images/hider50a.png"
        self.leftFilename  = "images/hider50b.png"
        pass



