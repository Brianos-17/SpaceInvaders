import pygame

# Initalise the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

# Player
playerImg = pygame.image.load("images/player.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load("images/enemy1.png")
enemyX = 370
enemyY = 50
enemyX_change = 0
enemyY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = +0.3
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = +0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerY += playerY_change
    if playerY >= 536:
        playerY = 536
    elif playerY <= 372:
        playerY = 372

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()


