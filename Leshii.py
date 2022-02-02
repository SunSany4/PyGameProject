import pygame
import random
from class_1 import DialogueCharacter


class Picture(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, imag, number, *groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(imag), (105, 54))
        self.number = number
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.informazia = (x_pos, y_pos, x_pos + 105, y_pos + 54, self.number)

    def infa_1(self, pos, r):
        if self.informazia[0] < pos[0] < self.informazia[2] and self.informazia[1] < pos[1] < self.informazia[3]:
            return self.informazia[4]
        else:
            return r

    def infa(self, pos, r):
        if self.informazia[0] < pos[0] < self.informazia[2] and self.informazia[1] < pos[1] < self.informazia[3]:
            return self.informazia[4]
        else:
            return r


def draw_text(screen, pos, text, size):  # отрисовка текста screen это поверхность на которой нужно нарисовать
    #  pos это позиция size это размер текст
    f = pygame.font.SysFont('arial', size)
    screen.blit(f.render(text, 1, (255, 255, 255)), pos)
    pygame.display.update()


def draw_surface(screen):
    surface1 = screen.convert_alpha()
    surface1.fill([0, 0, 0, 0])
    return surface1


def surface_1(image):
    surface = pygame.Surface((263 // 2.5, 137 // 2.5))
    surface.blit(pygame.image.load(image).convert_alpha(), (0, 0), (0, 0, 263 // 2.5, 137 // 2.5))
    return surface


def surf_draw(q, x, y):  # отрисовка бабы еги Q это картинка x и y это размеры
    surf = q
    surf = pygame.transform.scale(surf, (surf.get_width() // x, surf.get_height() // y))
    surf.set_colorkey((255, 255, 255))
    return surf


def run_leshii(text, screen=0, rt=0):
    pygame.init()
    leshii_group = pygame.sprite.Group()
    size = 750, 536
    if screen == 0:
        screen = pygame.display.set_mode(size)
    running = True
    fps = 20
    clock = pygame.time.Clock()
    pos = [(0, 445), (100, 400), (600, 400), (750, 445), (749, 445), (749, 535),
           (0, 535)]  # это координаты отрисовки диолога
    surface1 = draw_surface(screen)
    pygame.draw.polygon(surface1, (0, 0, 0, 170), pos)
    col = 0
    animation = [pygame.image.load("data/LESHII1.bmp"), pygame.image.load("data/LESHII2.bmp"),
                 pygame.image.load("data/LESHII3.bmp"), pygame.image.load("data/LESHII4.bmp")]
    leshii = DialogueCharacter(550, 140, animation, leshii_group)
    leshii_index = 0
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
        bg_surf = pygame.image.load("data/home_leshii.bmp").convert_alpha()
        bg_surf = pygame.transform.scale(bg_surf, (750, 536))
        pygame.draw.lines(surface1, (255, 215, 0), True, pos, 2)
        leshii_index = (leshii_index + 1) % 40
        leshii.character_draw(leshii_index // 10, 2.5, 2)
        leshii_group.draw(bg_surf)
        screen.blit(bg_surf, (0, 0))  # bg_surf это задний фон
        screen.blit(surface1, (0, 0))  # Отрисовка диолога на основном окне
        clock.tick(fps)
        pygame.display.flip()
        if col == 3:
            running = False
            screen.fill((0, 0, 0))
            if rt == 0:
                run(screen)
            else:
                return True
        else:
            lst = text[col].split('\n')
            y = 430
            for i in lst:
                draw_text(surface1, (100, y), i, 30)  # заного рисуем диолог с новым текстом
                y += 31
            draw_text(surface1, (690, 500), 'ENTER', 15)  # заного рисуем диолог с новым текстом
            pygame.display.flip()
    pygame.quit()


def run(screen):
    picture_group = pygame.sprite.Group()
    running = True
    fps = 120
    clock = pygame.time.Clock()
    bg_surf = pygame.image.load("data/home_leshii.bmp").convert_alpha()
    time = 60  # время
    print_message = pygame.USEREVENT
    pygame.time.set_timer(print_message, 1000)
    surface1 = draw_surface(screen)
    pygame.draw.polygon(surface1, (0, 0, 0, 170), ((0, 0), (750, 0), (750, 536), (0, 536)))
    lst_pos = [(530, 100), (645, 100), (530, 170), (645, 170), (530, 240), (645, 240),
               (530, 310), (645, 310), (530, 380), (645, 380), (530, 450), (645, 450), (60, 35), (175, 35),
               (290, 35), (405, 35)]
    lst_surface = ["data/pasl/image_part_001.bmp", "data/pasl/image_part_002.bmp", "data/pasl/image_part_003.bmp",
                   "data/pasl/image_part_004.bmp", "data/pasl/image_part_005.bmp", "data/pasl/image_part_006.bmp",
                   "data/pasl/image_part_007.bmp", "data/pasl/image_part_008.bmp", "data/pasl/image_part_009.bmp",
                   "data/pasl/image_part_010.bmp", "data/pasl/image_part_011.bmp", "data/pasl/image_part_012.bmp",
                   "data/pasl/image_part_013.bmp", "data/pasl/image_part_014.bmp", "data/pasl/image_part_015.bmp",
                   "data/pasl/image_part_016.bmp"]
    lst = []
    pos_image = (None, None)
    cartinka = 0
    random.shuffle(lst_pos)
    for i in range(16):
        lst.append((surface_1(lst_surface[i]), surface_1(lst_surface[i]).get_rect(center=lst_pos[i]),
                    int(lst_surface[i][-7:-4])))
    pos_pole = [(50.0, 150.0), (155.0, 150.0), (260.0, 150.0), (365.0, 150.0), (50.0, 204.0), (155.0, 204.0),
                (260.0, 204.0), (365.0, 204.0), (50.0, 258.0), (155.0, 258.0), (260.0, 258.0), (365.0, 258.0),
                (50.0, 312.0), (155.0, 312.0), (260.0, 312.0), (365.0, 312.0)]
    image_1 = Picture(lst_pos[0][0], lst_pos[0][1], lst_surface[0], 1, picture_group)
    image_2 = Picture(lst_pos[1][0], lst_pos[1][1], lst_surface[1], 2, picture_group)
    image_3 = Picture(lst_pos[2][0], lst_pos[2][1], lst_surface[2], 3, picture_group)
    image_4 = Picture(lst_pos[3][0], lst_pos[3][1], lst_surface[3], 4, picture_group)
    image_5 = Picture(lst_pos[4][0], lst_pos[4][1], lst_surface[4], 5, picture_group)
    image_6 = Picture(lst_pos[5][0], lst_pos[5][1], lst_surface[5], 6, picture_group)
    image_7 = Picture(lst_pos[6][0], lst_pos[6][1], lst_surface[6], 7, picture_group)
    image_8 = Picture(lst_pos[7][0], lst_pos[7][1], lst_surface[7], 8, picture_group)
    image_9 = Picture(lst_pos[8][0], lst_pos[8][1], lst_surface[8], 9, picture_group)
    image_10 = Picture(lst_pos[9][0], lst_pos[9][1], lst_surface[9], 10, picture_group)
    image_11 = Picture(lst_pos[10][0], lst_pos[10][1], lst_surface[10], 11, picture_group)
    image_12 = Picture(lst_pos[11][0], lst_pos[11][1], lst_surface[11], 12, picture_group)
    image_13 = Picture(lst_pos[12][0], lst_pos[12][1], lst_surface[12], 13, picture_group)
    image_14 = Picture(lst_pos[13][0], lst_pos[13][1], lst_surface[13], 14, picture_group)
    image_15 = Picture(lst_pos[14][0], lst_pos[14][1], lst_surface[14], 15, picture_group)
    image_16 = Picture(lst_pos[15][0], lst_pos[15][1], lst_surface[15], 16, picture_group)
    pole_surface = 'data/white_square.bmp'
    pole_1 = Picture(pos_pole[0][0], pos_pole[0][1], pole_surface, 1, picture_group)
    pole_2 = Picture(pos_pole[1][0], pos_pole[1][1], pole_surface, 2, picture_group)
    pole_3 = Picture(pos_pole[2][0], pos_pole[2][1], pole_surface, 3, picture_group)
    pole_4 = Picture(pos_pole[3][0], pos_pole[3][1], pole_surface, 4, picture_group)
    pole_5 = Picture(pos_pole[4][0], pos_pole[4][1], pole_surface, 5, picture_group)
    pole_6 = Picture(pos_pole[5][0], pos_pole[5][1], pole_surface, 6, picture_group)
    pole_7 = Picture(pos_pole[6][0], pos_pole[6][1], pole_surface, 7, picture_group)
    pole_8 = Picture(pos_pole[7][0], pos_pole[7][1], pole_surface, 8, picture_group)
    pole_9 = Picture(pos_pole[8][0], pos_pole[8][1], pole_surface, 9, picture_group)
    pole_10 = Picture(pos_pole[9][0], pos_pole[9][1], pole_surface, 10, picture_group)
    pole_11 = Picture(pos_pole[10][0], pos_pole[10][1], pole_surface, 11, picture_group)
    pole_12 = Picture(pos_pole[11][0], pos_pole[11][1], pole_surface, 12, picture_group)
    pole_13 = Picture(pos_pole[12][0], pos_pole[12][1], pole_surface, 13, picture_group)
    pole_14 = Picture(pos_pole[13][0], pos_pole[13][1], pole_surface, 14, picture_group)
    pole_15 = Picture(pos_pole[14][0], pos_pole[14][1], pole_surface, 15, picture_group)
    pole_16 = Picture(pos_pole[15][0], pos_pole[15][1], pole_surface, 16, picture_group)
    while running:
        for event in pygame.event.get():
            if event.type == print_message:
                if time == 0:
                    end_death(screen)
                    running = False
                elif cartinka == 16:
                    with open('level_pos.txt', 'a', encoding='utf-8') as file:
                        print(' 2', file=file, end='')
                    end_vin(screen)
                    running = False
                else:
                    time -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                pos_image = (pos_image[0], image_1.infa(pos, pos_image[1]))
                pos_image = (pole_1.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 1 == pos_image[1] and image_1.rect != pos_pole[0]:
                    image_1.rect = pos_pole[0]
                    pole_1.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_2.infa(pos, pos_image[1]))
                pos_image = (pole_2.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 2 == pos_image[1] and image_2.rect != pos_pole[1]:
                    image_2.rect = pos_pole[1]
                    pole_2.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_3.infa(pos, pos_image[1]))
                pos_image = (pole_3.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 3 == pos_image[1] and image_3.rect != pos_pole[2]:
                    image_3.rect = pos_pole[2]
                    pole_3.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_4.infa(pos, pos_image[1]))
                pos_image = (pole_4.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 4 == pos_image[1] and image_4.rect != pos_pole[3]:
                    image_4.rect = pos_pole[3]
                    pole_4.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_5.infa(pos, pos_image[1]))
                pos_image = (pole_5.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 5 == pos_image[1] and image_5.rect != pos_pole[4]:
                    image_5.rect = pos_pole[4]
                    pole_5.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_6.infa(pos, pos_image[1]))
                pos_image = (pole_6.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 6 == pos_image[1] and image_6.rect != pos_pole[5]:
                    image_6.rect = pos_pole[5]
                    pole_6.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_7.infa(pos, pos_image[1]))
                pos_image = (pole_7.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 7 == pos_image[1] and image_7.rect != pos_pole[6]:
                    image_7.rect = pos_pole[6]
                    pole_7.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_8.infa(pos, pos_image[1]))
                pos_image = (pole_8.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 8 == pos_image[1] and image_8.rect != pos_pole[7]:
                    image_8.rect = pos_pole[7]
                    pole_8.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_9.infa(pos, pos_image[1]))
                pos_image = (pole_9.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 9 == pos_image[1] and image_9.rect != pos_pole[8]:
                    image_9.rect = pos_pole[8]
                    pole_9.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_10.infa(pos, pos_image[1]))
                pos_image = (pole_10.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 10 == pos_image[1] and image_10.rect != pos_pole[9]:
                    image_10.rect = pos_pole[9]
                    pole_10.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_11.infa(pos, pos_image[1]))
                pos_image = (pole_11.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 11 == pos_image[1] and image_11.rect != pos_pole[10]:
                    image_11.rect = pos_pole[10]
                    pole_11.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_12.infa(pos, pos_image[1]))
                pos_image = (pole_12.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 12 == pos_image[1] and image_12.rect != pos_pole[11]:
                    image_12.rect = pos_pole[11]
                    pole_12.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_13.infa(pos, pos_image[1]))
                pos_image = (pole_13.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 13 == pos_image[1] and image_13.rect != pos_pole[12]:
                    image_13.rect = pos_pole[12]
                    pole_13.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_14.infa(pos, pos_image[1]))
                pos_image = (pole_14.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 14 == pos_image[1] and image_14.rect != pos_pole[13]:
                    image_14.rect = pos_pole[13]
                    pole_14.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_15.infa(pos, pos_image[1]))
                pos_image = (pole_15.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 15 == pos_image[1] and image_15.rect != pos_pole[14]:
                    image_15.rect = pos_pole[14]
                    pole_15.rect = 10000, 10000
                    cartinka += 1
                pos_image = (pos_image[0], image_16.infa(pos, pos_image[1]))
                pos_image = (pole_16.infa_1(pos, pos_image[0]), pos_image[1])
                if pos_image[0] == 16 == pos_image[1] and image_16.rect != pos_pole[15]:
                    image_16.rect = pos_pole[15]
                    pole_16.rect = 10000, 10000
                    cartinka += 1
                print(pos_image, cartinka)
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg_surf, (0, 0))
        screen.blit(surface1, (0, 0))
        picture_group.draw(screen)
        draw_text(screen, (650, 10), f'{time // 60}:{time - (60 * (time // 60))}', 50)  # отрисовка текста
        clock.tick(fps)
    pygame.quit()


def end_death(screen):
    running = True
    fps = 20
    clock = pygame.time.Clock()
    animation = [pygame.image.load("data/death_leghii_1.bmp"), pygame.image.load("data/death_leghii_2.bmp"),
                 pygame.image.load("data/death_leghii_3.bmp"), pygame.image.load("data/death_leghii_4.bmp"),
                 pygame.image.load("data/death_leghii_5.bmp"), pygame.image.load("data/death_leghii_6.bmp"),
                 pygame.image.load("data/death_leghii_7.bmp"), pygame.image.load("data/death_leghii_8.bmp"),
                 pygame.image.load("data/death_leghii_9.bmp"), pygame.image.load("data/death_leghii_10.bmp")]
    bg_surf = animation[0]
    pygame.transform.scale(bg_surf, (750, 536))
    surface1 = draw_surface(screen)
    pygame.draw.polygon(surface1, (0, 0, 0, 200), ((0, 0), (750, 0), (750, 536), (0, 536)))
    draw_text(surface1, (100, 140), 'Ты мертв!', 150)
    number_background = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos() >= (255, 350):
                    if pygame.mouse.get_pos() <= (525, 418):
                        return False
        number_background = (number_background + 1) % 40
        bg_surf = animation[number_background // 4]
        bg_surf = pygame.transform.scale(bg_surf, (750, 536))
        screen.blit(bg_surf, (0, 0))
        screen.blit(surface1, (0, 0))
        pygame.draw.rect(surface1, (255, 0, 0), ((255, 350), (270, 68)))
        draw_text(surface1, (265, 360), 'начать с начала', 40)
        clock.tick(fps)
        pygame.display.flip()
    return False


def end_vin(screen):
    run_leshii(['Спасибо тебе добрый молодец', 'За это я тебе отдам свою кальчугу', 'Идти дальше.'], screen, 1)
    return True


if __name__ == '__main__':
    run_leshii(['Какой ветер тебя ко мне в лес занес? \nА не лук со стрелами нужен тебе?',
                'Сослужи службу: колесо водяной сломалось,\n сможешь собрать отплочу чем хочешь', 'Начать.'])
