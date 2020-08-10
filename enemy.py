import pygame
import random
import math

class Enemy:

    def __init__(self, image, x, y):
        self.enemyImg = image
        self.explosionImage = pygame.image.load("images/explosion.png").convert_alpha()
        self.enemyX = x
        self.enemyY = y
        self.enemyX_change = 0.3

    def move_enemy(self):
        self.enemyX += self.enemyX_change
        if self.enemyX <= 0:
            self.enemyX = 0
            self.enemyY += 32
            self.enemyX_change = 0.3
        elif self.enemyX >= 736:
            self.enemyX = 736
            self.enemyY += 32
            self.enemyX_change = -0.3

    def chek_for_collision(self, bullet):
        if math.sqrt(
            math.pow(self.enemyX - bullet.bulletX, 2) +
            math.pow(self.enemyY - bullet.bulletY, 2)
        ) < 30:
            return True
        return False


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