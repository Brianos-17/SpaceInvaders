import pygame
import random
from screen import Screen
from player import Player, Bullet
from enemy import EnemyA, EnemyB, EnemyC
from pygame import mixer

# Initalise the pygame
enemies = []
enemyA_image = pygame.image.load("images/enemyA.png")
enemyB_image = pygame.image.load("images/enemyB.png")
enemyC_image = pygame.image.load("images/enemyC.png")

def run():
    pygame.init()

    screen = Screen()
    # mixer.music.load('sounds/background.wav')
    # mixer.music.play(-1)

    player = Player()
    playerX_change = 0
    playerY_change = 0
    screen.add_player(player)
    score = 0
    bullets = []

    for enemy in enemies:
        screen.add_enemy(enemy)

    # Game Loop
    running = True
    while running:
        screen.fill()
        screen.show_score(score)

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
                    if len(bullets) < 50  :
                        bullet = Bullet(player)
                        bullets.append(bullet)
                        mixer.Sound('sounds/laser.wav').play()

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
            if enemy.check_for_collision(player):
                screen.game_over()
                running = False
            for bullet in bullets:
                screen.add_bullet(bullet)
                if bullet.Y < 0:
                    bullets.remove(bullet)
                if enemy.check_for_collision(bullet):
                    screen.kill_enemy(enemy)
                    # Show Explosion briefly
                    pygame.display.update()
                    enemies.remove(enemy)
                    mixer.Sound('sounds/explosion.wav').play()
                    score += 1

        if len(enemies) == 0:
            x = random.randint(0, 320)
            if score < 80:
                while len(enemies) < 5:
                    if score < 20:
                        create_enemyA(x)
                    if 20 <= score < 50:
                        create_enemyB(x)
                    if 50 <= score < 80:
                        create_enemyC(x)
                    x += 64
            if 80 <= score < 150:
                while len(enemies) < 10:
                    create_enemyC(x)
                    x += 64
            if 150 <= score:
                while len(enemies) < 15:
                    create_enemyC(x)
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
