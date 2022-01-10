import pygame
import os
import sys
import math
from random import random


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos=30, y_pos=30, *groups):
        super().__init__(groups)
        filename = os.path.join('data', 'player.png')
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)

    def get_position(self):
        return self.rect.x, self.rect.y


class Gorynych(pygame.sprite.Sprite):
    def __init__(self, x_pos=300, y_pos=20, *groups):
        super().__init__(groups)
        filename = os.path.join('data', 'gorynych.png')
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)


class Fireball(pygame.sprite.Sprite):
    def __init__(self, x_pos=325, y_pos=20, player=None, *groups):
        super().__init__(groups)
        filename = os.path.join('data', 'fireball.png')
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (25, 25))
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
            dx = player_x - self.rect.x
            dy = abs(player_y - self.rect.y)
            angle = math.degrees(math.atan(dx / dy))
            self.dir_x = math.sin(math.radians(angle))
            self.dir_y = math.cos(math.radians(angle))

    def move(self):
        self.rect.x += self.speed * self.dir_x
        self.rect.y += self.speed * self.dir_y


def main():
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    fireball_group = pygame.sprite.Group()
    FPS = 60
    dir = ('RIGHT', 'LEFT', 'UP', 'DOWN', 'STOP')
    clock = pygame.time.Clock()
    running = True
    size = (700, 400)
    screen = pygame.display.set_mode(size)
    player = Player(325, 300, player_group)
    enemy = Gorynych(300, 20, enemy_group)
    motion = dir[4]
    speed = 5
    ticks = 0

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
            else:
                motion = dir[4]

        if motion != dir[4]:
            if motion == dir[0]:
                player.rect.x += speed
            if motion == dir[1]:
                player.rect.x -= speed
            if motion == dir[2]:
                player.rect.y -= speed
            if motion == dir[3]:
                player.rect.y += speed

        if ticks == 300:
            ticks = 0
            fireball = Fireball(325, 30, player, fireball_group)

        pygame.event.pump()

        screen.fill('black')
        player_group.draw(screen)
        enemy_group.draw(screen)
        for fireball in fireball_group:
            fireball.move()
        fireball_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

        ticks += 1

    pygame.QUIT()


if __name__ == '__main__':
    main()
