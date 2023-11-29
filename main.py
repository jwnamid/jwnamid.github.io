from G_baseballGame import baseballGame
from G_avoid import avoidGame
from G_memoryGame import memoryGame
from G_snake import snakeGame


memoryGame = memoryGame()
snakeGame = snakeGame()
avoidGame = avoidGame()

while memoryGame.running:
    memoryGame.game_loop()
