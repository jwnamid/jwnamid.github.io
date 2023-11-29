import pygame
import sys
from pygame.locals import *

def G_snake():
    pygame.init()

    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("G_snake")

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while True:
        screen.fill((255, 255, 255))
        text = font.render("G_snake", True, (0, 0, 0))
        screen.blit(text, (150, 150))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(30)

def G_avoid():
    pygame.init()

    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("G_avoid")

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while True:
        screen.fill((255, 255, 255))
        text = font.render("G_avoid", True, (0, 0, 0))
        screen.blit(text, (150, 150))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(30)

def G_memoryGame():
    pygame.init()

    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("G_memoryGame")

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while True:
        screen.fill((255, 255, 255))
        text = font.render("G_memoryGame", True, (0, 0, 0))
        screen.blit(text, (150, 150))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(30)



def main():
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Main Game")

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    games = [G_snake, G_avoid, G_memoryGame]
    selected_game = 0

    while True:
        screen.fill((255, 255, 255))

        for i, game in enumerate(games):
            text = font.render(f"Game {i + 1}", True, (0, 0, 0))
            screen.blit(text, (width // 2 - 50, 50 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    selected_game = (selected_game - 1) % len(games)
                elif event.key == K_DOWN:
                    selected_game = (selected_game + 1) % len(games)
                elif event.key == K_RETURN:
                    # 선택된 게임 실행
                    games[selected_game]()

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