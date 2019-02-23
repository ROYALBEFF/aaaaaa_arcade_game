import pkg_resources
import pygame


class Screen:

    def __init__(self):
        """
        Initialize game screen.
        """
        self.__clock = pygame.time.Clock()
        self.__size = (1000, 800)
        self.__screen = pygame.display.set_mode(self.__size)
        self.__font = pygame.font.Font(None, 24)
        self.__large_font = pygame.font.Font(None, 42)

        self.__white = (255, 255, 255)
        self.__grey = (150, 150, 150)

        self.__border_height = 35
        self.__border_width = 1000

        self.__show_blank = False
        self.__input_ticks = 10

        # number of ticks the message will be shown
        self.__message_ticks = 0
        self.__message = ''

        # extra life symbol
        image_path = pkg_resources.resource_filename('aaaaaa.resources.images', 'extra_lives.png')
        self.__symbol = pygame.image.load(image_path)
        self.__symbol_rect = self.__symbol.get_rect()
        self.__symbol_rect.topleft = [980, 10]

        # bomb symbol
        image_path = pkg_resources.resource_filename('aaaaaa.resources.images', 'obstacle.png')
        self.__bomb = pygame.image.load(image_path)
        self.__bomb = pygame.transform.scale(self.__bomb, (15, 15))
        self.__bomb.fill((0, 0, 0, 255), None, pygame.BLEND_RGB_MULT)
        self.__bomb.fill((255, 10, 10, 255), None, pygame.BLEND_RGB_ADD)
        self.__bomb_rect = self.__bomb.get_rect()
        self.__bomb_rect.topleft = [920, 10]

    def show_game(self, state, player):
        """
        Reset screen and prepare in-game screen.

        :param state:
            Current game state.
        :param player:
            Player object
        """
        self.__screen.fill((0, 0, 0))

        (_, y) = player.pos
        # check collision with upper bound
        if y <= 35:
            # collision animation
            pygame.draw.rect(self.__screen, self.__grey, (0, self.__border_height, self.__border_width, 3), 3)
            pygame.draw.rect(self.__screen, self.__white,
                             (0, self.__size[1] - self.__border_height, self.__border_width, 3), 3)
            player.flip()
            # increase score when colliding with bounds
            state.increase_score()
        # check collision with lower bound
        elif y >= 710:
            # collision animation
            pygame.draw.rect(self.__screen, self.__white, (0, self.__border_height, self.__border_width, 3), 3)
            pygame.draw.rect(self.__screen, self.__grey,
                             (0, self.__size[1] - self.__border_height, self.__border_width, 3), 3)
            player.flip()
            # increase score when colliding with bounds
            state.increase_score()
        else:
            # draw bounds
            pygame.draw.rect(self.__screen, self.__white, (0, self.__border_height, self.__border_width, 3), 3)
            pygame.draw.rect(self.__screen, self.__white,
                             (0, self.__size[1] - self.__border_height, self.__border_width, 3), 3)

    def show_highscore(self, state):
        """
        Reset screem and show highscore screen.

        :param state:
            Current game state.
        """
        self.__screen.fill((0, 0, 0))

        for i, nick in enumerate(state.nicks):
            # let current input character blink
            if state.input_nick and self.__show_blank and state.new_highscore and state.highscore_pos == i:
                prefix = nick[:state.nick_pos]
                postfix = nick[state.nick_pos+1:]
                nick = prefix + '_' + postfix

            text = self.__font.render('{:15}'.format(nick), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.topleft = [400, 200 + i*30]
            self.__screen.blit(text, text_rect)

        # decrease input ticks counter and toggle show_blank if ticks equals 0
        self.__input_ticks -= 1
        if self.__input_ticks == 0:
            self.__input_ticks = 10
            self.__show_blank = not self.__show_blank

        # show highscore scores
        for i, score in enumerate(state.scores):
            text = self.__font.render('{:>10}'.format(score), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.topright = [600, 200 + i*30]
            self.__screen.blit(text, text_rect)

        pygame.draw.rect(self.__screen, self.__white, (0, self.__border_height, self.__border_width, 3), 3)
        pygame.draw.rect(self.__screen, self.__white,
                         (0, self.__size[1] - self.__border_height, self.__border_width, 3), 3)

        if state.new_highscore:
            highscore_text = self.__large_font.render('NEW HIGHSCORE!', True, (255, 255, 255))
        else:
            highscore_text = self.__large_font.render('HIGHSCORE', True, (255, 255, 255))
        highscore_rect = highscore_text.get_rect()
        highscore_rect.center = [500, 100]
        self.__screen.blit(highscore_text, highscore_rect)

    def show_try_again(self):
        """
        Add try again or back to title to screen.
        """
        text = self.__font.render('TRY AGAIN? (ENTER)', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = [500, 700]
        self.__screen.blit(text, text_rect)

        text = self.__font.render('BACK TO TITLE (ESC)', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = [500, 720]
        self.__screen.blit(text, text_rect)

    def show_pause(self):
        """
        Reset screen and show pause screen.
        """
        self.__screen.fill((0, 0, 0))
        pygame.draw.rect(self.__screen, self.__white, (0, self.__border_height, self.__border_width, 3), 3)
        pygame.draw.rect(self.__screen, self.__white,
                         (0, self.__size[1] - self.__border_height, self.__border_width, 3), 3)

        text = self.__large_font.render('PAUSE', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = [500, 400]
        self.__screen.blit(text, text_rect)

    def show_title(self):
        """
        Reset screen and show title screen.
        """
        self.__screen.fill((0, 0, 0))
        pygame.draw.rect(self.__screen, self.__white, (0, self.__border_height, self.__border_width, 3), 3)
        pygame.draw.rect(self.__screen, self.__white,
                         (0, self.__size[1] - self.__border_height, self.__border_width, 3), 3)

        text = self.__large_font.render('PRESS ENTER TO AAAAAA!', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = [500, 400]
        self.__screen.blit(text, text_rect)

    def show_player(self, player):
        """
        Add player image to screen.

        :param player:
            Player object.
        """
        if player.shield:
            player.image.fill((0, 0, 0, 255), None, pygame.BLEND_RGB_MULT)
            player.image.fill((255, 200, 10, 255), None, pygame.BLEND_RGB_ADD)
        else:
            player.image.fill((0, 0, 0, 255), None, pygame.BLEND_RGB_MULT)
            player.image.fill((255, 255, 255, 255), None, pygame.BLEND_RGB_ADD)
        self.__screen.blit(player.image, player.pos)

    def show_obstacle(self, obstacle):
        """
        Add obstacle image to screen.

        :param obstacle:
            Obstacle object.
        """
        self.__screen.blit(obstacle.image, obstacle.pos)

    def show_powerup(self, powerup):
        """
        Add powerup image to screen.

        :param powerup:
            Powerup object.
        """
        self.__screen.blit(powerup.image, powerup.pos)

    def update(self):
        """
        Render new screen.
        """
        pygame.display.flip()
        self.__clock.tick(60)

    def set_message(self, msg):
        """
        Set message and number of ticks the message will be shown.
        Number of ticks = 250.

        :param msg:
            Message that will be shown in the info bar.
        """
        self.__message = msg
        self.__message_ticks = 250

    def show_info(self):
        """
        Show message in info bar.
        """
        text = self.__font.render(self.__message, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = [500, 17]
        self.__screen.blit(text, text_rect)

        self.__message_ticks -= 1
        if self.__message_ticks == 0:
            self.__message = ''

    def write_score_and_multiplier(self, state):
        """
        Show player score and score multiplier in info bar.

        :param state:
            Current game state.
        """
        text = self.__font.render('x' + str(state.multiplier) + ' | ' + str(state.score), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = [10, 10]
        self.__screen.blit(text, text_rect)

    def write_extra_lives(self, player):
        """
        Show extra lives in info bar.

        :param player:
            Player object.
        """
        text = self.__font.render(str(player.bombs) + 'x ', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topright = [920, 10]
        self.__screen.blit(text, text_rect)
        self.__screen.blit(self.__bomb, self.__bomb_rect)

        text = self.__font.render(str(player.extra_lives) + 'x ', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topright = [980, 10]
        self.__screen.blit(text, text_rect)
        self.__screen.blit(self.__symbol, self.__symbol_rect)
