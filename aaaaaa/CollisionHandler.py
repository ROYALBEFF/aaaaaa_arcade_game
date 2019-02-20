from OneUP import OneUP
from Multiplier import Multiplier
from Shield import Shield
from Bomb import Bomb


class CollisionHandler:

    def __init__(self):
        pass

    @staticmethod
    def check_player_obstacle_collision(player, obstacle, state, screen):
        """
        Check if player collides with given obstacle.

        :param player:
            Player object.
        :param obstacle:
            Obstacle object.
        :param state:
            Current game state.
        :param screen:
            Screen object.
        """
        if CollisionHandler.__check_collision(player, obstacle):
            # remove obstacle from game state
            state.remove_obstacle(obstacle)
            if player.shield:
                # if shield is activated, destroy shield
                player.remove_shield()
                screen.set_message("SHIELD DESTROYED!")
            else:
                # if now shield is activated, decrease extra lives
                player.onedown()
                state.reset_multiplier()
                screen.set_message("OUCH!")
                # kill player if no extra lives were left
                if player.extra_lives < 0:
                    player.kill()

    @staticmethod
    def check_player_powerup_collision(player, powerup, state, screen):
        """
        Check if player collides with given powerup.

        :param player:
            Player object.
        :param powerup:
            Powerup object.
        :param state:
            Current game state.
        :param screen:
            Screen object.
        """
        if CollisionHandler.__check_collision(player, powerup):
            # if powerup is an 1-UP, increase extra lives
            if isinstance(powerup, OneUP):
                screen.set_message("1-UP!")
                player.oneup()

            # if powerup is a multiplier, increase the current multiplier
            if isinstance(powerup, Multiplier):
                if state.multiplier == 1:
                    state.set_multiplier(powerup.multiplier)
                else:
                    state.increase_multiplier(powerup.multiplier)
                screen.set_message("MULTIPLIER INCREASED!")

            # if the powerup is a shield, activate player's shield
            if isinstance(powerup, Shield):
                screen.set_message("SHIELD ACTIVATED!")
                player.activate_shield()

            # if the powerup is a bomb, increase number of available bombs
            if isinstance(powerup, Bomb):
                screen.set_message("BOMB COLLECTED!")
                player.add_bomb()

            state.remove_powerup(powerup)


    @staticmethod
    def __check_collision(subject, other):
        """
        Check collision of two objects.

        :param subject:
            First object.
        :param other:
            Second object.
        :return:
            True if the objects collide, False otherwise.
        """
        other_rect = other.image.get_rect()
        (x, y) = other.pos
        other_rect.top = y
        other_rect.left = x

        subject_rect = subject.image.get_rect()
        (x, y) = subject.pos
        subject_rect.top = y
        subject_rect.left = x

        return other_rect.colliderect(subject_rect)
