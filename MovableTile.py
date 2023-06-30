from Tile import Tile
import numpy as np

class MovableTile(Tile):
    def __init__(self, filename, x, y) -> None:
        super().__init__(filename, x, y)
        self.amImovable = True

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
        pass

    def _GetFutureRect(self, direction):
        pass

    def Move(self, direction):
        pass

    def TryToPush(self, allOthers, direction):
        pass

    def CanIBePushed(self, allOthers, direction):
        # return super().CanIBePushed(allOthers, direction)
        # TODO implement here!
        pass
