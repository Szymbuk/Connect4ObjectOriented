import random

from connect4.agents.MoveAgent import MoveAgent


class RandomAgent(MoveAgent):
    """Class that implements a random agent"""

    def choose_move(self):
        return random.choice(self._get_possible_moves())+1

