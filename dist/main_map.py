import pygame
import os
import sys
from Player import *


def clear_screen(screen, fon):
    screen.blit(fon, (0, 0))


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
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.rad = 15
        self.x_pos = x_pos
        self.y_pos = y_pos

    def get_info(self):
        return self.x_pos, self.y_pos, self.rad


def draw_text(screen, pos, text, size):  # отрисовка текста screen это поверхность на которой нужно нарисовать
    #  pos это позиция size это размер текст
    f = pygame.font.SysFont('arial', size)
    screen.blit(f.render(text, 1, (255, 255, 255)), pos)
    pygame.display.update()


def main():
    pygame.init()
    pygame.font.init()
    player_group = pygame.sprite.Group()
    level_dots_group = pygame.sprite.Group()
    FPS = 60

    dir = ('RIGHT', 'LEFT', 'UP', 'DOWN', 'STOP')
    clock = pygame.time.Clock()
    size = (750, 536)
    screen = pygame.display.set_mode(size)
    pygame.display.set_icon(pygame.image.load('data/icon.jpg').convert())
    pygame.display.set_caption('Тридевятое царство')
    level = open('level_pos.txt').readline()

    running = True
    screen.fill('black')
    fon = pygame.transform.scale(pygame.image.load('data/main_map.jpg'), size)
    screen.blit(fon, (0, 0))
    player = Player(280, 100, player_group)
    player.image = pygame.transform.scale(player.image, (60, 60))
    motion = dir[4]
    speed = 1
    text = {
        '1': (162, 210)
    }
    level_1 = LevelDot(150, 200, level_dots_group)
    if '2' in level:
        text['2'] = (312, 320)
        level_2 = LevelDot(300, 310, level_dots_group)
    if '3' in level:
        text['3'] = (597, 285)
        level_3 = LevelDot(585, 275, level_dots_group)

    ticks = 0
    draw_text(fon, (340, 40), 'Управляя стрелками зайдите на кружок.', 25)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit('main.py')
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
        dots_infos = []
        for dot in level_dots_group:
            dots_infos.append(dot.get_info())

        for i in range(len(dots_infos)):
            if dots_infos[i][0] - dots_infos[i][2] <= player_pos[0] <= dots_infos[i][0] + dots_infos[i][2] and \
                    dots_infos[i][1] - dots_infos[i][2] <= player_pos[1] <= dots_infos[i][1] + dots_infos[i][2]:
                return i + 1

        if motion != dir[4]:
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
            if not player.idle:
                player.change_anim('idle')

        ticks += 1
        if ticks == 10:
            player.update()
            ticks = 0
        clear_screen(screen, fon)
        player.draw(screen)
        level_dots_group.draw(screen)
        font = pygame.font.Font(None, 20)
        for line, text_coord in text.items():
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            screen.blit(string_rendered, text_coord)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.QUIT()


if __name__ == '__main__':
    main()
