from typing import Literal

from connect4.board import Board
from connect4.marker import Marker
from connect4.player import Player


class Game:
    """Class that represents a game between two players"""
    def __init__(self, player1:Player, player2:Player,board:Board):
        self.player1 = player1
        self.player2 = player2
        self.board = board


    def is_end(self) -> tuple[bool,Marker]:
        """
        Determines if the game has reached its end condition.

        The method checks if the board has a winner or if it is full, indicating
        the end of the game. If there is no winner, it evaluates the board's
        current state to determine if all positions are occupied.

        :returns: A tuple containing a boolean indicating whether the game has
            ended and the marker of the winner (if any).
        :rtype: tuple[bool, Marker]
        """
        marker = self.board.who_won()
        if marker == Marker.EMPTY:
            return self.board.is_full(),marker
        else:
            return True,marker
