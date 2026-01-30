from connect4.agents.MoveAgent import MoveAgent


class HumanAgent(MoveAgent):


    def choose_move(self) -> int(1 - 7):
        move = int(input())
        return move