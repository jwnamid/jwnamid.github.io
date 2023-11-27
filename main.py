from G_baseballGame import baseballGame
#from G_avoid import avoidGame
#from G_snake import snakeGame
from G_memoryGame import memoryGame


g = baseballGame()

while g.running:
    g.curr_menu.display
    g.game_loop()