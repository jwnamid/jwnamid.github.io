from G_baseballGame import baseballGame
#from G_avoid import avoidGame
#from G_snake import snakeGame
#from G_memoryGame import memoryGame


endScene = baseballGame()

while g.running:
    g.playing = True
    g.game_loop()