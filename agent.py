import pygame

class AgentSide(pygame.surface.Surface):
    def __init__(self, filename) -> None:
        self._size = 50
        pygame.surface.Surface.__init__(self, (self._size, self._size))
        
        self.filename = filename
        self._img = pygame.image.load(self.filename).convert()

        self.set_colorkey( (0, 0, 0) )
        self.blit( self._img, (0, 0), (0, 0, self._size, self._size) )
        self.agentRect = self.get_rect()
        self.agentRect.x = 0
        self.agentRect.y = 0
        pass

    def Rotate(self, deg):
        self._img = pygame.image.load(self.filename).convert()
        self._img = pygame.transform.rotate(self._img, deg)
        self.blit( self._img, (0, 0), (0, 0, self._size, self._size) )
    #
#

class Agent:
    def __init__(self) -> None:
        rightFile = "images/hider50a.png"
        leftFile  = "images/hider50b.png"
        self._agentRight = AgentSide(rightFile)
        self._agentLeft  = AgentSide(leftFile)
        self._isRight = False
        self._agentDict = { True: self._agentRight, False: self._agentLeft}
        pass

    def GetSide(self, event):
        if event.type == pygame.KEYDOWN:
            self._isRight = not self._isRight
        #

        return self._agentDict[ self._isRight ]
    #
    
    def GetRect(self):
        return self._agentRight.agentRect
    
    def AddToX(self, dx):
        self._agentRight.agentRect.x += dx
        self._agentLeft.agentRect.x  += dx
        pass

    def AddToY(self, dy):
        self._agentRight.agentRect.y += dy
        self._agentLeft.agentRect.y  += dy
        pass

    def ProcessEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self._agentRight.Rotate(180)
            self._agentLeft.Rotate(180)
            self.AddToY(10)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self._agentRight.Rotate(0)
            self._agentLeft.Rotate(0)
            self.AddToY(-10)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self._agentRight.Rotate(90)
            self._agentLeft.Rotate(90)
            self.AddToX(-10)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self._agentRight.Rotate(-90)
            self._agentLeft.Rotate(-90)
            self.AddToX(10)

