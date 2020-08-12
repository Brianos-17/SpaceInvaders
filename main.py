import pygame
import random
from screen import Screen
from player import Player, Bullet
from enemy import EnemyA, EnemyB, EnemyC

# Initalise the pygame
enemies = []
enemyA_image = pygame.image.load("images/enemyA.png")
enemyB_image = pygame.image.load("images/enemyB.png")
enemyC_image = pygame.image.load("images/enemyC.png")

def run():
    pygame.init()

    screen = Screen()

    player = Player()
    playerX_change = 0
    playerY_change = 0
    screen.add_player(player)
    bullets = []

    for enemy in enemies:
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
                    playerX_change -= 0.5
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerX_change += 0.5
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    playerY_change -= 0.5
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    playerY_change += 0.5
                if event.key == pygame.K_SPACE:
                    if len(bullets) < 5:
                        bullet = Bullet(player)
                        bullets.append(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    playerY_change = 0

        player.move_player(playerX_change, playerY_change)
        screen.add_player(player)

        for enemy in enemies:
            enemy.move_enemy()
            screen.add_enemy(enemy)
            for bullet in bullets:
                screen.add_bullet(bullet)
                if bullet.bulletY < 0:
                    bullets.remove(bullet)
                if enemy.check_for_collision(bullet):
                    screen.kill_enemy(enemy)
                    # Show Explosion briefly
                    pygame.display.update()
                    enemies.remove(enemy)

        if len(enemies) == 0:
            x = random.randint(0, 320)
            while len(enemies) < 4:
                create_enemyA(x)
                x += 64

        pygame.display.update()


def create_enemyA(x):
    enemy = EnemyA(enemyA_image, x)
    enemies.append(enemy)


def create_enemyB(x):
    enemy = EnemyB(enemyB_image, x)
    enemies.append(enemy)


def create_enemyC(x):
    enemy = EnemyC(enemyC_image, x)
    enemies.append(enemy)


if __name__ == '__main__':
    run()
