import pygame
from pygame.sprite import Sprite
from random import randint
import time
class bomb_supply(Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.image = pygame.image.load('res/images/bomb_supply.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(30, w-30)
        self.rect.y = randint(-h, -100)
        self.speed = 7
        self.active_flag = False
        self.h = h
        self.w = w
        self.mask = pygame.mask.from_surface(self.image)
    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def move(self):
        if self.active_flag == True:
            if self.rect.bottom + self.speed < self.h:
                self.rect.y += self.speed
            else:
                self.reset()

    def reset(self):
        self.rect.x = randint(30,self.w-30)
        self.rect.y = randint(-self.h, -100)
        self.active_flag = False

    def update(self,surface):
        self.move()
        self.draw(surface)



class bullet_supply(Sprite):
    def __init__(self, w, h):
        super().__init__()
        self.image = pygame.image.load('res/images/bullet_supply.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(30, w - 30)
        self.rect.y = randint(-h, -100)
        self.speed = 7
        self.active_flag = False
        self.h = h
        self.w = w
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        if self.active_flag == True:
            if self.rect.bottom + self.speed < self.h:
                self.rect.y += self.speed
            else:
                self.reset()

    def reset(self):
        self.rect.x = randint(30, self.w - 30)
        self.rect.y = randint(-self.h, -100)
        self.active_flag = False

    def update(self, surface):
        self.move()
        self.draw(surface)