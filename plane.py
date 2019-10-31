import pygame
from pygame.sprite import Sprite
from pygame.locals import K_a,K_d,K_w,K_s
from random import randint
import time
class Myplane(Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.images = [pygame.image.load('res/images/me1.png'),
                    pygame.image.load('res/images/me2.png')]
        self.destroy_images = [
            pygame.image.load('res/images/me_destroy_1.png'),
            pygame.image.load('res/images/me_destroy_2.png'),
            pygame.image.load('res/images/me_destroy_3.png'),
            pygame.image.load('res/images/me_destroy_4.png')
        ]
        self.rect = self.images[0].get_rect()
        self.rect.centerx = w/2
        self.rect.y = h - 150
        self.active_flag = True
        self.counter = 0
        self.speed = 10
        self.life = 2
        self.w = w
        self.h = h
        self.bomb = 3
        self.bullet = 1
        self.mask = pygame.mask.from_surface(self.images[0])

    def draw(self,surface):
        if self.active_flag:
            surface.blit(self.images[self.counter//2%2], self.rect)
        else:
            surface.blit(self.destroy_images[self.counter//2%4], self.rect)
            self.counter += 1
            if self.counter == 8 and self.life >= 0:
                time.sleep(0.5)
                self.reset()
                self.counter = 0
                self.life -= 1

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            if self.rect.centerx - self.speed > 30:
                self.rect.x -= self.speed
        if keys[K_d]:
            if self.rect.centerx + self.speed < 450:
                self.rect.x += self.speed
        if keys[K_w]:
            if self.rect.centery - self.speed > 60:
                self.rect.y -= self.speed
        if keys[K_s]:
            if self.rect.centery + self.speed < 550:
                self.rect.y += self.speed
    def reset(self):
        self.bomb = 3
        self.bullet = 1
        self.rect.centerx = self.w / 2
        self.rect.y = self.h - 150
        self.active_flag = True

    def update(self,surface):
        self.move()
        self.draw(surface)

class Enemyplane(Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.image = pygame.image.load('res/images/enemy1.png')
        self.destroy_images = [pygame.image.load('res/images/enemy1_down1.png'),
                               pygame.image.load('res/images/enemy1_down2.png'),
                               pygame.image.load('res/images/enemy1_down3.png'),
                               pygame.image.load('res/images/enemy1_down4.png')]
        self.rect =self.image.get_rect()
        self.rect.x = randint(10,w-40)
        self.rect.y = randint(-h,0)
        self.speed = 5
        self.active_flag = True
        self.h = h
        self.w = w
        self.counter = 0
        self.life = 2
        self.bullet = 1
    def draw(self,surface):
        if self.active_flag:
            surface.blit(self.image,self.rect)
        else:
            #绘制销毁的图片
            surface.blit(self.destroy_images[self.counter%4],self.rect)
            self.counter += 1
            if self.counter == 4:
                self.counter = 0
                self.reset()

    def move(self):
        if self.rect.bottom + self.speed < self.h:
            self.rect.y += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.x = randint(10,self.w-40)
        self.rect.y = randint(-self.h, 0)
        self.active_flag = True

    def update(self,surface):
        self.move()
        self.draw(surface)



