import pygame
import sys
import subprocess
import os
from pygame.locals import *

def G_snake():
    game_path = os.path.abspath("pygame-SJ/G_snake.py")
    subprocess.run([sys.executable, game_path])
    print("Selected Game: G_snake")


def G_avoid():
    game_path = os.path.abspath("pygame-SJ/G_avoid.py")
    subprocess.run([sys.executable, game_path])
    print("Selected Game: G_avoid")


def G_memoryGame():
    game_path = os.path.abspath("pygame-SJ/G_memoryGame.py")
    subprocess.run([sys.executable, game_path], check=True)
    print("Selected Game: G_memoryGame")


def display_text(screen, font, text, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main():
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Main Game")

    # 배경 이미지 로드
    background_image = pygame.image.load("image/common.jpeg")
    background_rect = background_image.get_rect()

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    games = [G_snake, G_avoid, G_memoryGame]
    selected_game = None

    while True:
        screen.blit(background_image, background_rect)

        game_names = ["Snake Game", "Avoid Game", "Memory Game"]
        for i, game_name in enumerate(game_names):
            text = font.render(game_name, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width // 2, 50 + i * 50))
            screen.blit(text, text_rect)

        display_text(screen, font, f"Press Q button to stop play", width // 2, height // 2,(255,0,0))
        display_text(screen, font, f"Selected Game: {selected_game}", width // 2, height - 50,(0,0,0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, game in enumerate(games):
                    text_rect = font.render(game_names[i], True, (0, 0, 0)).get_rect(center=(width // 2, 50 + i * 50))
                    if text_rect.collidepoint(x, y):
                        selected_game = game_names[i]
                        games[i]()
                        break
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()

        clock.tick(30)

if __name__ == "__main__":
    main()
    

'''
각 파일 연결하는 코드 

from G_baseballGame import baseballGame
from G_avoid import avoidGame
from G_memoryGame import memoryGame
from G_snake import snakeGame


memoryGame = memoryGame()
snakeGame = snakeGame()
avoidGame = avoidGame()

while memoryGame.running:
    memoryGame.game_loop()

'''