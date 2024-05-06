import os
import pygame
import random
import sys

from Character import Character
from Text import Text
import gameListScreen
import __main__

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def galaxyattack():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    backgroundColor = (32, 32, 32)
    textColor = (201, 201, 201)

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    keysPressed = {}
    bullets = []
    enemies = []

    last_enemy_time = 0
    enemy_delay = 2500

    last_bullet_time = 0
    bullet_delay = 120

    bullet_picture = pygame.image.load('Games\\GalaxyAttack\\galaxyattackbullet.png')
    enemy_picture = pygame.image.load('Games\\GalaxyAttack\\galaxyattackenemy.png')
    enemy_picture = pygame.transform.rotate(enemy_picture, 180)
    enemy_picture = pygame.transform.scale(enemy_picture, (int(width/15), int(width/15)))

    gameIsOver = False
    gameOverTimer = 5000
    gameOverStartTime = 0

    canMove = True

    scoreCount = 0

    player = Character('Games\\GalaxyAttack\\galaxyattackspaceship.png', int(width/8), int(width/8), int(width/2.25), int(height/1.4))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_ESCAPE):
                    gameListScreen.render()
                keysPressed[event.key] = True
            elif event.type == pygame.KEYUP:
                keysPressed[event.key] = False

        if keysPressed.get(pygame.K_w) and player.y >= height/1.5 and canMove:
            player.y -= width/300
        if keysPressed.get(pygame.K_s) and player.y <= height - player.height and canMove:
            player.y += width/300
        if keysPressed.get(pygame.K_a) and player.x >= 0 and canMove:
            player.x -= width/300
        if keysPressed.get(pygame.K_d) and player.x <= width - player.width and canMove:
            player.x += width/300

        screen.fill(backgroundColor)
        player.render(screen)

        score = Text('Score: ' + str(scoreCount), (width/5, height/5), 45)

        # Enemy Logic
        for enemy in enemies:
            enemy[1] += 1
            if(enemy[1] > height):
                enemies.remove(enemy)
                gameIsOver = True

        if(gameIsOver):
            if gameOverStartTime == 0:
                gameOverStartTime = pygame.time.get_ticks()

            gameOver = Text('Game Over!', (width, height), 196)
            gameOver.render(screen)
            canMove = False

            current_time = pygame.time.get_ticks()
            if current_time - gameOverStartTime >= gameOverTimer:
                enemies = []
                bullets = []
                __main__.main() #Maybe make this go to gameListScreen instead of __main__
                break

        
        current_time = pygame.time.get_ticks()
        if current_time - last_enemy_time > enemy_delay and canMove:
            enemies.append([random.randint(0, width-int(width/15)), 0])
            if(enemy_delay > 1500):
                enemy_delay -= 5
            last_enemy_time = current_time
        
        for enemy in enemies:
            screen.blit(enemy_picture, (enemy[0], enemy[1]))

        # Bullet Logic
        for bullet in bullets:
            bullet[1] -= 10

        bullets = [bullet for bullet in bullets if bullet[0] > 0]

        current_time = pygame.time.get_ticks()
        if keysPressed.get(pygame.K_SPACE) and canMove and current_time - last_bullet_time > bullet_delay:
            bullets.append([player.x + player.width / 2 - 16, player.y])
            last_bullet_time = current_time

        for bullet in bullets:
            screen.blit(bullet_picture, (bullet[0], bullet[1]))

        # Collision Detection
        for bullet in bullets:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_picture.get_width(), bullet_picture.get_height())
            for enemy in enemies:
                enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_picture.get_width(), enemy_picture.get_height())
                if check_collision(bullet_rect, enemy_rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    scoreCount += 1
                    break
        
        score.render(screen)

        pygame.display.flip()
        clock.tick(60)

galaxyattack()
