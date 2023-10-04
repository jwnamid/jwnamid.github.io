import pygame git check # 파이게임 라이브러리 불러옴
import random

pygame.init() #초기화

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("낙하물 피하기")

# FPS
clock = pygame.time.Clock()

# 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:/git-workspace/pygame-SJ/back.png")
character = pygame.image.load("C:/git-workspace/pygame-SJ/player_small.png:)
enemy = pygame.image.load("C:/git-workspace/pygame-SJ/enemy_small.png")

