import pygame


class Player:

    def __init__(self):
        self.playerImg = pygame.image.load("images/player.png")
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


