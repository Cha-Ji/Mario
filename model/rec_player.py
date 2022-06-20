import random

class RectPlayer:
    def __init__(self, rect, star, missile, SCREEN_SIZE):
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = SCREEN_SIZE

        self.recPlayer = rect
        self.recPlayer.centerx = (self.SCREEN_WIDTH / 2)
        self.recPlayer.centery = (self.SCREEN_HEIGHT / 2)

        self.recStar = self.__createRecStar(star)
        self.recMissile = self.__createRecMissile(missile)

        self.time_delay_500ms = 0

        self.isGameOver = False


    def __createRecStar(self, star):
        recStar = [None for i in range(len(star))]
        for i in range(len(star)):
            recStar[i] = star[i].get_rect()
            recStar[i].y = -1

        return recStar

    def __createRecMissile(self, missile):
        recMissile = [None for i in range(len(missile))]
        for i in range(len(missile)):
            recMissile[i] = missile[i].get_rect()
            recMissile[i].y = -1

        return recMissile

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
                self.recStar[i].y = -1

    def isCollisionMissile(self):
        for rec in self.recStar:
            if rec.y == -1:
                continue

            for recM in self.recMissile:
                if recM.y == -1:
                    continue
                if rec.top < recM.bottom \
                    and recM.top < rec.bottom \
                    and rec.left < recM.right \
                    and recM.left < rec.right:

                    rec.y = recM.y = 0
                    
                    return True

        return False

    def makeMissile(self):
        if self.isGameOver:
            return
        for i in range(len(self.recMissile)):
            if self.recMissile[i].y == -1:
                self.recMissile[i].x = self.recPlayer.x
                self.recMissile[i].y = self.recPlayer.y
                break

    def moveMissile(self):
        # self.makeMissile()
        for i in range(len(self.recMissile)):
            if self.recMissile[i].y == -1:
                continue
            if not self.isGameOver:
                self.recMissile[i].y -= 1
            if self.recMissile[i].y < 0:
                self.recMissile[i].y = -1

