import pygame

class Plate(pygame.sprite.Sprite):
    BLACK = 'black.png'
    YELLOW = 'yellow.png'
    ROCK = 'rock.png'

    SIZE = (60,60)
    def __init__(self, position, type=ROCK, visible=False):
        self.type = type
        self.visible = visible
        self.rect.left, self.rect.top = position
        pygame.sprite.Sprite.__init__(self)

    @property
    def visible(self):
        return self.__visible
    
    @visible.setter
    def visible(self, v):
        image_path = 'img/'
        if v:
            image_path += self.type
        else:
            image_path += Plate.BLACK

        self.image = pygame.image.load(image_path)
        if not hasattr(self, 'rect'):
            self.rect = self.image.get_rect()
