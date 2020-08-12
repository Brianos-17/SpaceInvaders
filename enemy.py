import pygame
import random
import math

class Enemy:

    def __init__(self, image, x, y, xchange):
        self.enemyImg = image
        self.explosionImage = pygame.image.load("images/explosion.png").convert_alpha()
        self.enemyX = x
        self.enemyY = y
        self.enemyX_change = xchange

    def check_for_collision(self, bullet):
        if math.sqrt(
            math.pow(self.enemyX - bullet.bulletX, 2) +
            math.pow(self.enemyY - bullet.bulletY, 2)
        ) < 30:
            return True
        return False


class EnemyA(Enemy):

    def __init__(self, x):
        super().__init__(pygame.image.load("images/enemyA.png").convert_alpha(), x, 0, 0.3)

    def move_enemy(self):
        self.enemyX += self.enemyX_change
        if self.enemyX <= 0:
            self.enemyX = 0
            self.enemyY += 64
            self.enemyX_change = 0.3
        elif self.enemyX >= 736:
            self.enemyX = 736
            self.enemyY += 64
            self.enemyX_change = -0.3


class EnemyB(Enemy):

    def __init__(self, x):
        super().__init__(pygame.image.load("images/enemyB.png"), x, 0, 0.6)

    def move_enemy(self):
        self.enemyX += self.enemyX_change
        if self.enemyX <= 0:
            self.enemyX = 0
            self.enemyY += 64
            self.enemyX_change = 0.6
        elif self.enemyX >= 736:
            self.enemyX = 736
            self.enemyY += 64
            self.enemyX_change = -0.6


class EnemyC(Enemy):

    def __init__(self, x):
        super().__init__(pygame.image.load("images/enemyC.png"), x, 0, 0.9)

    def move_enemy(self):
        self.enemyX += self.enemyX_change
        if self.enemyX <= 0:
            self.enemyX = 0
            self.enemyY += 64
            self.enemyX_change = 0.9
        elif self.enemyX >= 736:
            self.enemyX = 736
            self.enemyY += 64
            self.enemyX_change = -0.9
