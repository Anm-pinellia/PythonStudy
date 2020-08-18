import pygame
import sys
import math
from pygame.locals import *
from random import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self):
        self.rect = self.rect.move(self.speed)

        if self.rect.right<0:
            self.rect.left = self.width

        elif self.rect.left> self.width:
            self.rect.right = 0

        elif self.rect.bottom < 0:
            self.rect.top = self.height

        elif self.rect.top > self.height:
            self.rect.bottom = 0

def collide_check(item, balls):
    col_balls = []
    for each in balls:
        distance = math.sqrt(\
            math.pow((item.rect.center[0] - each.rect.center[0]),2)+
            math.pow((item.rect.center[1] - each.rect.center[1]),2))
        if distance <= (item.rect.width + each.rect.width)/2:
            col_balls.append(each)

    return col_balls
            

def main():
    pygame.init()

    ball_image = "E:\\pygamestudy\\gray_ball.png"
    bg_image = "E:\\pygamestudy\\background.png"

    running = True

    #添加背景音乐
    pygame.mixer.music.load('E:\pygamestudy\sound\BG.ogg')
    volume = 0.2
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

    #添加音效
    loser_sound = pygame.mixer.Sound('E:\pygamestudy\sound\M1.wav')
    loser_sound.set_volume(volume)
    winner_sound = pygame.mixer.Sound('E:\pygamestudy\sound\M2.wav')
    winner_sound.set_volume(volume)

    #音乐播放完时的自定义事件
    GameOver = USEREVENT
    pygame.mixer.music.set_endevent(GameOver)
    
    #设置窗口大小
    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("球的小游戏")

    background = pygame.image.load(bg_image).convert_alpha()

    balls = []

    #创建小球数量
    BALL_NUM = 5

    for i in range(BALL_NUM):
        position = randint(0, width-100), randint(0, height-100)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(ball_image, position, speed, bg_size)
        while collide_check(ball, balls):
            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)
        balls.append(ball)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == GameOver:
                loser_sound.play()
                pygame.time.delay(2000)
                running = False

        screen.blit(background, (0,0))       #进行blit绘制

        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)

        #如果发生碰撞则处理
        for i in range(BALL_NUM):
            item = balls.pop(i)

            if collide_check(item, balls):      #如果返回的列表中有内容则执行
                item.speed[0] = -item.speed[0]
                item.speed[1] = -item.speed[1]
            balls.insert(i, item)

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
