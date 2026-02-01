from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from connect4.marker import Marker

if TYPE_CHECKING:
    from connect4.board import Board


class Observer(ABC):

    @abstractmethod
    def map_changed(self,board: 'Board',message: str) -> None:
        pass

    @abstractmethod
    def print_error(self,message: str) -> None:
        pass




