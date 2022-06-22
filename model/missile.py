from util.factory import Factory


class Missile:

    def __init__(self):
        self.missile = Factory().create_object_from_image('missile')
        self.recMissile = Factory().create_rect_object(self.missile)

    def make_missile(self, recPlayer):
        for missile in self.recMissile:
            if missile.y == -1:
                missile.x, missile.y = recPlayer.x, recPlayer.y
                break

    def __get_missile_y(self, y):
        if y == -1:
            return y
        elif y >= 0:
            return y - 1
        else:
            return -1

    def move_missile(self):
        for missile in self.recMissile:
            missile.y = self.__get_missile_y(missile.y)
