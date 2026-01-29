import pytest

from connect4.board import Board
from connect4.marker import Marker
from connect4.player import Player


@pytest.fixture()
def empty_board():
    return Board()

@pytest.fixture()
def player1():
    return Player(1,1,Marker.FIRST_PLAYER)

@pytest.fixture()
def player2():
    return Player(1,1,Marker.SECOND_PLAYER)