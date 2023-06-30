import pygame
from pygame import Rect
# from typing import List
from tiles import Tile
import numpy as np

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

    def GetRect(self):
        return self.agentRect

#

class Agent:
    def __init__(self) -> None:
        # rightFile = "images/hider50a.png"
        # leftFile  = "images/hider50b.png"

        rightFile = "images/tile.jpg"
        leftFile  = "images/tile.jpg"

        self._agentRight = AgentSide(rightFile)
        self._agentLeft  = AgentSide(leftFile)
        self._isRight = False
        self._agentDict = { True: self._agentRight, False: self._agentLeft}
        self._addDirection = {
            "+y" : np.asarray([  0,  10]),
            "-y" : np.asarray([  0, -10]),
            "+x" : np.asarray([ 10,   0]),
            "-x" : np.asarray([-10,   0]),
        }
        pass

    def GetSide(self, event) -> AgentSide:
        if event.type == pygame.KEYDOWN:
            self._isRight = not self._isRight
        #
        return self._agentDict[ self._isRight ]
        
    def AddToX(self, dx):
        self._agentRight.agentRect.x += dx
        self._agentLeft.agentRect.x  += dx
        pass

    def AddToY(self, dy):
        self._agentRight.agentRect.y += dy
        self._agentLeft.agentRect.y  += dy
        pass

    def WillCollide(self, listTile, direction):
        W = self._agentRight.agentRect.w
        H = self._agentRight.agentRect.h
        rightX0 = self._agentRight.agentRect.x
        rightY0 = self._agentRight.agentRect.y
        
        [left, top] = [rightX0, rightY0] + self._addDirection[direction]
        rect = Rect(left, top, W, H)
        for tile in listTile:
            if rect.colliderect(tile):
                # print( "will collide: ", top + H, tile.rect.y )
                return [True, tile]
        #
        return [False, None]


    def ProcessEvent(self, event, listTile, listMovable):
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self._agentRight.Rotate(180)
            self._agentLeft.Rotate(180)

            isAbleToMove = not self.WillCollide(listTile, "+y")[0]

            _, movable = self.WillCollide(listMovable, "+y")
            if movable != None:
                if isAbleToMove:
                    movable.rect.y += 10
            #

            if isAbleToMove:
                self.AddToY(10)
            #

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self._agentRight.Rotate(0)
            self._agentLeft.Rotate(0)

            isAbleToMove = not self.WillCollide(listTile, "-y")[0]

            _, movable = self.WillCollide(listMovable, "-y")
            if movable != None:
                if isAbleToMove:
                    movable.rect.y -= 10
            #

            if isAbleToMove:
                self.AddToY(-10)
            #

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self._agentRight.Rotate(90)
            self._agentLeft.Rotate(90)

            isAbleToMove = not self.WillCollide(listTile, "-x")[0]

            _, movable = self.WillCollide(listMovable, "-x")
            if movable != None:
                if isAbleToMove:
                    movable.rect.x -= 10
            #

            if isAbleToMove:
                self.AddToX(-10)
            #

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self._agentRight.Rotate(-90)
            self._agentLeft.Rotate(-90)

            isAbleToMove = not self.WillCollide(listTile, "+x")[0]

            _, movable = self.WillCollide(listMovable, "+x")
            if movable != None:
                if isAbleToMove:
                    movable.rect.x += 10
            #

            if isAbleToMove:
                self.AddToX(10)
            #

        #
    #
    
    def GetListHits(self, listTile, event):
        listTileCollide = []
        for tile in listTile:
            if self.GetSide(event).GetRect().colliderect(tile):
                listTileCollide.append(tile)
        #
        return listTileCollide
    
    def IsColliding(self, listTile, event):
        for tile in listTile:
            if self._agentRight.GetRect().colliderect(tile) or self._agentLeft.GetRect().colliderect(tile):
                return [True, tile]
        #
        return [False, None]
    #
