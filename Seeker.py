from Agent import Agent
import pygame

class Seeker(Agent):
    def __init__(self, filename, x, y, ID, movesFileName) -> None:
        super().__init__(filename, x, y, ID, movesFileName)
        self.rightFilename = "images/hider50a.png"
        self.leftFilename  = "images/hider50b.png"
        pass

    def GetDirection(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_DOWN:
                    self.isWalking = True
                    self.deg = 180
                    return "+y"
                case pygame.K_UP:
                    self.isWalking = True
                    self.deg = 0
                    return "-y"
                case pygame.K_LEFT:
                    self.isWalking = True
                    self.deg = 90
                    return "-x"
                case pygame.K_RIGHT:
                    self.isWalking = True
                    self.deg = -90
                    return "+x"
        #
        self.isWalking = False
        return None


        

    