import random

class RectPlayer:
    def __init__(self, rect, star, SCREEN_SIZE):
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = SCREEN_SIZE

        self.recPlayer = rect
        self.recPlayer.centerx = (self.SCREEN_WIDTH / 2)
        self.recPlayer.centery = (self.SCREEN_HEIGHT / 2)

        self.recStar = self.__createRecStar(star)

        self.time_delay_500ms = 0

        self.isGameOver = False


    def __createRecStar(self, star):
        recStar = [None for i in range(len(star))]
        for i in range(len(star)):
            recStar[i] = star[i].get_rect()
            recStar[i].y = -1

        return recStar

    def restart(self):
        for star in self.recStar:
            star.y = -1
        self.isGameOver = False

    def movePlayer(self, move):
        if not self.isGameOver:
            if 0 <= self.recPlayer.x + move.x < self.SCREEN_WIDTH - self.recPlayer.width:
                self.recPlayer.x += move.x

            if 0 <= self.recPlayer.y + move.y < self.SCREEN_HEIGHT - self.recPlayer.height:
                self.recPlayer.y += move.y

    def timeDelay500ms(self):
        if self.time_delay_500ms > 5:
            self.time_delay_500ms = 0
            return True    

        self.time_delay_500ms += 1
        return False

    def isCollision(self):
        for rec in self.recStar:
            if rec.y == -1:
                continue
            if rec.top < self.recPlayer.bottom \
                and self.recPlayer.top < rec.bottom \
                and rec.left < self.recPlayer.right \
                and self.recPlayer.left < rec.right:
                print('충돌')
                return True
        return False
 
    def makeStar(self):
        if self.isGameOver:
            return
        if self.timeDelay500ms():
            idex = random.randint(0, len(self.recStar)-1)
            if self.recStar[idex].y == -1:
                self.recStar[idex].x = random.randint(0, self.SCREEN_WIDTH)
                self.recStar[idex].y = 0

    def moveStar(self):
        self.makeStar()
        for i in range(len(self.recStar)):
            if self.recStar[i].y == -1:
                continue

            if not self.isGameOver:
                self.recStar[i].y += 1

            if self.recStar[i].y > self.SCREEN_HEIGHT:
                self.recStar[i].y = 0
 
