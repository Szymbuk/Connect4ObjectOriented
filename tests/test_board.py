import pytest

from connect4.board import Board
from connect4.marker import Marker
from connect4.player import Player


class TestBoard:

    class TestMove:
        @pytest.mark.parametrize("column,player_number",[(i,i%2) for i in range(0,7)])
        def test_move_empty_board(self,empty_board,player1,player2,column,player_number):
            players = [player1,player2]
            empty_board.choose_move()
            assert empty_board.board[5][column] == players[player_number].marker

        @pytest.mark.parametrize("column",[-1,-5,7,20])
        def test_move_out_of_bounds(self,empty_board,player1,column):
            with pytest.raises(ValueError):
                empty_board.choose_move()

        def test_multiple_moves_in_one_column(self,empty_board,player1,player2):
            empty_board.choose_move()
            empty_board.choose_move()
            empty_board.choose_move()
            empty_board.choose_move()
            empty_board.choose_move()
            empty_board.choose_move()

            assert empty_board.board[5][0] == 1
            assert empty_board.board[4][0] == 2
            assert empty_board.board[3][0] == 1
            assert empty_board.board[2][0] == 2
            assert empty_board.board[1][0] == 1
            assert empty_board.board[0][0] == 2


        def test_move_while_full_column(self,empty_board,player1,player2):
            empty_board.choose_move()
            empty_board.choose_move()
            empty_board.choose_move()
            empty_board.choose_move()
            empty_board.choose_move()
            empty_board.choose_move()

            with pytest.raises(ValueError):
                empty_board.choose_move()

    class TestWhoWon:

        class TestDiagonalWin:
            def test_trivial_win_board(self,empty_board,player1):
                empty_board.choose_move()
                empty_board.choose_move()
                empty_board.choose_move()
                empty_board.choose_move()
                empty_board.choose_move()
                empty_board.choose_move()
                empty_board.choose_move()
                empty_board.choose_move()
                empty_board.choose_move()
                empty_board.choose_move()


                assert empty_board._won_diagonally_upwards(5, 1) == True

            def test_false_on_almost_empty(self,empty_board,player1):
                empty_board.choose_move()

                assert empty_board._won_diagonally_upwards(5, 1) == False


        class TestHorizontalWin:
            pass
        class TestVerticalWin:
            pass

    class TestEndsGame:
        def test_trivial(self,empty_board):
            pass
        def test_diagonal_case(self,empty_board: Board):
            empty_board.move(1,Marker.SECOND_PLAYER)
            empty_board.move(2,Marker.FIRST_PLAYER)
            empty_board.move(2,Marker.SECOND_PLAYER)
            empty_board.move(3,Marker.SECOND_PLAYER)
            empty_board.move(3,Marker.FIRST_PLAYER)
            empty_board.move(3,Marker.SECOND_PLAYER)
            empty_board.move(4,Marker.FIRST_PLAYER)
            empty_board.move(4,Marker.SECOND_PLAYER)
            empty_board.move(4,Marker.FIRST_PLAYER)
            column, row = empty_board.move(4,Marker.SECOND_PLAYER)
            print(empty_board)
            assert empty_board.ends_game(row,column)


    def test__str__(self,empty_board):
        assert str(empty_board).strip() == """
    ┌─┬─┬─┬─┬─┬─┬─┬─┐
    │X│1│2│3│4│5│6│7│
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │1║ │ │ │ │ │ │ │
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │2║ │ │ │ │ │ │ │
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │3║ │ │ │ │ │ │ │
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │4║ │ │ │ │ │ │ │
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │5║ │ │ │ │ │ │ │
    ├─┼─┼─┼─┼─┼─┼─┼─┤
    │6║ │ │ │ │ │ │ │
    └─┴─┴─┴─┴─┴─┴─┴─┘""".strip()