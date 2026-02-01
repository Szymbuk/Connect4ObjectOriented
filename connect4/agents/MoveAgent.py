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
        return [i for i in range(0,columns) if self.__board.board[0][i] == Marker.EMPTY]


    @abstractmethod
    def choose_move(self) -> int(0-6):
        """
        Abstract method that enforces the implementation of a specific method
        to choose a move. This method is designed to be overridden by
        subclasses, mandating them to define their logic for selecting a move
        within a specified range.

        :raises NotImplementedError: If the method is not implemented in the
            subclass that inherits this abstract method.
        :returns: An integer representing the chosen move, constrained to the
            range of 1 to 7.
        :rtype: int
        """

        pass