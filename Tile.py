import pygame
from pygame import Rect
import numpy as np

class Tile(pygame.sprite.Sprite):
    def __init__(self, filename, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)

        width = 50
        height = 50
        self.filename = filename
        
        img = pygame.image.load(filename).convert()
        self.imgSprite = pygame.Surface( (width, height) )
        self.imgSprite.set_colorkey( (0, 0, 0) )
        self.imgSprite.blit( img, (0, 0), (0, 0, width, height) )

        self.rect = self.imgSprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        pass

    def draw(self, surface):
        surface.blit( self.imgSprite, (self.rect.x, self.rect.y) )
        pass

    def __str__(self):
        return "This is a tile object. filename: " + self.filename
    
    def CanIBePushed(self, allOthers, direction):
        pass
#
