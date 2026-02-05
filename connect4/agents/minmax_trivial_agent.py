from __future__ import annotations
from typing import TYPE_CHECKING, List
import numpy as np
import random
import math

from connect4.agents.MoveAgent import MoveAgent

if TYPE_CHECKING:
    from connect4.board import Board
    from connect4.marker import Marker
    from connect4.player import Player

class MinmaxTrivialAgent(MoveAgent):

    def __init__(self, board: Board, depth: int, pruning: bool):
        self._depth = depth
        self._pruning = pruning
        super().__init__(board)

    def choose_move(self, maxing_player: Player) -> int:
        current_depth = 0
        results = self._calculate_move_points(current_depth, maxing_player.marker, maxing_player)
        best_moves = [column for column in range(self._board.numer_of_columns) if results[column] == max(results)]
        return random.choice(best_moves)

    def _calculate_move_points(self, current_depth: int, current_marker: Marker, maxing_player: Player) -> np.ndarray:
        if current_marker == maxing_player.marker:
            player_coefficient = 1
        else:
            player_coefficient = -1

        results = np.zeros(self._board.numer_of_columns)
        for column in range(self._board.numer_of_columns):
            if self._board.is_column_full(column):
                results[column] = -math.inf*player_coefficient
                continue

            column, row  = self._board.move(column, current_marker)
            if self._board.ends_game(row, column):
                results[column] = math.inf*player_coefficient
            elif current_depth < self._depth:
                next_marker = current_marker.opposite()
                partial_res = self._calculate_move_points(current_depth + 1, next_marker, maxing_player)
                if current_marker == maxing_player.marker:
                    # Logic reverse is a necessity. A maxing player gets results from minimalizing player, which would choose an option the best for himself.
                    results[column] = min(partial_res)
                else:
                    results[column] = max(partial_res)
            else:
                results[column] = self._evaluate()*player_coefficient
            self._board.reverse_move(column, current_marker)
        return results

    def _evaluate(self) -> int:
        return 0
