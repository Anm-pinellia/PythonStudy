import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('E:\pygamestudy\sound\BG.ogg')
volume = 0.2
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play()
print('测试音乐开始播放\n')

M1_sound = pygame.mixer.Sound('E:\pygamestudy\sound\M1.wav')
M1_sound.set_volume(volume)
M2_sound = pygame.mixer.Sound('E:\pygamestudy\sound\M2.wav')
M2_sound.set_volume(volume)

bg_size = width, height = 600, 300
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('测试音乐播放')

pause = False

pause_image = pygame.image.load('E:\\pygamestudy\\sound\\pause.png').convert_alpha()
unpause_image = pygame.image.load('E:\\pygamestudy\\sound\\unpause.png').convert_alpha()
pause_rect = pause_image.get_rect()
pause_rect.left, pause_rect.top = (width - pause_rect.width)//2, (height - pause_rect.height)//2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                M1_sound.play()
            if event.button == 3:
                M2_sound.play()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                print('播放状态转换')
                pause = not pause

    screen.fill((255,255,255))

    if pause:
        screen.blit(pause_image,pause_rect)
        pygame.mixer.music.pause()
    else:
        screen.blit(unpause_image,pause_rect)
        pygame.mixer.music.unpause()

    pygame.display.flip()

    clock.tick(30)

                
            
