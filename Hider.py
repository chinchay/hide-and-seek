import pygame
from Agent import Agent

class Hider(Agent):
    def __init__(self, filename, x, y, ID) -> None:
        super().__init__(filename, x, y, ID)
        rightFilename = "images/hider50a.png"
        leftFilename  = "images/hider50b.png"
        rightImg = pygame.image.load(rightFilename).convert()
        leftImg  = pygame.image.load(leftFilename).convert()
        self.isRightSide2Img = { True: rightImg, False: leftImg}
        pass
    
    def _GetDirection(self, event):
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
    #

    def ProcessEvent(self, event, allOthers):
        self.contactList = []
        direction = self._GetDirection(event)
        if direction != None:
            if self.CanIPush(allOthers, direction):
                self.Move(direction)



