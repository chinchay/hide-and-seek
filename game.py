import pygame
import sys
from Scenario import Scenario
from Cube import Cube
from Ramp import Ramp
from Hider import Hider
from Seeker import Seeker
import copy

option = input("Choose option:\n  1. Hider\n  2. Seeker\nOption: ")
# option = "1"

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

hider = Hider(filename="", x=0, y=0, ID=count, movesFileName="hider.txt")
hider.LoadSides()
hider.LoadMovesFromFile()


count += 1
seeker = Seeker(filename="", x=700, y=0, ID=count, movesFileName="seeker.txt")
seeker.LoadSides()
seeker.LoadMovesFromFile()

count += 1
cube1 = Cube( filename="images/movableBlock.png", x=200, y=200, ID=count)
count += 1
cube2 = Cube( filename="images/movableBlock.png", x=200, y=300, ID=count)
# count += 1
# cube3 = Cube( filename="images/movableBlock.png", x=500, y=200, ID=count)

if option == "1":
    one     = hider
    partner = seeker
else:
    one     = seeker
    partner = hider
#

oneFakeMoves = one.listFakeMove.copy()


# listMovableTile = [cube1, cube2, cube3]
listMovableTile = [cube1, cube2]
allOthers = listFixedTile + listMovableTile + [partner]

# allOthers = listFixedTile


# Create a clock object to control the frame rate
clock = pygame.time.Clock()


# Game loop
running = True
while running:

    # Set the frame rate
    clock.tick(10)

    if len(oneFakeMoves) > 0:
        direction = oneFakeMoves[0]
        if direction == "+y":
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
        elif direction == "-y":
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
        elif direction == "+x":
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
        elif direction == "-x":
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)

        del( oneFakeMoves[0] )
        _ = pygame.event.get()

        one.ProcessEvent(event, allOthers)
        
        # to avoid going to the else loop with my previous event.
        # event in the else-side will be undefined until something happens
        event = pygame.event.Event(pygame.NOEVENT)

    else:
        for event in pygame.event.get():
            running = ( event.type != pygame.QUIT )
        #
        one.ProcessEvent(event, allOthers)
    #

    canvas.fill((0, 180, 240))
    
    scenario.Draw(canvas, one, allOthers, event)
    # scenario.Draw(canvas)


    one.Draw(canvas)
    partner.Draw(canvas)
    
    for movable in listMovableTile:
        movable.Draw(canvas)
    #
        
    screen.blit(canvas, (0, 0))
    pygame.display.update()

#

one.SaveMoves()
partner.SaveMoves()


# Quit the game
pygame.quit()
sys.exit()
