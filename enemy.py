import pygame
import random

class Enemy:

    def __init__(self, image, x, y):
        self.enemyImg = image
        self.enemyX = x
        self.enemyY = y
        self.enemyX_change = 7

    def move_enemy(self):
        self.enemyX += self.enemyX_change
        if self.enemyX <= 0:
            self.enemyX = 0
            self.enemyY += 32
            self.enemyX_change = 7
        elif self.enemyX >= 736:
            self.enemyX = 736
            self.enemyY += 32
            self.enemyX_change = -7


class EnemyA(Enemy):

    def __init__(self):
        super().__init__(pygame.image.load("images/enemyA.png").convert_alpha(),
                         random.randint(0, 736),
                         0)


class EnemyB(Enemy):

    def __init__(self):
        super().__init__(pygame.image.load("images/enemyB.png"),
                         random.randint(0, 736),
                         0)


class EnemyC(Enemy):

    def __init__(self):
        super().__init__(pygame.image.load("images/enemyC.png"),
                         random.randint(0, 736),
                         0)