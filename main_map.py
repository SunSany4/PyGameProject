import pygame
import os
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos=30, y_pos=30, *groups):
        super().__init__(groups)
        filename = os.path.join('data', 'player.png')
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)


class LevelDot(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, *groups):
        super().__init__(groups)
        filename = os.path.join('data', 'level_dot.png')
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
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


def main():
    player_group = pygame.sprite.Group()
    level_dots_group = pygame.sprite.Group()
    FPS = 60

    dir = ('RIGHT', 'LEFT', 'UP', 'DOWN', 'STOP')
    clock = pygame.time.Clock()
    running = True
    size = (700, 400)
    screen = pygame.display.set_mode(size)
    player = Player(30, 30, player_group)
    motion = dir[4]
    speed = 5
    level_1 = LevelDot(100, 300, level_dots_group)
    level_2 = LevelDot(300, 400, level_dots_group)
    level_3 = LevelDot(600, 100, level_dots_group)

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

        pygame.event.pump()

        screen.fill('black')
        player_group.draw(screen)
        level_dots_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.QUIT()


if __name__ == '__main__':
    main()
