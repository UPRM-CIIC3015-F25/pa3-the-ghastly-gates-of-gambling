import pygame
from enum import Enum

class Blind(Enum): # Base score values for each blind type
    SMALL = 300
    BIG = 600
    BOSS = 900
    NONE = 0

class SubLevel():
    def __init__(self, blind : Blind = Blind.NONE, ante = 0, bossLevel = ""):
        self.blind = blind
        self.ante = ante
        self.finished = False
        self.name = blind.name 
        self.bossLevel = bossLevel
        self.setUpScore()
        # --------- Loading blind image ----------
        if self.blind == Blind.SMALL:
            self.image = pygame.image.load("graphics/backgrounds/blinds/smallBlind.png").convert_alpha()
        elif self.blind == Blind.BIG:
            self.image = pygame.image.load("graphics/backgrounds/blinds/bigBlind.png").convert_alpha()
        else: # Default image for BOSS or NONE
            if self.bossLevel:
                if self.bossLevel == "The Water":
                    self.image = pygame.image.load("graphics/backgrounds/blinds/theWaterBlind.png").convert_alpha()
                elif self.bossLevel == "The Mark":
                    self.image = pygame.image.load("graphics/backgrounds/blinds/theMarkBlind.png").convert_alpha()
                elif self.bossLevel == "The House":
                    self.image = pygame.image.load("graphics/backgrounds/blinds/theHouseBlind.png").convert_alpha()
                elif self.bossLevel == "The Hook":
                    self.image = pygame.image.load("graphics/backgrounds/blinds/theHookBlind.png").convert_alpha()
                elif self.bossLevel == "The Manacle":
                    self.image = pygame.image.load("graphics/backgrounds/blinds/theManacleBlind.png").convert_alpha()
                elif self.bossLevel == "The Needle":
                    self.image = pygame.image.load("graphics/backgrounds/blinds/theNeedleBlind.png").convert_alpha()
                else:
                    self.image = pygame.image.load("graphics/backgrounds/blinds/smallBlind.png").convert_alpha()

    def setUpScore(self): # Sets up score based on blind and ante values
        if self.blind != Blind.NONE and self.ante != 0:  # Calculate score only if blind is valid and ante is valid
            self.score = int((self.blind.value) * (1.5 ** (self.ante - 1)))
        else:
            self.score = -1