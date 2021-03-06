import random
import pkg_resources
import pygame


class Obstacle:

    def __init__(self, speed):
        """
        Initialize obstacle with random position.

        :param speed:
            Movement speed.
        """
        # load obstacle image
        image_path = pkg_resources.resource_filename('aaaaaa.resources.images', 'obstacle.png')
        self.__img = pygame.image.load(image_path)
        # obstacle position
        self.__x = random.sample([0, 1000], 1)[0]
        self.__y = random.randint(35, 800-35-26)
        # movement direction, moves right if obstacles starts at x=0 otherwise it moves left
        self.__move_left = self.__x != 0
        # movement speed
        self.__speed = speed

    @property
    def image(self):
        """
        Image of obstacle
        """
        return self.__img

    @property
    def pos(self):
        """
        Obstacle position
        """
        return self.__x, self.__y

    def move(self):
        """
        Update position depending on obstacle speed and direction.
        """
        self.__x += self.__speed * (not self.__move_left) - self.__speed * self.__move_left

    def out_of_bounds(self):
        """
        Check if obstacle is out of bounds.

        :return:
            True if obstacle is out of bound, False otherwise.
        """
        return self.__x < -26 or self.__x > 1000


