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


def draw_surface(screen):
    surface1 = screen.convert_alpha()
    surface1.fill([0, 0, 0, 0])
    return surface1


def draw_text(screen, pos, dialog_text, size):  # отрисовка текста
    f = pygame.font.SysFont('arial', size)
    screen.blit(f.render(dialog_text, 1, (255, 255, 255)), pos)
    pygame.display.update()


def main(time_game=1):
    pygame.init()
    pygame.font.init()
    text = load_text('end dialog text.txt')
    size = [750, 536]
    screen = pygame.display.set_mode(size)
    #    text.append('Нажмите на любую кнопку для продолжения...')

    col = 0  # переменная для отслеживания сколько раз игрок нажал ентер
    pos = [(0, 445), (100, 400), (600, 400), (750, 445), (749, 445), (749, 535), (0, 535)]  # это поле отрисовки диолога
    surface1 = draw_surface(screen)
    pygame.draw.polygon(surface1, (0, 0, 0, 170), pos)

    running = True
    text[-1] = text[-1] + 'enter' + f'Вы прошли игру за {time_game} секунд'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # если игрок кликает мышкой или наживает энтер то следуйщая фраза
                col += 1
                surface1 = draw_surface(screen)  # отрисовка диолога
                pygame.draw.polygon(surface1, (0, 0, 0, 170), pos)
            if event.type == pygame.KEYDOWN:
                if event.key == 13:  # энтер
                    col += 1
                    surface1 = draw_surface(screen)
                    pygame.draw.polygon(surface1, (0, 0, 0, 170), pos)
        fon = pygame.transform.scale(pygame.image.load("data/backgrd.jpeg"), size)

        pygame.draw.lines(surface1, (255, 215, 0), True, pos, 2)

        screen.blit(fon, (0, 0))  # fon это задний фон
        screen.blit(surface1, (0, 0))  # Отрисовка диолога на основном окне
        pygame.display.flip()
        if col == 3:
            return
        else:
            lst = text[col].split('enter')
            y = 430
            for i in lst:
                draw_text(surface1, (100, y), i, 20)  # заного рисуем диолог с новым текстом
                y += 31
            draw_text(surface1, (690, 500), 'ENTER', 18)  # заного рисуем диолог с новым текстом
            pygame.display.flip()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
