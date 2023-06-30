from Tile import Tile

class FixedTile(Tile):
    def __init__(self, filename, x, y) -> None:
        super().__init__(filename, x, y)
        self.amImovable = False
        pass

    def CanIBePushed(self, allOthers, direction):
        # return super().CanIBePushed(allOthers, direction)
        return False
    
    

