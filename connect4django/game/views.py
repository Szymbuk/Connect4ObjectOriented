from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'game/home.html')

def instruction(request):
    return render(request, 'game/instruction.html')

def leaderboard(request):
    return render(request, 'game/leaderboard.html')

def play(request):
    return render(request, 'game/play.html')
