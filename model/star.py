import random

from main import SCREEN_WIDTH, SCREEN_HEIGHT
from util.factory import Factory


class Star:

    def __init__(self):
        self.star = Factory().create_object_from_image('star')
        self.recStar = Factory().create_rect_object(self.star)
        self.delay = 0

    def __delay_star(self):
        if self.delay > 5:
            self.delay = 0
            return True

        else:
            self.delay += 1
            return False

    def make_star(self):
        if self.__delay_star():
            i = random.randint(0, len(self.recStar) - 1)
            if self.recStar[i].y == -1:
                self.recStar[i].x = random.randint(0, SCREEN_WIDTH)
                self.recStar[i].y = 0

    def __get_star_y(self, y):
        if y == -1:
            return y
        elif y >= SCREEN_HEIGHT:
            return -1
        else:
            return y + 1

    def move_star(self):
        self.make_star()
        for star in self.recStar:
            star.y = self.__get_star_y(star.y)
