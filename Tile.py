import pygame
import numpy as np
import math

class Tile(pygame.surface.Surface):
    def __init__(self, filename, x, y, ID) -> None:
        self.width  = 50
        self.height = 50
        pygame.surface.Surface.__init__(self, (self.width, self.height))

        self.ID = ID
        self.filename = filename
        self.x = x
        self.y = y
        
        self.surf = pygame.Surface( (self.width, self.height) )
        self.surf.set_colorkey( (0, 0, 0) )
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.canIdrawMyself = False
        
        # self.surf.blit( img, (0, 0), (0, 0, self.width, self.height) )
        pass

    def _GetCanIdrawMyself(self, player, allOthers):
        filteredTiles = self.GetFilterTiles(allOthers)
        for anotherTile in filteredTiles:
            if self._IsAnotherTileInTheWay(player, anotherTile):
                return False
        #
        return True

    def _DrawMyself(self, surface):
        img = pygame.image.load(self.filename).convert()
        surface.blit( img, self.rect )
        pass
        
    def Draw(self, surface, player=None, allOthers=None, event=None):
        # surface.blit( self.surf, (self.rect.x, self.rect.y) )
        # pass
        if player is None:
            self._DrawMyself(surface)
        else:
            if event.type == pygame.KEYDOWN:
                self.canIdrawMyself = self._GetCanIdrawMyself(player, allOthers)
                if self.canIdrawMyself:
                    self._DrawMyself(surface)
                else:
                    # img = pygame.image.load("images/movableBlock.png").convert()
                    # surface.blit( img, self.rect )
                    # img = pygame.image.load(self.filename).convert()
                    # surface.blit( img, self.rect )
                    pass
            else:
                if self.canIdrawMyself:
                    self._DrawMyself(surface)
            #
        #

    def __str__(self):
        return "This is a tile object. filename: " + self.filename
    
    def CanIBePushed(self, allOthers, direction):
        pass
    
    def GetFilterTiles(self, allOthers):
        filteredTiles = []
        for tile in allOthers:
            if self.ID != tile.ID:
                filteredTiles.append(tile)
        #
        return filteredTiles

    def _IsAnotherTileInTheWay(self, player, anotherTile):
        width = 50
        height = 50

        xo = player.rect.x
        yo = player.rect.y
        # redefine for player's center:
        xo += (width / 2)
        yo += (height / 2)

        xh = anotherTile.rect.x
        yh = anotherTile.rect.y
        # redefine for anotherTile's center:
        # xh += (width / 2)
        # yh += (height / 2)
        
        xf_ = self.rect.x
        yf_ = self.rect.y
        # redefine for self's center:
        # xf += (width / 2)
        # yf += (height / 2)

        targetVertices = [ [xf_, yf_] ]

        for (xf, yf) in targetVertices:
            vTarget     = np.asarray([xf - xo, yf - yo])
            vHalfWay    = np.asarray([xh - xo, yh - yo])
            normTarget  = np.linalg.norm(vTarget)
            normHalfway = np.linalg.norm(vHalfWay)

            uTarget  = vTarget  / normTarget
            uHalfway = vHalfWay / normHalfway
            

            # halfwayTile shadow
            pA = np.asarray([xh         - xo, yh          - yo])
            pB = np.asarray([xh + width - xo, yh          - yo])
            pC = np.asarray([xh         - xo, yh + height - yo])
            pD = np.asarray([xh + width - xo, yh + height - yo])

            per = np.asarray([-uHalfway[1], uHalfway[0]])


            # proyection onto per (per is already is unitary)
            s0 = abs( np.dot(pA - pB, per) )
            s1 = abs( np.dot(pA - pC, per) )
            s2 = abs( np.dot(pA - pD, per) )
            s3 = abs( np.dot(pB - pC, per) )
            s4 = abs( np.dot(pB - pD, per) )
            s5 = abs( np.dot(pC - pD, per) )

            listProjections = np.asarray([s0, s1, s2, s3, s4, s5])

            maxIndx  = listProjections.argmax()

            dic = {
                0 : [pA, pB],
                1 : [pA, pC],
                2 : [pA, pD],
                3 : [pB, pC],
                4 : [pB, pD],
                5 : [pC, pD],
            }

            [v1, v2] = dic[maxIndx]
            
            u1 = v1 / np.linalg.norm(v1)
            u2 = v2 / np.linalg.norm(v2)

            if (
                (uTarget[0] == u1[0]) and (uTarget[1] == u1[1])
                or
                (uTarget[0] == u2[0]) and (uTarget[1] == u2[1])
                ):
                return False
            # 

            d1 = np.dot(u1 - uTarget, per)
            d2 = np.dot(u2 - uTarget, per)

            if np.dot((u1 + u2), uTarget) > 0:  # make sure all of them point the same upper side (same "direction")     
                if d1 * d2 <= 0: # see if projections are opposites
                    if normHalfway < normTarget: # verify that halfway is in the middle between player and target
                        return True
        #
        # print("hi")
        return False


#
