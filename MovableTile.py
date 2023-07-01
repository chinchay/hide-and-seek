from Tile import Tile
from pygame import Rect
import numpy as np

class MovableTile(Tile):
    def __init__(self, filename, x, y, ID) -> None:
        super().__init__(filename, x, y, ID)
        self.canImove = True
        self.amIpushable = True

        self.canImoveTo = {
            "+x": True,
            "-x": True,
            "+y": True,
            "-y": True,
        }

        self._deltaR = {
            "+y" : np.asarray([  0,  10]),
            "-y" : np.asarray([  0, -10]),
            "+x" : np.asarray([ 10,   0]),
            "-x" : np.asarray([-10,   0]),
        }    

        self.listHit = []     
        pass

    def _GetFutureRect(self, direction):
        [dx, dy] = self._deltaR[direction]
        x = self.rect.x + dx
        y = self.rect.y + dy
        w = self.rect.w
        h = self.rect.h
        return Rect(x, y, w, h)

    def Move(self, direction):
        [dx, dy] = self._deltaR[direction]
        self.rect.x += dx
        self.rect.y += dy
        for tile in self.listHit: # tile has been checked it can be pushed
            tile.Move(direction)
        #
        pass

    def UpdateListHit(self, allOthers, direction):
        listHit = []
        futureRect = self._GetFutureRect(direction)
        for tile in allOthers:
            if self.ID != tile.ID:
                if futureRect.colliderect(tile):
                    listHit.append(tile)
        #
        self.listHit = listHit
        pass

    def GetFilterTiles(self, thisTile, allOthers):
        filteredTiles = []
        for tile in allOthers:
            if thisTile.ID != tile.ID:
                filteredTiles.append(tile)
        #
        return filteredTiles

    def CanIPush(self, allOthers, direction):
        # return super().CanIBePushed(allOthers, direction)

        self.UpdateListHit(allOthers, direction)
        for tile in self.listHit:
            filteredTiles = self.GetFilterTiles(tile, allOthers)
            if tile.amIpushable:
                if not tile.CanIPush(filteredTiles, direction):
                    return False
            else:
                return False
        #
        return True
