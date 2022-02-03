import main_map
from Player import *
import pygame


def clear_screen(screen, fon, text, font, text_coord):
    screen.blit(fon, (0, 0))

    for line in text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def main():
    pygame.init()
    pygame.font.init()
    player_group = pygame.sprite.Group()
    player = Player(650, 420, player_group)
    text = ['Кликните мышкой в любое место, чтобы начать игру']
    size = [750, 536]
    screen = pygame.display.set_mode(size)
    screen.fill('black')
    fon = pygame.transform.scale(load_image('backgrd.jpeg'), size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 20)
    text_coord = 20
    ticks = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        if ticks == 200:
            player_group.update()
            ticks = 0
        ticks += 1
        clear_screen(screen, fon, text, font, text_coord)
        player_group.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
    main_map.main()
