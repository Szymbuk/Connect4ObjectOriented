from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE, ForeignKey


# Create your models here.
class Player(models.Model):
    played_games = models.IntegerField()
    won_games = models.IntegerField()

    def is_human(self) -> bool:
        return hasattr(self, 'humanplayer')

    def is_bot(self) -> bool:
        return hasattr(self, 'gameengine')


class HumanPlayer(Player):
    user = models.OneToOneField(User, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.user.username


class GameEngine(Player):
    AGENT_CHOICES =[
        ('RANDOM', 'random agent'),
        ('MINMAX1', 'minmax agent 1'),
        ('MINMAX2', 'minmax agent 2'),
        ('MINMAX3', 'minmax agent 3'),
        ('MINMAX4', 'minmax agent 4'),
        ('MINMAX5', 'minmax agent 5'),
        #('MCTS1', 'monte carlo tree search agent 1'),
        #('MCTS2', 'monte carlo tree search agent 2'),
        #('MCTS3', 'monte carlo tree search agent 3'),
    ]
    engine_name = models.CharField(choices=AGENT_CHOICES, default='RANDOM')

    def __str__(self)-> str:
        return self.engine_name


class Game(models.Model):
    active = models.BooleanField(default=True)
    board_state = models.JSONField(default=list)
    player1 = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='game_as_first_player')
    player2 = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='game_as_second_player')

