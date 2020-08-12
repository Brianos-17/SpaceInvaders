import pygame


class Screen:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(pygame.image.load("images/icon.png"))
        self.font = pygame.font.Font('freesansbold.ttf', 32)  # Default font for pygame

        # Loading bullet image here and reusing to reduce load
        self.bulletImage = pygame.image.load("images/bullet.png").convert_alpha()
        self.background = pygame.image.load("images/background.jpg").convert()

    def fill(self):
        self.screen.blit(self.background, (0, 0))

    def add_player(self, player):
        self.screen.blit(player.playerImg, (player.X, player.Y))

    def add_enemy(self, enemy):
        self.screen.blit(enemy.enemyImg, (enemy.enemyX, enemy.enemyY))

    def add_bullet(self, bullet):
        bullet.Y -= 0.3
        self.screen.blit(self.bulletImage, (bullet.X, bullet.Y))

    def kill_enemy(self, enemy):
        self.screen.blit(enemy.explosionImage, (enemy.enemyX, enemy.enemyY))

    def show_score(self, score):
        score_value = self.font.render("Score: " + str(score), True, (255, 255, 255))
        self.screen.blit(score_value, (10, 10))

    def game_over(self):
        game_over = self.font.render("GAME OVER", True, (255, 0, 0))
        self.screen.blit(game_over, (400, 300))

