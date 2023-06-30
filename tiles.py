import pygame
# from pygame.sprite import _Group

char2file = {
    # "-" : "images/tile.jpg",
    "?" : "images/tile.jpg",
    "#" : "images/brick.png",
    "=" : "images/brick.png",
}

# class Tile(pygame.sprite.Sprite):
#     # def __init__(self, *groups: _Group) -> None:
#     # super().__init__(*groups)

#     def __int__(self, image, x, y):    
#         pass


# #

class Tile(pygame.sprite.Sprite):
    def __init__(self, tilefile, x, y) -> None:
        self.tileW= 50
        self.tileH = 50

        self.tilefile = tilefile
        pygame.sprite.Sprite.__init__(self)
        
        
        img = pygame.image.load(tilefile).convert()
        
        self.imgSprite = pygame.Surface( (self.tileW, self.tileH) )
        self.imgSprite.set_colorkey( (0, 0, 0) )
        self.imgSprite.blit(img, (0, 0), (0, 0, self.tileW, self.tileH))

        self.rect = self.imgSprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        pass

    def draw(self, surface):
        surface.blit( self.imgSprite, (self.rect.x, self.rect.y) )
        pass

    def __str__(self):
        return "this is a tile object. tilefile: " + self.tilefile
#


class TileMap():
    def __init__(self) -> None:
        self.tileW= 50
        self.tileH = 50

        self.filename = "sample.txt"
        self.width, self.height = self.GetMapSize()
        pass

    def initialize(self):
        self.width  = None
        self.height = None
        # self.width  = 300
        # self.height = 300
        filename = "sample.txt"
        self.tiles = self.LoadTiles(filename) # will update width and height
        print(self.tiles[0])

        self.surface = pygame.Surface((self.width, self.height))
        # self.surface.set_colorkey((0, 0, 200))
        
        print(self.width, self.height)

        # self.surface = pygame.Surface((300, 300))
        # self.surface.fill((200, 180, 0)) 


        for tile in self.tiles:
            tile.draw( self.surface )
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

    def drawSurface(self, surface):
        # surface.blit( self.surface, (0, 0) )

        # s = pygame.Surface((300, 300))
        # s.fill((200, 180, 0)) 
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
        for line in listLine:
            for char in line.strip():
                if char != "-":
                    tilefile = char2file[char]
                    # print(tilefile)
                    tile = Tile(tilefile, x, y)
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

