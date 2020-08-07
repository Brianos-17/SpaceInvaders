import pygame
from screen import Screen
from player import Player
from enemy import Enemy, EnemyA

# Initalise the pygame
pygame.init()

screen = Screen()
player = Player()
playerX_change = 0
playerY_change = 0

enemy = EnemyA()
enemyX_change = 0
enemyY_change = 0

screen.add_player(player)
screen.add_enemy(enemy)

# Game Loop
running = True
while running:
    screen.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change -= 0.3
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change += 0.3
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change -= 0.3
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change += 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0

    player.move_player(playerX_change, playerY_change)
    screen.add_player(player)
    screen.add_enemy(enemy)
    pygame.display.update()

    # enemy(enemyX, enemyY)



