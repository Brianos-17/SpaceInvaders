import pygame
import random

class Enemy:

    def __init__(self, image, x, y):
        self.enemyImg = image
        self.enemyX = x
        self.enemyY = y

    def move_enemy(self, x, y):
        self.enemyX += x
        if self.playerX <= 0:
            self.playerX = 0
            # self.playerY +=
        elif self.playerX >= 736:
            self.playerX = 736
        self.enemyY += y