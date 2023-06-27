import pygame
import sys
from tiles import TileMap

pygame.init()




tileMap = TileMap()
width, height = tileMap.GetMapSize()

# width  = 800
# height = 600
canvas = pygame.Surface((width, height))
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hide and Seek")

# Set the colors
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)


# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# tile_w = 20
# tile_h = 20
# sprite = pygame.Surface((tile_w, tile_h))
# sprite.set_colorkey((0,0,0))
# self.sprite_sheet = pygame.image.load(filename).convert()
# sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))

# spritesheet = 


# tileMap = TileMap()
# width, height = tileMap.GetMapSize()
tileMap.initialize()


x = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        running = ( event.type != pygame.QUIT )
    #

    # # Clear the screen
    # screen.fill((0, 0, 0))
    # # screen.fill(WHITE)

    # # Render graphics (draw a rectangle)
    # pygame.draw.rect(screen, (255, 0, 0), (300, 200, 200, 100))

    # filename = "images/pacman.png"
    # img = pygame.image.load(filename)
    # # pygame.display.set_icon(img)
    # screen.blit(img, (x, 100))
    # x += 1

    # # Update the entire display
    # pygame.display.flip()

    # Set the frame rate
    clock.tick(60)


    canvas.fill((0, 180, 240))

    tileMap.drawSurface(canvas)

    screen.blit(canvas, (0, 0))
    pygame.display.update()

#


# Quit the game
pygame.quit()
sys.exit()
