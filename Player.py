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
        pygame.init()
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
        self.fight = False
        self.dead = False
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
                self.fight = False
                self.dead = False
            elif new_animation == 'idle':
                self.run = False
                self.idle = True
                self.fight = False
                self.dead = False
            elif new_animation == 'fight':
                self.run = False
                self.idle = False
                self.fight = True
                self.dead = False
            else:
                self.run = False
                self.idle = False
                self.fight = False
                self.dead = True

    def cut_dead_animation(self):
        sheet = load_image(os.path.join('PlayerAnim.png'))
        self.rect = pygame.Rect(0, 0, 60,
                                100)

        left = 0
        for i in range(8):
            frame_location = (self.rect.w * i, 310)
            self.dead_animation.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))
            left += 60 + 60

    def cut_fight_animation(self):
        sheet = load_image(os.path.join('PlayerAnim.png'))
        self.rect = pygame.Rect(0, 0, 60,
                                100)

        left = 0
        for i in range(11):
            frame_location = (left, 210)
            self.fight_animation.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))
            left += 59 + 60

    def cut_run_animation(self):
        sheet = load_image(os.path.join('PlayerAnim.png'))
        self.rect = pygame.Rect(0, 0, 60,
                                100)
        left = 0
        for i in range(8):
            frame_location = (left, 100)
            self.run_animation.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))
            left += 65 + 60

    def cut_idle_animation(self):
        sheet = load_image(os.path.join('PlayerAnim.png'))
        self.rect = pygame.Rect(0, 0, 60,
                                100)
        left = 0
        for i in range(11):
            frame_location = (left, 0)
            self.idle_animation.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))
            left += 120

    def get_position(self):
        return self.rect.x, self.rect.y

    def update(self):
        self.current_frame += 1
        if self.idle:
            if self.current_frame != 0:
                self.current_frame %= len(self.idle_animation)

            self.image = self.idle_animation[self.current_frame]
        elif self.run:
            if self.current_frame != 0:
                self.current_frame %= len(self.run_animation)

            self.image = self.run_animation[self.current_frame]
        elif self.fight:
            if self.current_frame != 0:
                if self.current_frame == len(self.fight_animation):
                    self.fight = False
                    self.idle = True
                else:
                    self.current_frame %= len(self.fight_animation)

                    self.image = self.fight_animation[self.current_frame]

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def dead_event(self):
        self.current_frame = 0
        ticks = 0
        while self.current_frame <= 7:
            self.image = self.dead_animation[self.current_frame]
            if ticks == 250:
                self.current_frame += 1
                ticks = 0
            ticks += 1
