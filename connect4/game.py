from typing import Literal

from connect4.board import Board
from connect4.marker import Marker
from connect4.observers.observer import Observer
from connect4.player import Player


class Game:
    """Class that represents a game between two players"""
    def __init__(self, player1:Player, player2:Player,board:Board):
        self._player1 = player1
        self._player2 = player2
        self._observers = []
        self._board = board



    def run(self):
        current_player = self._player1
        while not self.is_end()[0]:
            while True:
                try:
                    place = current_player.move(self._board)
                    break
                except ValueError as position_error:
                    self.print_error(position_error)
            message = f"Tura gracza {current_player.player} ({str(current_player.marker)}). Wykonano ruch na pole {place[0]+1},{place[1]+1}"
            self.notify_observers(message)
            if current_player == self._player1:
                current_player = self._player2
            else:
                current_player = self._player1

    def notify_observers(self,message: str):
        for observer in self._observers:
            observer.map_changed(self._board,message)

    def print_error(self,error):
        for observer in self._observers:
            observer.print_error(error)

    def add_observer(self,observer: Observer):
        self._observers.append(observer)


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
        marker = self._board.who_won()
        if marker == Marker.EMPTY:
            return self._board.is_full(),marker
        else:
            return True,marker
