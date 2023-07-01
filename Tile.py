import pygame

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
        
        # self.surf.blit( img, (0, 0), (0, 0, self.width, self.height) )
        pass

    def Draw(self, surface):
        # surface.blit( self.surf, (self.rect.x, self.rect.y) )
        # pass

        img = pygame.image.load(self.filename).convert()
        surface.blit( img, self.rect )
        pass

    def __str__(self):
        return "This is a tile object. filename: " + self.filename
    
    def CanIBePushed(self, allOthers, direction):
        pass
#
