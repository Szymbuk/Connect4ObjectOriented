from enum import Enum, IntEnum
class Marker(IntEnum):
    FIRST_PLAYER = 1
    SECOND_PLAYER = 2
    EMPTY = 0

    def __str__(self):
        symbols = {Marker.FIRST_PLAYER : 'O', Marker.SECOND_PLAYER : 'X',Marker.EMPTY :' '}
        return symbols[self]


