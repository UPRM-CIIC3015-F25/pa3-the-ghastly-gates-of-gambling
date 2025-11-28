import pygame

class Jokers:
    def __init__(self,name: str, description: str, price = 5, chips = 0, mult = 0, image = None, isActive = False):
        self.name = name
        self.description = description
        self.price = price
        self.chips = chips
        self.mult = mult
        self.image = image
        self.isActive = isActive

    def __str__(self):
        return f"{self.name}: {self.description}"

    def sellPrice(self):
        return int(self.price * 0.6)
    
