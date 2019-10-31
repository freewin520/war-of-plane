import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from random import randint

# 初始化pygame
pygame.init()

# 创建一个窗口，参数(w,h)
screen = pygame.display.set_mode((480,700))
# 修改窗口标题
pygame.display.set_caption("myplane")
# 加载窗口图标
icon = pygame.image.load('res/images/plane.ico')
# 设置窗口图标
pygame.display.set_icon(icon)

# 加载背景图片 load函数返回serface对象
bg = pygame.image.load('res/images/background.png').convert()
# 获取图片大小、rect对象
print(bg.get_size())
print(bg.get_rect().center)
print(bg.get_rect().x+5)

# 绘制背景
screen.blit(bg,(0,0))

# 加载飞机图片
plane1 = pygame.image.load('res/images/me1.png')
plane2 = pygame.image.load('res/images/me2.png')
# 获取飞机的rect对象
plane_rect = plane1.get_rect()

# 设置鼠标隐藏
# pygame.mouse.set_visible(False)


# 加载暂停和恢复图片
pause = pygame.image.load('res/images/pause_nor.png')
resume = pygame.image.load('res/images/resume_nor.png')
# 获取rect
pause_rect = pause.get_rect() 
# 设置图片绘制位置 x、y
pause_rect.x = 320
pause_rect.y = 10
# 设置绘制暂停 or 恢复 标志  True=>绘制pause
pause_flag = True 


# 定义 自定义事件类型
MYEVENT = USEREVENT + 1
# 定时 发送自定义事件到事件队列 ，时间单位为毫秒
pygame.time.set_timer(MYEVENT,1000)

# 另一种方法： 推送事件到事件队列
# pygame.event.post(MYEVENT,("name":"liyr"))
# event.name 

count = 0

# 实例化clock 用于监控时间
clock = pygame.time.Clock()

# 加载字体
myfont = pygame.font.Font('res/font/font.ttf',30)
# 准备字体内容 > 返回surface对象 
mytext = myfont.render("code",True,(0,0,0))


# 加载音乐 music 流式音乐，同时只能播放一首
pygame.mixer.music.load('res/sound/game_music.ogg')
# 播放  n 循环n次+1   -1时为无限循环   
pygame.mixer.music.play(-1) 

# 加载音频（可同时播放多个） 
sound = pygame.mixer.Sound('res/sound/enemy1_down.wav')
sound.play()

while True:
	# 获取并变量每个事件
	for event in pygame.event.get():
		# 检测事件类型
		# 退出事件
		if event.type == QUIT:
			exit()
		# 鼠标弹起事件
		if event.type == MOUSEBUTTONUP:
			# 判断鼠标弹起位置 是否在 暂停键图片区域
			if pause_rect.collidepoint(event.pos):
				# 在该区域弹起鼠标（按下）  切换图片显示标记
				pause_flag = not pause_flag

		# 自定义事件
		if event.type == MYEVENT:
			print("触发Myevnet")
			# 时间为0 关闭自定义事件
			pygame.time.set_timer(MYEVENT,0)


		# 按键按下事件
		# 通过按键事件控制飞机位移
		# if event.type == KEYDOWN:
		# 	if event.key == K_w:
		# 		plane_rect.y-=10
		# 	if event.key == K_s:
		# 		plane_rect.y+=10
		# 	if event.key == K_a:
		# 		plane_rect.x-=10
		# 	if event.key == K_d:
		# 		plane_rect.x+=10

	# 循环计算值
	count+=1

	# 绘制背景
	screen.blit(bg,(0,0))
	
	# 通过获取按键状态，控制飞机位移
	# 获取按下状态 修改飞机rect (x,y,w,h)中x,y坐标
	keys = pygame.key.get_pressed()
	if keys[K_w]:
		plane_rect.y-=10
	if keys[K_s]:
		plane_rect.y+=10
	if keys[K_a]:
		plane_rect.x-=10
	if keys[K_d]:
		plane_rect.x+=10

	# 通过获取鼠标位置控制飞机位移
	# pos = pygame.mouse.get_pos()
	# plane_rect.center = pos
	
	# count是个计数值，偶数绘制图1 奇数绘制图2
	if count%2:
		screen.blit(plane1,plane_rect) 
	else:
		screen.blit(plane2,plane_rect)

	# 简单图形绘制 矩形、圆圈、线
	pygame.draw.rect(screen,(0,0,0),(10,10,20,30))	
	pygame.draw.circle(screen,(23,32,45),(50,50),10)
	pygame.draw.line(screen,(34,56,32),(10,15),(120,170),5)
	
	# 判断pause_flag 绘制暂停 or 恢复
	if pause_flag:
		screen.blit(pause,pause_rect)
	else:
		screen.blit(resume,pause_rect)

	# 绘制文本
	screen.blit(mytext,(120,120))
	
	# 刷新页面
	pygame.display.flip()

	# print(pygame.mouse.get_pressed())
	# print(pygame.mouse.get_pos())
	# res = pygame.key.get_pressed()
	# for x in range(len(res)):
	# 	if res[x] :
	# 		print(pygame.key.name(x))
	# if res[K_a]:
	# 	print("a按下")

	# 设置帧率
	clock.tick(20)
	# 打印帧率
	print(clock.get_fps())




