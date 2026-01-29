from connect4.marker import Marker


class Player:
    """Class representing a player"""
    def __init__(self, player_id, moving_logic, marker: Marker):
        self.player = player_id
        self.marker = marker
        self.moving_logic = moving_logic
