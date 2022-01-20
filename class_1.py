import pygame


class DialogueCharacter(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, animation, *groups):
        super().__init__(groups)
        self.animation = animation
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)

    def character_draw(self, index, x, y):  # отрисовка персонажа Q это картинка x и y это размеры картинки
        self.image = self.animation[index]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // x, self.image.get_height() // y))
        self.image.set_colorkey((255, 255, 255))

