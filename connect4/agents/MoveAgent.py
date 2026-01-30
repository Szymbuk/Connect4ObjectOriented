from abc import abstractmethod,ABC
from typing import List, TYPE_CHECKING

from connect4.marker import Marker
if TYPE_CHECKING:
    from connect4.board import Board



class MoveAgent(ABC):
    def __init__(self,board: 'Board'):
        self._valid_moves = None
        self.__board = board

    def _get_possible_moves(self) -> List[int]:
        columns = self.__board.get_numer_of_columns()
        results = []
        for column in range(columns):
            if self.__board.board[0][column] == Marker.EMPTY:
                results.append(column)
        return results


    @abstractmethod
    def choose_move(self):
        pass