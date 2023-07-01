import pygame
from pygame.image import load
from MovableTile import MovableTile
from pygame.transform import rotate

class Agent(MovableTile):
    def __init__(self, filename, x, y, ID) -> None:
        super().__init__(filename, x, y, ID)
        self.amIpushable = False
        self.isWalking = False
        self.deg = 0

        self._isRightSide = False
        pass

    def LoadSides(self):
        rightImg = load(self.rightFilename).convert()
        leftImg  = load(self.leftFilename).convert()
        self.isRightSide2Img = { True: rightImg, False: leftImg}
        pass

    def __str__(self): # will overwrite inherited method!
        return "I am an agent. filename: " + self.filename
    
    def Draw(self, surface): # will overwrite inherited method!
        if self.isWalking:
            self._isRightSide = not self._isRightSide # defined in derived classes
        #
        img = self.isRightSide2Img[self._isRightSide] # see derived class
        img = rotate(img, self.deg)
        surface.blit(img, self.rect)
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
    #

    def ProcessEvent(self, event, allOthers):
        self.contactList = []
        direction = self.GetDirection(event)
        if direction != None:
            if self.CanIPush(allOthers, direction):
                self.Move(direction)


        