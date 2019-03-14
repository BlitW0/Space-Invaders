import pygame
import sys
import os
import time
from Aliens import *
from Ship import *
from Missile import *
from MissileA import *
from MissileB import *
from pygame.locals import *

pygame.init()

display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Space Invaders')


def get_image(img, width, height):
    image = pygame.image.load(os.path.join(game_path, img)).convert()
    image = pygame.transform.scale(image, (width, height))
    return image

ship = Ship(display, get_image(ship_img, 100, 150))
bullets = []
aliens = []

aliens_x = []
image = get_image(alien_img, 100, 100)
for x in range(10, display_width - image.get_width() - 10, 110):
    aliens_x.append(x)

is_taken = {}
for x in aliens_x:
    is_taken[x] = False

aliens_y = [100, 210]

start_time = time.time()
start_time -= 10

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ship.x_change = -5
            elif event.key == pygame.K_d:
                ship.x_change = 5
            elif event.key == pygame.K_SPACE:
                image = get_image(missile_img, 50, 50)
                x = ship.rect.centerx - 25
                y = ship.rect.top
                bullets.append(MissileA(display, image, x, y, 10))
            elif event.key == pygame.K_s:
                image = get_image(missile_img, 50, 50)
                x = ship.rect.centerx - 25
                y = ship.rect.top
                bullets.append(MissileB(display, image, x, y, 15))
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                ship.x_change = 0

    display.fill(black)

    ship.display_score()
    ship.draw()

    for alien in aliens:
        alien.draw()

    for bullet in bullets:
        bullet.draw()

    cur_time = time.time()

    ship.move()

    if cur_time - start_time >= 10:
        image = get_image(alien_img, 100, 100)
        x = aliens_x[random.randint(0, len(aliens_x) - 1)]
        y = aliens_y[random.randint(0, len(aliens_y) - 1)]
        if is_taken[x]:
            x = aliens_x[random.randint(0, len(aliens_x) - 1)]
            y = aliens_y[random.randint(0, len(aliens_y) - 1)]
        aliens.append(Alien(display, image, x, y, cur_time))
        start_time = cur_time

    for bullet in bullets:
        if bullet.y - bullet.v < 100:
            bullets.remove(bullet)
        else:
            bullet.move()

    for alien in aliens:

        kill = False
        incr_time = 0

        for bullet in bullets:
            rem = False
            incr_time, rem, kill = bullet.utility(alien, incr_time, rem, kill)
            if rem:
                bullets.remove(bullet)

        if kill:
            ship.hit_count += 1
            aliens.remove(alien)
        else:
            if incr_time > 0:
                image = get_image(frozen_alien, 100, 100)
                alien.image = image
                diff = cur_time - alien.spawn_time
                if diff < 5:
                    alien.spawn_time -= 5 - diff
                else:
                    alien.spawn_time += diff - 5
            if cur_time - alien.spawn_time >= 8:
                is_taken[alien.x] = False
                aliens.remove(alien)

    pygame.display.update()
    clock.tick(30)
