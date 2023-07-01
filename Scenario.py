import pygame
from FixedTile import FixedTile

char2file = {
    # "-" : "images/tile.jpg",
    "?" : "images/tile.jpg",
    "#" : "images/brick.png",
    "=" : "images/brick.png",
}

class Scenario:
    def __init__(self) -> None:
        self.tileW = 50
        self.tileH = 50

        self.filename = "sample.txt"
        self.width, self.height = self.GetMapSize()
        self.count = None
        pass

    def initialize(self):
        self.width  = None
        self.height = None
        # self.width  = 300
        # self.height = 300
        filename = "sample.txt"
        self.tiles = self.LoadTiles(filename) # will update width and height
        self.count = len(self.tiles)
        print(self.tiles[0])

        self.surface = pygame.Surface((self.width, self.height))
        # self.surface.set_colorkey((0, 0, 200))
        
        print(self.width, self.height)

        # self.surface = pygame.Surface((300, 300))
        # self.surface.fill((200, 180, 0)) 

        for tile in self.tiles:
            tile.Draw( self.surface )
        #
    #

    def GetMapSize(self):
        f = open(self.filename, "r")
        listLine = f.readlines()
        f.close()
        tileSize = self.tileW
        width  = tileSize * (len(listLine[0]) - 1)
        height = tileSize * len(listLine)
        return [width, height]

    def Draw(self, surface):
        surface.blit( self.surface, (0, 0) )
        pass

    def LoadTiles(self, filename):
        f = open(filename, "r")
        listLine = f.readlines()
        f.close()
        listTile = []
        tileSize = self.tileW
        x = 0
        y = 0
        count = 0
        for line in listLine:
            for char in line.strip():
                if char != "-":
                    filename = char2file[char]
                    tile = FixedTile(filename, x, y, count)
                    count += 1
                    listTile.append(tile)
                #
                x += tileSize
            #
            x = 0
            y += tileSize
        #
        self.width  = tileSize * (len(listLine[0]) - 1)
        self.height = tileSize * len(listLine)
        return listTile
    
    def GetCount(self):
        return self.count

