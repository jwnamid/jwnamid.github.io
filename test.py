import sys
import pygame
from pygame.locals import *

class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
        self.buttons = [
            {"text": "Avoid Game", "function": self.run_avoid_game},
            {"text": "Snake Game", "function": self.run_snake_game},
            {"text": "Memory Game", "function": self.run_memory_game},
            {"text": "Baseball Game", "function": self.run_baseball_game}
        ]
        self.button_rects = []

    def draw_cursor(self):
        self.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def draw_buttons(self):
        for i, button_rect in enumerate(self.button_rects):
            pygame.draw.rect(self.game.display, (255, 255, 255), button_rect, 2)
            self.draw_text(self.buttons[i]["text"], 20, button_rect.centerx, button_rect.centery)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.game.display.blit(text_surface, text_rect)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.draw_text('Main Menu', 20, self.mid_w, self.mid_h - 20)

            # Set button positions
            button_width, button_height = 200, 50
            button_start_y = self.mid_h
            spacing = 10

            self.button_rects = []
            for i, button in enumerate(self.buttons):
                button_x = self.mid_w - button_width / 2
                button_y = button_start_y + (button_height + spacing) * i
                button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
                self.button_rects.append(button_rect)

            self.draw_buttons()
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            self.cursor_rect.y += 1
            if self.cursor_rect.y >= len(self.button_rects):
                self.cursor_rect.y = 0
        elif self.game.UP_KEY:
            self.cursor_rect.y -= 1
            if self.cursor_rect.y < 0:
                self.cursor_rect.y = len(self.button_rects) - 1

        self.cursor_rect.midtop = (self.button_rects[self.cursor_rect.y].centerx + self.offset,
                                   self.button_rects[self.cursor_rect.y].centery)

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            self.buttons[self.cursor_rect.y]["function"]()

        elif self.game.ESC_KEY:
            self.run_exit_game()

    def run_avoid_game(self):
        print("Running Avoid Game...")  # 여기에 원하는 동작을 추가하십시오.

    def run_snake_game(self):
        print("Running Snake Game...")  # 여기에 원하는 동작을 추가하십시오.

    def run_memory_game(self):
        print("Running Memory Game...")  # 여기에 원하는 동작을 추가하십시오.

    def run_baseball_game(self):
        print("Running Baseball Game...")  # 여기에 원하는 동작을 추가하십시오.

    def run_exit_game(self):
        print("Exiting the game...")  # 여기에 원하는 동작을 추가하십시오.
        self.run_display = False

class Game:
    def __init__(self):
        pygame.init()
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.display = pygame.Surface((400, 300))
        self.clock = pygame.time.Clock()
        self.running = True
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.ESC_KEY = False, False, False, False

    def game_loop(self):
        main_menu = Menu(self)
        while self.running:
            self.check_events()
            self.window.fill((0, 0, 0))
            self.display.fill((0, 0, 0))
            main_menu.display_menu()
            self.window.blit(self.display, (200, 150))
            pygame.display.flip()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC_KEY = True

        main_menu_buttons = getattr(self, 'main_menu_buttons', None)
        if main_menu_buttons is not None:
            for button in main_menu_buttons:
                button.check_events()

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.ESC_KEY = False, False, False, False

if __name__ == "__main__":
    game = Game()
    game.game_loop()