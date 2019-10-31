import pygame
from pygame.locals import *
from sys import exit
from plane import Myplane, Enemyplane
from bullet import Bullet
from supply import bomb_supply,bullet_supply
from pygame.sprite import collide_mask
from random import choice
import time
pygame.init()
# 创建一个窗口
w=480
h=600
screen = pygame.display.set_mode((w,h))
fontObj = pygame.font.SysFont('utf-8', 40)



# 加载资源文件
bg = pygame.image.load('res/images/background.png')
bg2 = pygame.image.load('res/images/background.png')
bg_rect = bg.get_rect()
bg2_rect = bg2.get_rect()
again_btn = pygame.image.load('res/images/again.png')
again_btn_rect = again_btn.get_rect()
again_btn_rect.centerx = bg_rect.centerx
again_btn_rect.y =300
gameover_btn = pygame.image.load('res/images/gameover.png')
gameover_btn_rect = gameover_btn.get_rect()
gameover_btn_rect.centerx = bg_rect.centerx
gameover_btn_rect.y=400
pause0_btn = pygame.image.load('res/images/pause_nor.png')
pause0_btn_rect = gameover_btn.get_rect()
pause0_btn_rect.x = 400
pause0_btn_rect.y= 10
pause1_btn = pygame.image.load('res/images/pause_pressed.png')
pause1_btn_rect = gameover_btn.get_rect()
pause1_btn_rect.x = 400
pause1_btn_rect.y= 10
resume0_btn = pygame.image.load('res/images/resume_nor.png')
resume0_btn_rect = gameover_btn.get_rect()
resume0_btn_rect.x = 350
resume0_btn_rect.y= 10
resume1_btn = pygame.image.load('res/images/resume_pressed.png')
resume1_btn_rect = gameover_btn.get_rect()
resume1_btn_rect.x = 350
resume1_btn_rect.y = 10
# 全局变量声明
run_flag = True
score = 0
life = 2
pause = False
def mygame():

    # 初始化标记变量
    clock = pygame.time.Clock()
    counter = 0
    global score
    score = 0
    global pause
    pause = False
    # global life
    # life = 2

    # 创建精灵实体
    plane = Myplane(w, h)
    supply1 = bomb_supply(w,h)
    supply2 = bullet_supply(w,h)
    bullet_group = pygame.sprite.Group(Bullet(plane.rect.centerx, plane.rect.y))
    enemy_group = pygame.sprite.Group(*[Enemyplane(w,h) for x in range(10)])
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONUP:
                # 判断鼠标弹起位置 是否在 暂停键图片区域
                if pause0_btn_rect.collidepoint(event.pos):
                    pause = True
                elif resume0_btn_rect.collidepoint(event.pos):
                    pause = False
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            if plane.bomb > 0:
                count = 0
                for i in enemy_group:
                    if i.rect.y > 0:
                        i.active_flag = False
                        count += 1
                plane.bomb -= 1
                score += count*100


        #分数
        textSurfaceObj = fontObj.render(u'Score: %i' % score, False, (0, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        if pause:
            screen.blit(resume0_btn, resume0_btn_rect)
            screen.blit(pause1_btn, pause1_btn_rect)
            pygame.display.update(resume0_btn_rect)
            continue

        else:
            bg_rect.y += 1
            bg2_rect.y = bg_rect.y - h
            if bg_rect.y >= 600:
                bg_rect.y = 0
            screen.blit(bg, bg_rect)
            screen.blit(bg2, bg2_rect)
            screen.blit(resume1_btn, resume1_btn_rect)
            screen.blit(pause0_btn, pause0_btn_rect)
        screen.blit(textSurfaceObj, textRectObj)


        # 飞机
        plane.update(screen)
        # 子弹
        bullet_group.update(screen)

        # 每循环12次创建一个子弹
        if counter%12 ==0:
            if plane.bullet == 1:
                bullet_group.add(Bullet(plane.rect.centerx,plane.rect.y))
            else:
                bullet_group.add(Bullet(plane.rect.x+20,plane.rect.y))
                bullet_group.add(Bullet(plane.rect.x + 85,plane.rect.y))
        if score%2000 == 0:
            supply1.active_flag = True
            supply2.active_flag = True
        enemy_group.update(screen)
        supply1.update(screen)
        supply2.update(screen)
        for i in enemy_group:
            pygame.draw.rect(screen, (255, 0, 0),
                             (i.rect.x, i.rect.y, 50, 8))
            pygame.draw.rect(screen, (0, 128, 0), (i.rect.x, i.rect.y, 50, 8))



        #子弹碰撞事件
        collide_dict = pygame.sprite.groupcollide(bullet_group, enemy_group, True, False,collide_mask)
        tmp = []
        for i in collide_dict.values():
            tmp += i
        for i in tmp:
            i.active_flag = False
        score += len(tmp) * 100
        print(score)


        #飞机碰撞事件
        # for i in enemy_group:
        #     if pygame.Rect.colliderect(plane.rect, i.rect):
        #         i.active_flag = False
        #         plane.active_flag = False
        #         break
        if plane.active_flag:
            collide_list = pygame.sprite.spritecollide(plane, enemy_group, False, collide_mask)
            collide_supply1 = pygame.sprite.collide_mask(plane, supply1)
            collide_supply2 = pygame.sprite.collide_mask(plane, supply2)
            if collide_supply2:
                plane.bullet += 1
                supply2.reset()
            if collide_supply1:
                plane.bomb += 1
                supply1.reset()
            for i in collide_list:
                i.active_flag = False
            if collide_list and counter > 50:
                plane.active_flag = False
                counter = 0





        counter += 1
        if plane.life < 0:
            global run_flag
            run_flag = False
            break

        if score == 1000:
            if len(enemy_group)<15:
                enemy_group.add(*[Enemyplane(w,h) for x in range(5)])

        pygame.display.flip()
            #设置帧率
        clock.tick(30)
        # 检测事件
		# 绘制背景
		# 更新精灵等 状态 比如位置等
		# 碰撞检测
		# 绘制精灵
		# 绘制图片、文字


def gameover():
    # 绘制结束页面
    screen.blit(bg, bg_rect)
    screen.blit(again_btn, again_btn_rect)
    screen.blit(gameover_btn, gameover_btn_rect)
    pygame.display.flip()
    while True:
        # 事件检测
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONUP:
                # 判断鼠标弹起位置 是否在 暂停键图片区域
                if again_btn_rect.collidepoint(event.pos):
                    global run_flag
                    run_flag = True
                    break
                if gameover_btn_rect.collidepoint(event.pos):
                    exit()
        if run_flag:
            break


if __name__ == '__main__' :
    while True:
        if run_flag:
            mygame()
        else:
            gameover()





