IMG_PATH = "img/"

class Star:
    def createStar(self, pygame):
        star = [pygame.image.load(IMG_PATH + 'star.png') for i in range(40)]
        for i in range(len(star)):
            star[i] = pygame.transform.scale(star[i], (20, 20))
        return star
