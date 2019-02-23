import random
import pkg_resources
import pygame


class Powerup:

    def __init__(self, color, ticks):
        """
        Initialize Powerup with random position.

        :param color:
            Powerup color.
        :param ticks:
            Number of ticks the powerup will stay until it is removed.
        """
        # load obstacle image
        image_path = pkg_resources.resource_filename('aaaaaa.resources.images', 'obstacle.png')
        self.__img = pygame.image.load(image_path)
        self.__color = color
        self.__img.fill((0, 0, 0, 255), None, pygame.BLEND_RGB_MULT)
        self.__img.fill(self.__color, None, pygame.BLEND_RGB_ADD)
        # position
        self.__x = random.randint(0, 1000 - 26)
        self.__y = random.randint(35, 800 - 35 - 26)
        # life time
        self.__ticks = ticks

    @property
    def image(self):
        """
        Image of powerup.
        """
        return self.__img

    @property
    def color(self):
        """
        Color of powerup.
        """
        return self.__color

    @property
    def pos(self):
        """
        Powerup position.
        """
        return self.__x, self.__y

    def decrease_ticks(self):
        """
        Decrease life time (ticks).

        :return:
            If remaining ticks are 0 return True else return False
        """
        self.__ticks -= 1
        return self.__ticks == 0
