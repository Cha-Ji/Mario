class Game:

    def __init__(self):
        self.isGameOver = False

    def restart(self, recStar):
        for star in recStar:
            star.y = -1
        self.isGameOver = False

    def __is_collision(self, me, target):
        return me.top < target.bottom and me.bottom > target.top and me.left < target.right and me.right > target.left

    def check_collision_star(self, recStar, recPlayer):
        for rec in recStar:
            if rec.y == -1:
                continue
            if self.__is_collision(rec, recPlayer):
                self.isGameOver = True
                break

    def check_collision_missile(self, recStar, recMissile):
        for rec in recStar:
            if rec.y == -1:
                continue

            for recM in recMissile:
                if recM.y == -1:
                    continue

                if self.__is_collision(rec, recM):
                    rec.y = recM.y = 0
                    return
        return
