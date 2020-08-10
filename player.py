import pygame


class Player:
    def __init__(self):
        self.playerImg = pygame.image.load("images/player.png").convert_alpha()
        self.playerX = 370
        self.playerY = 480

    def move_player(self, x, y):
        self.playerX += x
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 736:
            self.playerX = 736

        self.playerY += y
        if self.playerY >= 536:
            self.playerY = 536
        elif self.playerY <= 372:
            self.playerY = 372


class Bullet:
    def __init__(self, player):
        self.bulletX = player.playerX + 23
        self.bulletY = player.playerY - 20
