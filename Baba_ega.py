import pygame
from class_1 import DialogueCharacter


def draw_text(screen, pos, text, size):  # отрисовка текста screen это поверхность на которой нужно нарисовать
    #  pos это позиция size это размер текст
    f = pygame.font.SysFont('arial', size)
    screen.blit(f.render(text, 1, (255, 255, 255)), pos)
    pygame.display.update()


def draw_surface(screen):
    surface1 = screen.convert_alpha()
    surface1.fill([0, 0, 0, 0])
    return surface1


def baba_ege_run():
    baba_ega_group = pygame.sprite.Group()
    pygame.init()
    size = width, height = 750, 536
    screen = pygame.display.set_mode(size)
    running = True
    fps = 20
    clock = pygame.time.Clock()
    bg_surf = pygame.image.load("data/home_baba_ega_1.bmp").convert_alpha()
    bg_surf = pygame.transform.scale(bg_surf, (750, 536))
    number_baba_ega = 0
    col = 0  # переменная для отслеживания индекса текста
    text = ['Что то русским духом по пахивает.\n Знаю нужны тебе доспехи,\n Помощь нужна мне, мыши одолели.',
            'Сможещь отловить, получишь, что хочешь.\n Не успеешь спраивиться,\nсуп у меня вкусный будет на ужин.',
            'Начать.']
    pos = [(0, 445), (100, 400), (600, 400), (750, 445), (749, 445), (749, 535), (0, 535)]  # это поле отрисовки диолога
    surface1 = draw_surface(screen)
    pygame.draw.polygon(surface1, (0, 0, 0, 170), pos)
    animation = [pygame.image.load("data/baba_ega_1.bmp"), pygame.image.load("data/baba_ega_2.bmp"),
                 pygame.image.load("data/baba_ega_4.bmp"), pygame.image.load("data/baba_ega_6.bmp"),
                 pygame.image.load("data/baba_ega_1.bmp")]
    bg_baba_ega = DialogueCharacter(500, -50, animation, baba_ega_group)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # если игрок кликает мышкой или наживает энтер то следуйщая фраза
                col += 1
                surface1 = draw_surface(screen)  # отрисовка диолога
                pygame.draw.polygon(surface1, (0, 0, 0, 170), pos)
            if event.type == pygame.KEYDOWN:  # энтер
                if event.key == 13:
                    col += 1
                    surface1 = draw_surface(screen)
                    pygame.draw.polygon(surface1, (0, 0, 0, 170), pos)
        bg_surf = pygame.image.load("data/home_baba_ega_1.bmp").convert_alpha()
        bg_surf = pygame.transform.scale(bg_surf, (750, 536))
        number_baba_ega = (number_baba_ega + 1) % 35
        pygame.draw.lines(surface1, (255, 215, 0), True, pos, 2)
        bg_baba_ega.character_draw(number_baba_ega % 35 // 7, 3, 2.5)
        baba_ega_group.draw(bg_surf)
        screen.blit(bg_surf, (0, 0))  # bg_surf это задний фон
        screen.blit(surface1, (0, 0))  # Отрисовка диолога на основном окне
        clock.tick(fps)
        pygame.display.flip()
        if col == 3:
            running = False
            screen.fill((0, 0, 0))
            baba_ege_house(screen, baba_ega_group, bg_baba_ega)
        else:
            lst = text[col].split('\n')
            y = 430
            for i in lst:
                draw_text(surface1, (100, y), i, 30)  # заного рисуем диолог с новым текстом
                y += 31
            draw_text(surface1, (690, 500), 'ENTER', 15)  # заного рисуем диолог с новым текстом
            pygame.display.flip()
    pygame.quit()


def baba_ege_house(screen, baba_ega_group, bg_baba_ega):
    running = True
    fps = 20
    col_mouse = 7
    clock = pygame.time.Clock()
    bg_surf = pygame.image.load("data/home_baba_ega_2.bmp").convert_alpha()  # задний фон с мышаами
    number_baba_ega = 0
    pos_mouse = [((204, 370), (250, 438), (224, 399)), ((120, 423), (150, 468), (136, 447)),
                 ((452, 430), (486, 474), (458, 454)), ((483, 58), (548, 94), (516, 74)),
                 ((294, 178), (325, 208), (310, 190)), ((190, 57), (238, 89), (211, 71)),
                 ((628, 65), (671, 100), (651, 83))]
    # в этих кортеджах 1 и 2 элемент это позиции квдрата с мышами а 3 позиция для отрисовки круга
    time = 30  # время
    print_message = pygame.USEREVENT  # это эвент который срабатывает каждую секунду
    pygame.time.set_timer(print_message, 1000)  # сам таймер которых срабатывает каждую секунду
    bg_baba_ega.rect = (540, 115)
    while running:
        for event in pygame.event.get():
            if event.type == print_message:
                if time == 0:
                    end(screen, 0)
                    running = False
                elif col_mouse == 0:
                    end(screen, 1)
                    running = False
                else:
                    time -= 1
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for i in pos_mouse:
                    if i[0][0] <= pos[0] and i[0][1] <= pos[1]:
                        if i[1][0] >= pos[0] and i[1][1] >= pos[1]:
                            col_mouse -= 1
                            pygame.draw.circle(bg_surf, (255, 255, 255, 255), i[2], 31, 4)
                            pos_mouse.remove(i)
        number_baba_ega = (number_baba_ega + 1) % 35
        bg_baba_ega.character_draw(number_baba_ega % 35 // 7, 4, 3.5)
        screen.blit(bg_surf, (0, 0))
        baba_ega_group.draw(screen)
        draw_text(screen, (650, 10), f'{time // 60}:{time - (60 * (time // 60))}', 50)  # отрисовка текста
        if col_mouse == 7 or col_mouse == 5 or col_mouse == 6:  # это склонение
            text = f'Найдите {col_mouse} мышей.'
        elif col_mouse != 1 and col_mouse != 0:
            text = f'Найдите {col_mouse} мыши.'
        elif col_mouse == 1:
            text = f'Найдите {col_mouse} мышь.'
        else:
            text = 'Вы нашли всех мышей'
        draw_text(screen, (0, 490), text, 30)  # отрисовка текста с количеством мышей
        clock.tick(fps)
    pygame.quit()


def end(screen, q):  # после завершения игры надо запустить катцену с победой или СМЕРТЬ
    if q:
        print('вы выйграли')
    else:
        print('Вы проиграли')
    pass


if __name__ == '__main__':
    baba_ege_run()
