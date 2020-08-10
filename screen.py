import pygame


class Screen:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(pygame.image.load("images/icon.png"))

        # Loading bullet image here and reusing to reduce load
        self.bulletImage = pygame.image.load("images/bullet.png").convert_alpha()

    def fill(self):
        self.screen.blit(pygame.image.load("images/background.jpg"), (0, 0))

    def add_player(self, player):
        self.screen.blit(player.playerImg, (player.playerX, player.playerY))

    def add_enemy(self, enemy):
        self.screen.blit(enemy.enemyImg, (enemy.enemyX, enemy.enemyY))

    def add_bullet(self, bullet):
        bullet.bulletY -= 10
        self.screen.blit(self.bulletImage, (bullet.bulletX, bullet.bulletY))

