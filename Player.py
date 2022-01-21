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
    def __init__(self, x_pos=30, y_pos=30, *groups):
        super().__init__(groups)
        filename = os.path.join('playerAnim', 'idle', 'anim0.png')
        self.image = load_image(filename)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.idle_animation = []
        self.fight_animation = []
        self.dead_animation = []
        self.run_animation = []
        self.current_animation = 'idle'
        self.current_frame = 0
        self.transparent = (0, 0, 0, 0)
        self.setup_animation()

    def change_anim(self, new_animation):
        try:
            assert new_animation in ['idle', 'run', 'fight', 'dead']
        except AssertionError:
            print('Wrong animation')
        else:
            self.current_frame = 0
            self.current_animation = new_animation

    def setup_animation(self):
        main_str = 'anim'
        self.idle_animation = []
        path = os.path.join('playerAnim', 'idle')
        for i in range(11):
            img_name = main_str + str(i) + '.png'
            self.idle_animation.append(load_image(os.path.join(path, img_name)))

    def get_position(self):
        return self.rect.x, self.rect.y

    def update(self):
        if self.current_animation == 'idle':
            self.current_frame += 1
            self.current_frame %= len(self.idle_animation)

            self.image = self.idle_animation[self.current_frame]
        elif self.current_animation == ' run':
            self.current_frame += 1
            self.current_frame %= len(self.run_animation)

            self.image = self.idle_animation[self.current_frame]
        elif self.current_animation == 'fight':
            self.current_frame += 1
            self.current_frame %= len(self.fight_animation)

            self.image = self.idle_animation[self.current_frame]
        else:
            self.current_frame += 1
            self.current_frame %= len(self.dead_animation)

            self.image = self.idle_animation[self.current_frame]
