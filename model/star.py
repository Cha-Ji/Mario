import random

from main import SCREEN_WIDTH, SCREEN_HEIGHT
from util.factory import Factory

IMG_PATH = "img/"


class Star:

    def __init__(self, star):
        self.recStar = Factory().create_rect_object(star)
        self.delay = 0

    def __delay_star(self):
        if self.delay > 5:
            self.delay = 0
            return True

        else:
            self.delay += 1
            return False

    def make_star(self, isGameOver):
        if isGameOver:
            return
        if self.__delay_star():
            i = random.randint(0, len(self.recStar) - 1)
            if self.recStar[i].y == -1:
                self.recStar[i].x = random.randint(0, SCREEN_WIDTH)
                self.recStar[i].y = 0

    def move_star(self, isGameOver):
        self.make_star(isGameOver)
        for i in range(len(self.recStar)):
            if self.recStar[i].y == -1:
                continue

            if not isGameOver:
                self.recStar[i].y += 1

            if self.recStar[i].y > SCREEN_HEIGHT:
                self.recStar[i].y = -1
