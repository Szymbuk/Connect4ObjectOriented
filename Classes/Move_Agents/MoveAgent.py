from abc import abstractmethod,ABC


class MoveAgent(ABC):
    def __init__(self,board):
        self._valid_moves = None
        self.__board = board
    @abstractmethod
    def __get_possible_moves(self):
        pass

    @abstractmethod
    def make_move(self):
        pass