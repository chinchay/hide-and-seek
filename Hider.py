from Agent import Agent
import pygame

class Hider(Agent):
    def __init__(self, filename, x, y, ID, movesFileName) -> None:
        super().__init__(filename, x, y, ID, movesFileName)
        self.rightFilename = "images/hider50a.png"
        self.leftFilename  = "images/hider50b.png"
        pass

    def GetDirection(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_x:
                    self.isWalking = True
                    self.deg = 180
                    return "+y"
                case pygame.K_s:
                    self.isWalking = True
                    self.deg = 0
                    return "-y"
                case pygame.K_z:
                    self.isWalking = True
                    self.deg = 90
                    return "-x"
                case pygame.K_c:
                    self.isWalking = True
                    self.deg = -90
                    return "+x"
        #
        self.isWalking = False
        return None

    # def GetDirection(self, event):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_s]:
    #         self.isWalking = True
    #         self.deg = 180
    #         return "+y"
    #     elif keys[pygame.K_w]:
    #         self.isWalking = True
    #         self.deg = 0
    #         return "-y"
    #     elif keys[pygame.K_a]:
    #         self.isWalking = True
    #         self.deg = 90
    #         return "-x"
    #     elif keys[pygame.K_d]:
    #         self.isWalking = True
    #         self.deg = -90
    #         return "+x"
    #     #
    #     self.isWalking = False
    #     return None
    # #



