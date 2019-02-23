import pkg_resources
import pygame


class Player:

    def __init__(self, x, y):
        """
        Create player object.

        :param x:
            Start position X
        :param y:
            Start position Y
        """
        # load player image
        image_path = pkg_resources.resource_filename('aaaaaa.resources.images', 'player.png')
        self.__img = pygame.image.load(image_path)
        # player position
        self.__x = x
        self.__y = y
        # player still alive?
        self.__dead = False
        # movement variables
        self.__move_up = True
        self.__move_right = False
        self.__move_left = False
        # movement speed
        self.__speed = 10
        # extra lives
        self.__extra_lives = 0
        # shield
        self.__shield = False
        # bombs
        self.__bombs = 0

    @property
    def bombs(self):
        """
        Number of available bombs.
        """
        return self.__bombs

    @property
    def dead(self):
        """
        Is player dead?
        """
        return self.__dead

    @property
    def shield(self):
        """
        Is shield activated?
        """
        return self.__shield

    @property
    def move_up(self):
        """
        Does player move upwards?
        """
        return self.__move_up

    @property
    def move_left(self):
        """
        Does player move left?
        """
        return self.__move_left

    @property
    def move_right(self):
        """
        Does player move right?
        """
        return self.__move_right

    @property
    def pos(self):
        """
        Player's current position
        """
        return self.__x, self.__y

    @property
    def image(self):
        """
        Image of player.
        """
        return self.__img

    @property
    def extra_lives(self):
        """
        Number of extra lives.
        """
        return self.__extra_lives

    def oneup(self):
        """
        Increase extra lives by 1.
        """
        self.__extra_lives += 1

    def onedown(self):
        """
        Decrease extra lives by 1.
        """
        self.__extra_lives -= 1

    def flip(self):
        """
        Changes move_up to False if True and vice versa.
        """
        self.__move_up = not self.__move_up
        self.__img = pygame.transform.rotate(self.__img, 180)

    def set_move_left(self, b):
        """
        Changes move_left given Boolean b.

        :param b: Boolean.
        """
        self.__move_left = b

    def set_move_right(self, b):
        """
        Changes move_right to given Boolean b.

        :param b: Boolean
        """
        self.__move_right = b

    def move(self):
        """
        Update player position depending on move variables.
        """
        self.__x += self.__speed * self.__move_right - self.__speed * self.__move_left

        if self.__x < 0 and self.__move_left:
            self.__x += 1000 - 26
        if self.__x > 1000 - 26 and self.__move_right:
            self.__x -= 1000 - 26

        self.__y += self.__speed * self.__move_up - self.__speed * (not self.__move_up)

    def kill(self):
        """
        Change dead status variable to True.
        """
        self.__dead = True

    def activate_shield(self):
        """
        Set shield to True.
        """
        self.__shield = True

    def remove_shield(self):
        """
        Set shield to false.
        """
        self.__shield = False

    def add_bomb(self):
        """
        Increase number of bombs by 1.
        """
        self.__bombs += 1

    def remove_bomb(self):
        """
        Decrease number of bombs by 1.
        """
        self.__bombs = max(0, self.__bombs - 1)
