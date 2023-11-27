from G_baseballGame import baseballGame
#from G_avoid import avoidGame
from G_snake import snakeGame
from G_memoryGame import memoryGame


g = snakeGame()

while g.running:
    g.game_loop()

    