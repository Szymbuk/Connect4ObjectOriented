import pytest

from connect4.agents.minmax_trivial_agent import MinmaxTrivialAgent
from connect4.board import Board
from connect4.marker import Marker
from connect4.player import Player


class TestMinmaxTrivialAgent:
    def test_choose_move(self):
        pass
        #assert False

    class TestCalculateMovePoints:

        def test_empty_board(self,empty_board: Board):
            minmax = MinmaxTrivialAgent(empty_board,1,False,)
            p1 = Player(1,minmax,Marker.FIRST_PLAYER)
            column = p1.choose_move()
            empty_board.move(column,p1.marker)
            print(empty_board)

        def test_perform_winning_move(self,empty_board: Board):
            chosen_column =1
            minmax = MinmaxTrivialAgent(empty_board,1,False,)
            p1 = Player(1,minmax,Marker.FIRST_PLAYER)
            empty_board.move(chosen_column,p1.marker)
            empty_board.move(chosen_column,p1.marker)
            empty_board.move(chosen_column,p1.marker)
            column = p1.choose_move()
            empty_board.move(column,p1.marker)
            assert column == chosen_column

        def test_blocks_opponents_winning_move(self,empty_board: Board):
            chosen_column =1
            minmax = MinmaxTrivialAgent(empty_board,1,False,)
            p1 = Player(1,minmax,Marker.FIRST_PLAYER)
            empty_board.move(chosen_column,Marker.SECOND_PLAYER)
            empty_board.move(chosen_column,Marker.SECOND_PLAYER)
            empty_board.move(chosen_column,Marker.SECOND_PLAYER)
            column = p1.choose_move()
            empty_board.move(column,p1.marker)
            print(empty_board)
            assert column == chosen_column

        @pytest.mark.parametrize("execution_number", range(1000))
        def test_not_making_move_which_lead_to_opponent_win(self,empty_board: Board,execution_number):
            print("number:",execution_number)
            wrong_column = 4
            minmax = MinmaxTrivialAgent(empty_board,1,False,)
            p1 = Player(1,minmax,Marker.FIRST_PLAYER)
            empty_board.move(1,Marker.SECOND_PLAYER)
            empty_board.move(2,Marker.FIRST_PLAYER)
            empty_board.move(2,Marker.SECOND_PLAYER)
            empty_board.move(3,Marker.SECOND_PLAYER)
            empty_board.move(3,Marker.FIRST_PLAYER)
            empty_board.move(3,Marker.SECOND_PLAYER)
            empty_board.move(4,Marker.FIRST_PLAYER)
            empty_board.move(4,Marker.SECOND_PLAYER)
            column = p1.choose_move()
            empty_board.move(column,p1.marker)

            assert column != wrong_column
            print("\n\n")



    def test__evaluate(self):
        pass
        #assert False
