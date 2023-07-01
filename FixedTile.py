from Tile import Tile

class FixedTile(Tile):
    def __init__(self, filename, x, y, ID) -> None:
        super().__init__(filename, x, y, ID)
        self.canImove = False
        self.amIpushable = False
        pass

    def CanIBePushed(self, allOthers, direction):
        # return super().CanIBePushed(allOthers, direction)
        return False
    
    

