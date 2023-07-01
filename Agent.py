import pygame
from pygame.image import load
from MovableTile import MovableTile
from pygame.transform import rotate
from time import sleep

class Agent(MovableTile):
    def __init__(self, filename, x, y, ID, movesFileName) -> None:
        super().__init__(filename, x, y, ID)
        self.amIpushable = False
        self.isWalking = False
        self.deg = 0

        self._isRightSide = False
        
        self.movesFileName = movesFileName
        self.listMove = []
        self.listFakeMove = []
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
        # derived class will implement it
        pass

    def ProcessEvent(self, event, allOthers):
        self.contactList = []
        direction = self.GetDirection(event)
        if direction != None:
            if self.CanIPush(allOthers, direction):
                self.Move(direction)
                self.listMove.append(direction)
    #

    def SaveMoves(self):
        f = open(self.movesFileName, "w")
        for direction in self.listMove:
            f.write(direction + "\n")
        #
        f.close()
        pass

    def LoadMovesFromFile(self):
        try:
            f = open(self.movesFileName, "r")
            listLine = f.readlines()
            f.close()
            for line in listLine:
                self.listFakeMove.append(line.strip())
            #
        except:
            print("_Error loading file.")
            pass
    #

