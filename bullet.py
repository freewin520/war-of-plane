import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,w, h):
        super().__init__()
        self.image = pygame.image.load('res/images/bullet1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = w
        self.rect.y = h
        self.speed = 5
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        if self.rect.y < 0-10:
            self.kill()  #数组删除
            del self  #内存删除
        else:
            self.rect.y -= self.speed

    def update(self,surface):
        self.move()
        self.draw(surface)


