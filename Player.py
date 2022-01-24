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
        self.animation = animation
        self.idle_animation = []
        self.fight_animation = []
        self.dead_animation = []
        self.run_animation = []
        self.current_frame = 0
        self.cut_idle_animation()
        self.image = self.idle_animation[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.current_animation = 'idle'

    def change_anim(self, new_animation):
        try:
            assert new_animation in ['idle', 'run', 'fight', 'dead']
        except AssertionError:
            print('Wrong name animation')
        else:
            self.current_frame = 0
            self.current_animation = new_animation

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
            if self.current_animation == 'idle':
                self.current_frame %= len(self.idle_animation)

                self.image = self.idle_animation[self.current_frame]
                rect = self.image.get_rect()
            elif self.current_animation == ' run':
                self.current_frame %= len(self.run_animation)

                self.image = self.idle_animation[self.current_frame]
            elif self.current_animation == 'fight':
                self.current_frame %= len(self.fight_animation)

                self.image = self.idle_animation[self.current_frame]
            else:
                self.current_frame %= len(self.dead_animation)

                self.image = self.idle_animation[self.current_frame]
