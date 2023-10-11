import sys
import pygame
from pygame.locals import *

# 출처 : https://wonhwa.tistory.com/44
BLACK = (0,0,0)
WHITE = (255,255,255)

## 게임 창 설정 ##
GameDisplay = pygame.display.set_mode((640,440))
GameDisplay.fill(WHITE) #하얀색으로 배경 채우기
pygame.display.set_caption("PYGAME Example") # 창 이름 설정

## 선(line) 및 도형 그리기 ##
# pointlist: 튜플형식으로 각 포인트(각)의 좌표를 설정
# start_point, end_point, centerpoint: 시작 좌표, 끝점, 가운데 좌표
# width: 도형 테두리 굵기 지정
"""
# 선
pygame.draw.line(surface, color, start_point, end_point, width)
pygame.draw.lines(surface, color, closed, pointlist, width)

# 면
pygame.draw.polygon(surface, color, pointlist, width)

# 원
pygame.draw.circle(surface, color, center_point, radius, width)
pygame.draw.line(GameDisplay,BLUE,(180,60),(220,60))

pygame.draw.rect(GameDisplay,RED,(300,20,50,50),2)

pygame.draw.ellipse(GameDisplay,GREEN,(400,20,80,50),2)



##Game loop 설정: 게임이 진행되는 동안 실행되는 이벤트(함수)들 만들기##

# 게임을 종료시키는 함수
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSec.tick(FPS)
