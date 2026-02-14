from django.shortcuts import render
from django.http import HttpResponse

from connect4.board import Board
from connect4.marker import Marker


# Create your views here.
def home(request):
    return render(request, 'game/home.html')

def instruction(request):
    return render(request, 'game/instruction.html')

def leaderboard(request):
    return render(request, 'game/leaderboard.html')

def play(request):
    board = Board()
    board.move(3,Marker.FIRST_PLAYER)
    board.move(4,Marker.SECOND_PLAYER)
    context = {
        'board' : board.board
    }
    return render(request, 'game/play.html',context)
