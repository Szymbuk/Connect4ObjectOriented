from typing import TYPE_CHECKING

from connect4.agents.MoveAgent import MoveAgent

if TYPE_CHECKING:
    from connect4.board import Board
from connect4.marker import Marker


class Player:
    """Class representing a player"""
    def __init__(self, player_id, moving_logic: MoveAgent, marker: Marker):
        self.player = player_id
        self.marker = marker
        self.moving_logic = moving_logic


    def move(self,board: 'Board') -> tuple[int,int]:
        column = self.moving_logic.choose_move()
        return board.move(column,self)


