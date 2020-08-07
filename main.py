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


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                pass
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                pass
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                pass
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                pass

    player(playerX, playerY)
    pygame.display.update()


