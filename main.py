import pygame
import neat
import os
import random
import sys

pygame.init()

#
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 60
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

UNITS = [pygame.image.load(os.path.join("sprites/units/", "P_Blue.png")),
         pygame.image.load(os.path.join("sprites/units/", "W_Blue.png")),
         pygame.image.load(os.path.join("sprites/units/", "P_Yellow.png")),
         pygame.image.load(os.path.join("sprites/units/", "W_Yellow.png"))
         ]

P_COLORS = {
    'Blue': UNITS[0],
    'Yellow': UNITS[2]
}
W_COLORS = {
    'Blue': UNITS[1],
    'Yellow': UNITS[3]
}

BUILDINGS = [pygame.image.load(os.path.join("sprites/buildings", "Field.png")),
             pygame.image.load(os.path.join("sprites/buildings", "Main_Home_Yellow.png")),
             pygame.image.load(os.path.join("sprites/buildings", "Main_Home_Blue.png"))
             ]


BACKGROUND = 0

FONT = 0


class Object:
    X_POS = None
    Y_POS = None
    IMAGE = None


class Unit(Object):
    SPEED = None
    TYPE = None
    HEALTH = None

    def get_hit(self, value):
        self.HEALTH -= value


class Building(Object):
    TYPE = None
    HEALTH = None


class Fabric(Building):
    TYPE = 'Fabric'
    HEALTH = 10

    def __init__(self, x_pos, y_pos):
        self.X_POS = x_pos
        self.Y_POS = y_pos
        self.IMAGE = BUILDINGS[0]

    def placed(self):
        SCREEN.blit(self.IMAGE, (self.X_POS, self.Y_POS))


class PeacefulUnit(Unit):
    TYPE = 'Peaceful'
    HEALTH = 100
    SPEED = 1

    def __init__(self, x_pos, y_pos, color):
        self.X_POS = x_pos
        self.Y_POS = y_pos
        self.COLOR = color
        self.IMAGE = P_COLORS[color]


def main():
    clock = pygame.time.Clock()

    example = Fabric(100, 100)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Начало игры
        SCREEN.fill((255, 255, 255))
        user_input = pygame.mouse.get_pressed()
        if user_input[pygame.KEYDOWN]:
            example.placed()

        clock.tick(FPS)
        pygame.display.update()


main()
