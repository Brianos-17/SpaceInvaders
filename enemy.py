import pygame
import random

class Enemy:

    def __init__(self):
        self.enemyImg = pygame.image.load("images/enemy1.png")
        self.enemyX = 0 #random.randint(0, 736)
        self.enemyY = 0 #random.randint(50, 150)

    def move_enemy(self, x, y):
        self.enemyX += x
        if self.playerX <= 0:
            self.playerX = 0
            # self.playerY +=
        elif self.playerX >= 736:
            self.playerX = 736
        self.enemyY += y