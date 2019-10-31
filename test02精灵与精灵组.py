import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from random import randint


# 精灵与精灵组的使用

class Myplane(pygame.sprite.Sprite):
	def __init__(self,surface):
		# 调用父类初始化函数
		super().__init__()
		self.image = surface
		self.rect = surface.get_rect()
	def draw(self,surface):
		surface.blit(self.image,self.rect)

class Enemyplane(pygame.sprite.Sprite):
	def __init__(self,surface):
		super().__init__()
		self.image = surface
		self.rect = surface.get_rect()
		self.rect.x = randint(10,470)
		self.rect.y = randint(0,700)
	def draw(self,surface):
		surface.blit(self.image,self.rect)

# 初始化、创建窗口等
pygame.init()
screen = pygame.display.set_mode((480,700))
pygame.display.set_caption("myplane")
icon = pygame.image.load('res/images/plane.ico')
pygame.display.set_icon(icon)

# 加载背景
bg = pygame.image.load('res/images/background.png').convert()
# 加载飞机图片
plane1 = pygame.image.load('res/images/me1.png')
# 加载敌机
enemy = pygame.image.load('res/images/enemy1.png')

# 实例化一个我方飞机
myplane2 = Myplane(plane1)
# 实例化5个敌机
enemy_list = [ Enemyplane(enemy) for x in range(5) ]
# 将5敌机加入到一个精灵组中
enemy_group = pygame.sprite.Group(*enemy_list)

# 创建clock对象监控时间
clock = pygame.time.Clock()
# 隐藏鼠标
pygame.mouse.set_visible(False)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		

	# 绘制背景
	screen.blit(bg,(0,0))
	# 绘制我方飞机
	myplane2.draw(screen)
	# 绘制敌机
	enemy_group.draw(screen)
	# 碰撞检测，如果我方飞机碰到敌机，杀死敌机（从精灵组中删除）
	pygame.sprite.spritecollide(myplane2,enemy_group,True)
	

	# 按键操作飞机
	keys = pygame.key.get_pressed()
	if keys[K_w]:
		myplane2.rect.y-=10
	if keys[K_s]:
		myplane2.rect.y+=10
	if keys[K_a]:
		myplane2.rect.x-=10
	if keys[K_d]:
		myplane2.rect.x+=10

	pygame.display.flip()


	clock.tick(20)
	print(clock.get_fps())




