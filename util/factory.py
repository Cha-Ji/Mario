from main import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame


class Factory:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Factory, cls).__new__(cls)

        return cls.instance

    def create_player(self):
        player = pygame.image.load('img/player.png')
        player = pygame.transform.scale(player, (20, 30))
        return player

    def create_rect_player(self, player):
        recPlayer = player.get_rect()
        recPlayer.centerx = (SCREEN_WIDTH / 2)
        recPlayer.centery = (SCREEN_HEIGHT / 2)
        return recPlayer

    def create_rect_object(self, object):
        recObject = [None for _ in range(len(object))]
        for i in range(len(object)):
            recObject[i] = object[i].get_rect()
            recObject[i].y = -1

        return recObject

    def create_object_from_image(self, name):
        object = [pygame.image.load('img/' + name + '.png') for _ in range(40)]
        for i in range(len(object)):
            object[i] = pygame.transform.scale(object[i], (20, 20))
        return object
