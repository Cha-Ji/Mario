from main import SCREEN_WIDTH, SCREEN_HEIGHT
from util.factory import Factory


class Player:
    def __init__(self, move):
        self.move = move
        self.player = Factory().create_player()
        self.recPlayer = Factory().create_rect_player(self.player)

    def move_player(self):
        if 0 <= self.recPlayer.x + self.move.x < SCREEN_WIDTH - self.recPlayer.width:
            self.recPlayer.x += self.move.x

        if 0 <= self.recPlayer.y + self.move.y < SCREEN_HEIGHT - self.recPlayer.height:
            self.recPlayer.y += self.move.y

    def event_process(self, x, y, swt):
        self.move.x = -1 if 0 <= x < 500 else 0 if 500 <= x < 520 else 1
        self.move.y = -1 if 0 <= y < 500 else 0 if 500 <= x < 520 else 1
