import pygame


class Player:
    def __init__(self):
        self.playerImg = pygame.image.load("images/player.png").convert_alpha()
        self.X = 370
        self.Y = 480

    def move_player(self, x, y):
        self.X += x
        if self.X <= 0:
            self.X = 0
        elif self.X >= 736:
            self.X = 736

        self.Y += y
        if self.Y >= 536:
            self.Y = 536
        elif self.Y <= 372:
            self.Y = 372


class Bullet:
    def __init__(self, player):
        self.X = player.X + 23
        self.Y = player.Y - 20
