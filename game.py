import pygame
import sys
from tiles import TileMap, Tile
from agent import Agent

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

hider = Agent()



# filenameMovableBlock = "images/movableBlock.png"
# img = pygame.image.load(filenameMovableBlock).convert()
# mov1 = pygame.Surface( (50,50) )
# mov1.set_colorkey( (0, 0, 0) )

# mov1.blit(img, (0, 0), (0, 0, 50, 50))
# mov1Rect = mov1.get_rect()
# mov1Rect.x, mov1Rect.y = 0, 250

# # mov1.blit(img, (0, 0), (0, 0, 50, 50))
# # mov1Rect = mov1.get_rect()
# # mov1Rect.x, mov1Rect.y = 200, 200

filename = "images/movableBlock.png"
mov1 = Tile(tilefile=filename, x=200, y=200)
listMovable = [mov1]



listTile = tileMap.tiles





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
    clock.tick(10)


    canvas.fill((0, 180, 240))

    tileMap.drawSurface(canvas)



    hider.ProcessEvent(event, listTile, listMovable)
    
    

    hiderSide = hider.GetSide(event)
    hiderRect = hiderSide.GetRect()
    canvas.blit( hiderSide,  hiderRect)

    # rotated_player = pygame.transform.rotate(hiderSide, 45)
    # canvas.blit( rotated_player,  hiderRect)

    # canvas.blit(mov1, mov1Rect)

    
    for movable in listMovable:
        movable.draw(canvas)
    #    


    # listTileCollide = []
    # for tile in listTile:
    #     if hiderARect.colliderect(tile) or hiderBRect.colliderect(tile):
    #         listTileCollide.append(tile)
    # #
    # for tile in listTileCollide:
    #     if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
    #         hiderARect.x = tile.rect.left - hiderARect.w
    #         hiderBRect.x = tile.rect.left - hiderBRect.w
    #         # hiderARect.x  -= 10
    #         # hiderBRect.x  -= 10



    screen.blit(canvas, (0, 0))
    pygame.display.update()

#


# Quit the game
pygame.quit()
sys.exit()
