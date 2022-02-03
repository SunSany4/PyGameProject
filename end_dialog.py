import pygame
from Player import Player
import os
import sys


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


def load_text(path):
    text = open(path, 'r', encoding='utf-8').readlines()
    text = list(map(lambda x: x.strip(), text))
    return text


def main():
    pygame.init()
    pygame.font.init()
    text = load_text('end dialog text.txt')
    size = [750, 536]
    screen = pygame.display.set_mode(size)
    screen.fill('black')
    fon = pygame.transform.scale(pygame.image.load('data' + '/' + 'backgrd.jpeg'), size)
    screen.blit(fon, (0, 0))
    text_coord = 10
    font = pygame.font.Font(None, 20)

    for line in text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
