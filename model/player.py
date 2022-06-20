IMG_PATH = "img/"

class Player:
    def __init__(self, pygame):
        self.player = pygame.image.load(IMG_PATH + 'player.png')
        self.player = pygame.transform.scale(self.player,(20,30))
