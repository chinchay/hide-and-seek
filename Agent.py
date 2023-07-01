from MovableTile import MovableTile
from pygame.transform import rotate

class Agent(MovableTile):
    def __init__(self, filename, x, y, ID) -> None:
        super().__init__(filename, x, y, ID)
        self.amIpushable = False
        self._isRightSide = False
        self.isWalking = False
        self.deg = 0
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

        