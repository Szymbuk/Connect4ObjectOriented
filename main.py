from connect4.agents.RandomAgent import RandomAgent
from connect4.agents.human_agent import HumanAgent
from connect4.board import Board
from connect4.game import Game
from connect4.marker import Marker
from connect4.observers.console_display import ConsoleDisplay
from connect4.player import Player


def main():
    plansza = Board()
    print(plansza)
    p1,p2 = Player(1,HumanAgent(plansza),Marker.FIRST_PLAYER), Player(2,RandomAgent(plansza),Marker.SECOND_PLAYER)
    game = Game(p1,p2,plansza)
    game.add_observer(ConsoleDisplay())
    game.run()



if __name__ == "__main__":
    main()



