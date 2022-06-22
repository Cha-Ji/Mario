import pygame.display
from pygame.rect import *

from main import SWITCH, vrx_channel, vry_channel, swt_channel, SCREEN_HEIGHT, SCREEN_WIDTH
from model.missile import Missile
from model.player import Player
from model.referee import Referee
from model.star import Star

from model.joystick import Joystick
import RPi.GPIO as GPIO


class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.joystick = Joystick()
        self.player = Player(Rect(0, 0, 0, 0))
        self.star = Star()
        self.missile = Missile()
        self.referee = Referee()

        self.isGameOver = False
        self.score = 0

    def __get_read_channels(self):
        return (self.joystick.read_channel(vrx_channel),
                self.joystick.read_channel(vry_channel),
                self.joystick.read_channel(swt_channel))

    def __move_player(self):
        self.player.move_player()
        self.screen.blit(self.player.player, self.player.recPlayer)

    def __move_star(self):
        self.star.move_star()
        for i in range(len(self.star.star)):
            self.screen.blit(self.star.star[i], self.star.recStar[i])

    def __move_missile(self):
        self.missile.move_missile()
        for i in range(len(self.missile.missile)):
            self.screen.blit(self.missile.missile[i], self.missile.recMissile[i])

    def __restart(self):
        for star in self.star.recStar:
            star.y = -1

    def move_object(self):
        self.screen.fill((0, 0, 0))
        vrx_pos, vry_pos, swt_val = self.__get_read_channels()
        self.player.event_process(vrx_pos, vry_pos, swt_val)

        if GPIO.input(SWITCH) == 0:
            self.missile.make_missile(self.player.recPlayer)

        self.__move_player()
        self.__move_star()
        self.__move_missile()

        self.referee.check_collision_star(recStar=self.star.recStar, recPlayer=self.player.recPlayer)
        self.referee.check_collision_missile(recStar=self.star.recStar, recMissile=self.missile.recMissile)

        if self.referee.isGameOver:
            self.__restart()
            self.isGameOver = True

        self.score += 1
