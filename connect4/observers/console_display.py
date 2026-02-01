from connect4.board import Board
from connect4.marker import Marker
from connect4.observers.observer import Observer


class ConsoleDisplay(Observer):


    def print_error(self, message: str) -> None:
        print(message)

    def map_changed(self, board: 'Board',message: str) -> None:
        print(message)
        print(board)
        print("\n\n")

