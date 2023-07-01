import pygame
import sys
from Scenario import Scenario
from Cube import Cube
from Ramp import Ramp
from Hider import Hider
from Seeker import Seeker


pygame.init()


scenario = Scenario()
width, height = scenario.GetMapSize()


canvas = pygame.Surface((width, height))
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hide and Seek")

WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)


scenario.initialize()
listFixedTile = scenario.tiles
count  = scenario.GetCount()
print("count: ", count)

hider = Hider(filename="", x=0, y=0, ID=count)
hider.LoadSides()

count += 1
seeker = Seeker(filename="", x=700, y=0, ID=count)
seeker.LoadSides()

count += 1
cube1 = Cube( filename="images/movableBlock.png", x=200, y=200, ID=count)
count += 1
cube2 = Cube( filename="images/movableBlock.png", x=200, y=300, ID=count)
count += 1
cube3 = Cube( filename="images/movableBlock.png", x=500, y=200, ID=count)


listMovableTile = [cube1, cube2, cube3]
allOthers = listFixedTile + listMovableTile + [seeker]

# Create a clock object to control the frame rate
clock = pygame.time.Clock()


# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        running = ( event.type != pygame.QUIT )
    #
    
    # Set the frame rate
    clock.tick(10)

    canvas.fill((0, 180, 240))
    scenario.Draw(canvas)

    hider.ProcessEvent(event, allOthers)
    hider.Draw(canvas)

    seeker.Draw(canvas)
    
    for movable in listMovableTile:
        movable.Draw(canvas)
    #
    
    screen.blit(canvas, (0, 0))
    pygame.display.update()

#

# Quit the game
pygame.quit()
sys.exit()
