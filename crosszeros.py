from inspect import ArgInfo

import pygame
from enum import Enum

from cross_zero.model import GameField, Player, HumanPlayer

FPS = 60
CELL_SIZE = 50


class GameFieldView:
    """
    Виджет игрового поля, который отображает его на экране, а также выясняет место клика.
    """
    def __init__(self, field):
        # Загрузить картинки значков клеток...
        # Отобразить первичное состояние поля
        self.field = field
        self.height = field.height * CELL_SIZE
        self.width  = field.width * CELL_SIZE

    def draw(self):
        pass

class ChoosePlayersManager:
    """
    Менеджер игры, запускающий все игровые процессы
    """
    pass

class GameRoundManager:
    """
    Менеджер игры, запускающий все игровые процессы
    """
    def __init__(self, player1: Player, player2: Player):
        self.players = [player1, player2]
        self.current_player_index = 0
        self.field = GameField

    def handle_click (self, i, j):
        player = self.players[self.current_player_index]
        # Игрок делает клик на поле
        print("Click_handled", i, j)

class GameWindow:
    """
    Содержит виджет поля,
    а также менеджера игрового раунда.
    """

    def __init__(self):
        # инициализация pygame

        pygame.init()

        self.width = 800
        self.height = 600
        self.title = "Crosses & Zeroes"
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        player1 = HumanPlayer(Cell.CROSS)
        player2 = AIPlayer(Cell.ZERO)
        self.game_manager = GameRoundManager(player1, player2)
        self.field_widjet = GameFieldView(self.game_manager.field)

    def main_loop(self):
        pass

def main()
    pass


if __name__ == "__main__":
    main()

