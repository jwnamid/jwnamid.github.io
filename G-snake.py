# Make G-snake.py
import pygame

#게임 화면의 크기, 색상 등을 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)   

display_width = 600
display_height = 400

dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

#뱀과 먹이를 정의
snake_block = 10
snake_speed = 15
x1 = display_width / 2
y1 = display_height / 2
x1_change = 0
y1_change = 0
snake_List = []
Length_of_snake = 1

foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
