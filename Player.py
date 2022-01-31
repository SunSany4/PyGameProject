import pygame
import os
import sys


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    pygame.display.init()
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    # if color_key is not None:
    #     image = image.convert()
    #     if color_key == -1:
    #         color_key = image.get_at((0, 0))
    #     image.set_colorkey(color_key)
    # else:
    #     image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos=30, y_pos=30, *groups, animation=True):
        super().__init__(groups)
        pygame.init()
        self.animation = animation
        self.idle_animation = []
        self.fight_animation = []
        self.dead_animation = []
        self.run_animation = []
        self.current_frame = 0
        self.cut_idle_animation()
        self.cut_run_animation()
        self.cut_fight_animation()
        self.cut_dead_animation()
        self.image = self.idle_animation[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.current_animation = 'idle'
        self.run = False
        self.idle = True
        self.health = 100

    def change_anim(self, new_animation):
        try:
            assert new_animation in ['idle', 'run', 'fight', 'dead']
        except AssertionError:
            print('Wrong name animation')
        else:
            self.current_frame = 0
            self.current_animation = new_animation
            if new_animation == 'run':
                self.run = True
                self.idle = False
            else:
                self.run = False
                if new_animation == 'idle':
                    self.idle = True

    def cut_dead_animation(self):
        sheet = load_image(os.path.join('PlayerAnim.png'))
        self.rect = pygame.Rect(0, 0, (sheet.get_width() - 345) // 8,
                                100)

        for i in range(8):
            frame_location = (self.rect.w * i, 300)
            self.dead_animation.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))

    def cut_fight_animation(self):
        sheet = load_image(os.path.join('PlayerAnim.png'))
        self.rect = pygame.Rect(0, 0, sheet.get_width() // 11,
                                100)

        for i in range(11):
            frame_location = (self.rect.w * i, 200)
            self.fight_animation.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))

    def cut_run_animation(self):
        sheet = load_image(os.path.join('PlayerAnim.png'))
        self.rect = pygame.Rect(0, 0, (sheet.get_width() - 345) // 8,
                                100)

        for i in range(8):
            frame_location = (self.rect.w * i, 100)
            self.run_animation.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))

    def cut_idle_animation(self):
        sheet = load_image(os.path.join('PlayerAnim.png'))
        self.rect = pygame.Rect(0, 0, sheet.get_width() // 11,
                                100)

        for i in range(11):
            frame_location = (self.rect.w * i, 0)
            self.idle_animation.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))

    def get_position(self):
        return self.rect.x, self.rect.y

    def update(self):
        if self.animation:
            self.current_frame += 1
            # print(self.current_frame)
            if self.current_animation == 'idle':
                if self.current_frame != 0:
                    self.current_frame %= len(self.idle_animation)

                self.image = self.idle_animation[self.current_frame]
                print(self.image.get_rect().x, self.image.get_rect().y)
            elif self.run:
                if self.current_frame != 0:
                    self.current_frame %= len(self.run_animation)

                self.image = self.run_animation[self.current_frame]
            elif self.current_animation == 'fight':
                if self.current_frame != 0:
                    self.current_frame %= len(self.fight_animation)

                self.image = self.fight_animation[self.current_frame]
            else:
                if self.current_frame != 0:
                    self.current_frame %= len(self.dead_animation)

                self.image = self.dead_animation[self.current_frame]

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
