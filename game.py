import pygame
import sys
from Scenario import Scenario
from Cube import Cube
from Ramp import Ramp
from Hider import Hider
from Seeker import Seeker
import copy


pygame.init()


scenario = Scenario()
width, height = scenario.GetMapSize()


canvas = pygame.Surface((width, height))
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hide and Seek")


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


# oneFakeMoves = one.listFakeMove.copy()
hiderPrevMoves  = hider.listFakeMove.copy()
seekerPrevMoves = seeker.listFakeMove.copy()


# listMovableTile = [cube1, cube2, cube3]
listMovableTile = [cube1, cube2]


allOthersForHider  = listFixedTile + listMovableTile + [seeker]
allOthersForSeeker = listFixedTile + listMovableTile + [hider]


# Create a clock object to control the frame rate
clock = pygame.time.Clock()


# Game loop
running = True
while running:

    # Set the frame rate
    clock.tick(10)

    if (len(hiderPrevMoves) > 0) or (len(seekerPrevMoves) > 0):
        if len(hiderPrevMoves) > 0:
            ####################################################################
            # hider
            ####################################################################
            direction = hiderPrevMoves[0]
            if direction == "+y":
                event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_x)
            elif direction == "-y":
                event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s)
            elif direction == "+x":
                event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_c)
            elif direction == "-x":
                event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_z)
            #
            del( hiderPrevMoves[0] )
            _ = pygame.event.get()
            #
            hider.ProcessEvent(event,  allOthersForHider)

        ########################################################################
        # seeker
        ########################################################################
        if len(seekerPrevMoves) > 0:
            direction = seekerPrevMoves[0]
            if direction == "+y":
                event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
            elif direction == "-y":
                event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
            elif direction == "+x":
                event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
            elif direction == "-x":
                event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
            #
            del( seekerPrevMoves[0] )
            _ = pygame.event.get()
            # 
            # one.ProcessEvent(event, allOthers)
            seeker.ProcessEvent(event, allOthersForSeeker)
        ########################################################################
        
        # to avoid going to the else loop with my previous event.
        # event in the else-side will be undefined until something happens
        event = pygame.event.Event(pygame.NOEVENT)

    else:
        for event in pygame.event.get():
            running = ( event.type != pygame.QUIT )
        #
                
        hider.ProcessEvent(event, allOthersForHider)
        seeker.ProcessEvent(event, allOthersForSeeker)
    #

    canvas.fill((0, 180, 240))
    
    # scenario.Draw(canvas, one, allOthers, event)
    scenario.Draw(canvas)

    hider.Draw(canvas)
    seeker.Draw(canvas)

    for movable in listMovableTile:
        movable.Draw(canvas)
    #
        
    screen.blit(canvas, (0, 0))
    pygame.display.update()

#

hider.SaveMoves()
seeker.SaveMoves()


# Quit the game
pygame.quit()
sys.exit()
