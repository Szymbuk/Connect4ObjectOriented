import numpy as np
import matplotlib

from connect4.marker import Marker
from connect4.player import Player


class Board:
    """Class representing a board"""
    def __init__(self):
        self.__number_of_columns = 7
        self.__number_of_rows = 6
        self.board= np.zeros((self.__number_of_rows, self.__number_of_columns))


    def move(self, column: int,player: Player):
        if not 1<=column<=7:
            raise ValueError("Niedozwolony ruch. Numer kolumny powinien być z zakresu 1-7")
        true_column = column-1

        if self.board[0][true_column] != Marker.EMPTY:
            raise ValueError("Niedozwolony ruch. Kolumna jest pełna")

        for row in range(self.__number_of_rows - 1, -1, -1):
            if self.board[row][true_column] == Marker.EMPTY:
                self.board[row][true_column] = player.marker
                return
        raise RuntimeError("Błąd metody wykonującej ruch")





    def __str__(self):
        symbols = {Marker.FIRST_PLAYER : 'O', Marker.SECOND_PLAYER : 'X',Marker.EMPTY :' '}
        data = {}
        for i in range(self.__number_of_rows):
            for j in range(self.__number_of_columns):
                if self.board[i][j] == 1:
                    data['c{}_{}'.format(i + 1, j + 1)] = symbols[Marker.FIRST_PLAYER]
                if self.board[i][j] == 2:
                    data['c{}_{}'.format(i + 1, j + 1)] = symbols[Marker.SECOND_PLAYER]
                if self.board[i][j] == 0:
                    data['c{}_{}'.format(i + 1, j + 1)] = symbols[Marker.EMPTY]
        szablon = """
    ┌─┬─┬─┬─┬─┬─┬─┬─┐
    │X│1│2│3│4│5│6│7│
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │1║{c1_1:^1}│{c1_2:^1}│{c1_3:^1}│{c1_4:^1}│{c1_5:^1}│{c1_6:^1}│{c1_7:^1}│
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │2║{c2_1:^1}│{c2_2:^1}│{c2_3:^1}│{c2_4:^1}│{c2_5:^1}│{c2_6:^1}│{c2_7:^1}│
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │3║{c3_1:^1}│{c3_2:^1}│{c3_3:^1}│{c3_4:^1}│{c3_5:^1}│{c3_6:^1}│{c3_7:^1}│
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │4║{c4_1:^1}│{c4_2:^1}│{c4_3:^1}│{c4_4:^1}│{c4_5:^1}│{c4_6:^1}│{c4_7:^1}│
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │5║{c5_1:^1}│{c5_2:^1}│{c5_3:^1}│{c5_4:^1}│{c5_5:^1}│{c5_6:^1}│{c5_7:^1}│
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │6║{c6_1:^1}│{c6_2:^1}│{c6_3:^1}│{c6_4:^1}│{c6_5:^1}│{c6_6:^1}│{c6_7:^1}│
    └─┴─┴─┴─┴─┴─┴─┴─┘
    """
        return szablon.format(**data)
