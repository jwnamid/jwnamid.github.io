import pygame # 파이게임 라이브러리 불러옴
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
character = pygame.image.load("C:/git-workspace/pygame-SJ/player_small.png:")
enemy = pygame.image.load("C:/git-workspace/pygame-SJ/enemy_small.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

enemy_x_pos = random.randint(0, (screen_width - character_width))
enemy_y_pos = 0

to_x = 0
to_y = 0

character_speed = 0.5
enemy_speed = 1

game_over_font = pygame.font.Font(None, 100)
game_font = pygame.font.Font(None, 40)

start_ticks = pygame.time.get_ticks()
avoid_enemies = 0

