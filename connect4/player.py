from connect4.agents.MoveAgent import MoveAgent
from connect4.marker import Marker


class Player:
    """Class representing a player_id"""
    def __init__(self, player_id, moving_logic: MoveAgent, marker: Marker):
        self._player_id = player_id
        self._marker = marker
        self._moving_logic = moving_logic


    def choose_move(self) -> int:
        return self._moving_logic.choose_move(self)

    @property
    def player_id(self):
        return self._player_id


    @property
    def marker(self):
        return self._marker

    @property
    def moving_logic(self):
        return self._moving_logic



