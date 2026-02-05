from connect4.agents.MoveAgent import MoveAgent


class HumanAgent(MoveAgent):


    def choose_move(self,player = None) -> int:
        try:
            move = int(input("Podaj numer kolumny z zakresu 1-7: "))
        except:
            raise ValueError("Podana wartość nie jest liczbą.")
        return move -1