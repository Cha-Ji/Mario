from util.factory import Factory

IMG_PATH = 'img/'

class Missile:

    def __init__(self, missile):
        self.recMissile = Factory().create_rect_object(missile)

    def make_missile(self, recPlayer, isGameOver):
        if isGameOver:
            return
        for i in range(len(self.recMissile)):
            if self.recMissile[i].y == -1:
                self.recMissile[i].x = recPlayer.x
                self.recMissile[i].y = recPlayer.y
                break

    def move_missile(self, isGameOver):
        for i in range(len(self.recMissile)):
            if self.recMissile[i].y == -1:
                continue
            if not isGameOver:
                self.recMissile[i].y -= 1
            if self.recMissile[i].y < 0:
                self.recMissile[i].y = -1
