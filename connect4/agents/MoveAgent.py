from __future__ import annotations
from abc import abstractmethod,ABC
from typing import List, TYPE_CHECKING

from connect4.marker import Marker


if TYPE_CHECKING:
    from connect4.board import Board
    from connect4.player import Player



class MoveAgent(ABC):
    def __init__(self,board: Board):
        self._valid_moves = None
        self._board = board

    def _get_possible_moves(self) -> List[int]:
        columns = self._board.numer_of_columns
        return [column for column in range(0, columns) if not self._board.is_column_full(column)]


    @abstractmethod
    def choose_move(self,player: Player) -> int:
        pass