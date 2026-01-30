from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from connect4.board import Board
from connect4.marker import Marker


class Player:
    """Class representing a player"""
    def __init__(self, player_id, moving_logic, marker: Marker):
        self.player = player_id
        self.marker = marker
        self.moving_logic = moving_logic


    def move(self,column:int,board: 'Board') -> tuple[int,int]:
        return board.move(column,self)


