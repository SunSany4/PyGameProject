import pygame
import os
import sys
from Player import *
import fight


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


class LevelDot(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, *groups):
        super().__init__(groups)
        self.image = load_image('level_dot.png', -1)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.rad = 25
        self.x_pos = x_pos
        self.y_pos = y_pos

    def get_info(self):
        return self.x_pos, self.y_pos, self.rad


def main():
    player_group = pygame.sprite.Group()
    level_dots_group = pygame.sprite.Group()
    FPS = 60

    dir = ('RIGHT', 'LEFT', 'UP', 'DOWN', 'STOP')
    clock = pygame.time.Clock()
    running = True
    size = (700, 400)
    screen = pygame.display.set_mode(size)
    player = Player(30, 30, player_group, animation=False)
    motion = dir[4]
    speed = 5
    level_1 = LevelDot(100, 300, level_dots_group)
    level_2 = LevelDot(600, 100, level_dots_group)

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

        player_pos = player.get_position()
        dot_2_info = level_2.get_info()

        if dot_2_info[0] <= player_pos[0] <= dot_2_info[0] + 2 * dot_2_info[2] and\
                dot_2_info[1] <= player_pos[1] <= dot_2_info[1] + 2 * dot_2_info[2]:
            return 2

        if motion != dir[4]:
            if motion == dir[0]:
                player.rect.x += speed
            if motion == dir[1]:
                player.rect.x -= speed
            if motion == dir[2]:
                player.rect.y -= speed
            if motion == dir[3]:
                player.rect.y += speed

        screen.fill('black')
        player_group.draw(screen)
        level_dots_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.QUIT()


if __name__ == '__main__':
    next_scene = main()
    print(next_scene)
    if next_scene == 2:
        fight.main()
