import pygame


class Screen:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(pygame.image.load("images/icon.png"))

    def fill(self):
        self.screen.fill((0, 0, 0))

    def add_player(self, player):
        self.screen.blit(player.playerImg, (player.playerX, player.playerY))
        # pygame.display.update()

    def add_enemy(self, enemy):
        self.screen.blit(enemy.enemyImg, (enemy.enemyX, enemy.enemyY))
        # pygame.display.update()

