import numpy as np
import matplotlib

from Classes.Marker import Marker


class Board:
    """Class representing a board"""
    def __init__(self,number_of_rows,number_of_columns):
        self.board= np.zeros(number_of_columns,number_of_rows)




    def __str__(self):
        symbols = {Marker.FIRST_PLAYER : 'O', Marker.SECOND_PLAYER : 'X',Marker.EMPTY :' '}
        data = {}
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:
                    data['c{}_{}'.format(i + 1, j + 1)] = 'X'
                if self.board[i][j] == 2:
                    data['c{}_{}'.format(i + 1, j + 1)] = 'O'
                if self.board[i][j] == 0:
                    data['c{}_{}'.format(i + 1, j + 1)] = ''
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
