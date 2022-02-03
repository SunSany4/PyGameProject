import pygame
import os
import sys
import math
from random import random
from Player import Player


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    pygame.display.init()
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Gorynych(pygame.sprite.Sprite):
    def __init__(self, x_pos=300, y_pos=20, *groups):
        super().__init__(groups)
        filename = os.path.join('gorynych.jpg')
        self.image = load_image(filename, -1)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.health = 100


class Fireball(pygame.sprite.Sprite):
    def __init__(self, x_pos=340, y_pos=30, player=None, *groups):
        super().__init__(groups)
        filename = os.path.join('fireball.png')
        self.image = load_image(filename, -1)
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.speed = 10
        self.direction_find(player)

    def direction_find(self, player):
        if player is None:
            self.dir_x = random()
            self.dir_y = random()
        else:
            player_x, player_y = player.get_position()
            player_x += 20
            dx = player_x - self.rect.x
            dy = abs(player_y - self.rect.y)
            angle = math.degrees(math.atan(dx / dy))
            self.dir_x = math.sin(math.radians(angle))
            self.dir_y = math.cos(math.radians(angle))

    def move(self):
        self.rect.x += self.speed * self.dir_x
        self.rect.y += self.speed * self.dir_y

    def get_position(self):
        return self.rect.x, self.rect.y, 12


def main():
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    fireball_group = pygame.sprite.Group()
    FPS = 60
    dir = ('RIGHT', 'LEFT', 'UP', 'DOWN', 'STOP')
    clock = pygame.time.Clock()
    running = True
    size = (750, 536)
    screen = pygame.display.set_mode(size)
    fon = pygame.transform.scale(pygame.image.load('data/fight_background.png'), size)
    screen.blit(fon, (0, 0))
    player = Player(325, 300, player_group)
    enemy = Gorynych(300, 150, enemy_group)
    motion = dir[4]
    speed = 5
    ticks = 0
    player_ticks = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    motion = dir[0]
                if event.key == pygame.K_LEFT:
                    motion = dir[1]
                if event.key == pygame.K_UP:
                    motion = dir[2]
                if event.key == pygame.K_DOWN:
                    motion = dir[3]
                if event.key == pygame.K_SPACE:
                    player.change_anim('fight')
                    player_pos = player.get_position()
                    if 300 <= player_pos[0] <= 350 and\
                            abs(player_pos[1] - 250) <= 40:
                        enemy.health -= 20
            else:
                motion = dir[4]

        if motion != dir[4]:
            if not player.run and not player.fight:
                player.change_anim('run')
            if not player.run:
                player.change_anim('run')
            if motion == dir[0]:
                if player.rect.x < 700:
                    player.rect.x += speed
            if motion == dir[1]:
                if player.rect.x > 5:
                    player.rect.x -= speed
            if motion == dir[2]:
                if player.rect.y > 5:
                    player.rect.y -= speed
            if motion == dir[3]:
                if player.rect.y < 436:
                    player.rect.y += speed
        else:
            if not player.idle and not player.fight:
                player.change_anim('idle')

        if ticks == 100:
            ticks = 0
            fireball = Fireball(325, 130, player, fireball_group)

        if player_ticks == 10:
            player_ticks = 0
            player_group.update()

        pygame.event.pump()

        screen.blit(fon, (0, 0))
        player_group.draw(screen)
        enemy_group.draw(screen)
        player_pos = player.get_position()
        fireballs_info = []
        for fireball in fireball_group:
            fireball.move()
            fireballs_info.append(fireball.get_position())

        for fireball in fireballs_info:
            if player_pos[0] <= fireball[0] + fireball[2] <= player_pos[0] + 57 and\
                player_pos[1] <= fireball[1] + fireball[2] <= player_pos[1] + 57:
                    player.health -= 10

        if player.health <= 0:
            return False
        if enemy.health <= 0:
            return True

        fireball_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

        ticks += 1
        player_ticks += 1

        # if not running:
        #     frame = 0
        #     player.change_anim('dead')
        #     ticks = 0
        #     while frame <= 7:
        #         print(ticks)
        #         player.image = player.dead_animation[frame]
        #         if ticks % 10000 == 0:
        #             frame += 1
        #         if ticks == 80000:
        #             return False
        #         ticks += 1


if __name__ == '__main__':
    main()
