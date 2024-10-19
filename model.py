import pygame
from enum import Enum

class CELL(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2

class GameField:
    height = 3
    width = 3

    def __init__(self):
        self.cells = [[CELL.VOID]*GameField.width for i in range(GameField.height)]

class PlayerType(Enum):
    HUMAN = 0
    AI = 1


class Player:
    """
    Класс игрока, содержащий тип значков и информацию об игроке: человек или комп.
    Создала класс, в котором два аттрибута: player_type, cell_type.
    """

    def __init__(self, player_type: PlayerType, cell_type: CELL):
        self.player_type = player_type
        self.cell_type = cell_type

class HumanPlayer(Player):
    """
    Класс игрока человека
    """
    def __init__(self, cell_type: CELL):
        super(Player).__init__(PlayerType.HUMAN, cell_type)


class AI(Player):
    """
    Класс игрока AI
    """

    def __init__(self, cell_type: CELL):
        super(Player).__init__(PlayerType.AI, cell_type)

    def choose_cell(self, field):


