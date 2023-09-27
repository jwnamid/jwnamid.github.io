import sys
import pygame
import random
from pygame.locals import *

pygame.init()
WIDTH = 800
HEIGHT = 1000
screen = pygame.display.set_mode([WIDTH, HEIGHT])
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption('Say Number')

class Button:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled

    def draw(self):
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (200,25))
        pygame.draw.rect(screen, 'gray', button_rect, 0,5)





run = True
while run:
    screen.fill('white')
    timer.tick(fps)
    my_button = Button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
