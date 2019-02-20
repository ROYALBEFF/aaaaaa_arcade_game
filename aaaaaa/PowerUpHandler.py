from OneUP import  OneUP
from Multiplier import Multiplier
from Shield import Shield
from Bomb import Bomb
import random


class PowerUpHandler:

    def __init__(self):
        pass

    @staticmethod
    def update_powerups(state):
        """
        Decrease life time of powerups and remove them if necessary.

        :param state:
            Current game state.
        """
        for powerup in state.powerups:
            remove = powerup.decrease_ticks()
            if remove:
                state.remove_powerup(powerup)

    @staticmethod
    def generate_powerups(state):
        """
        Generate random powerups.

        :param state:
            Current game state.
        """
        PowerUpHandler.generate_oneup(state)
        PowerUpHandler.generate_multiplier(state)
        PowerUpHandler.generate_shield(state)
        PowerUpHandler.generate_bomb(state)

    @staticmethod
    def generate_oneup(state):
        """
        Generate a new 1-UP powerup with a probability of 1/7500.
        """
        p = random.randint(0, 7500)
        if p < 1:
            state.add_powerup(OneUP())

    @staticmethod
    def generate_multiplier(state):
        """
        Generate a new x2 multiplier with a probability of 1/1000
        or a new x3 multiplier with a probability of 2/1000.
        """
        p = random.randint(0, 1000)
        if p < 1:
            state.add_powerup(Multiplier(3))
        elif p < 2:
            state.add_powerup(Multiplier(2))

    @staticmethod
    def generate_shield(state):
        """
        Generate new shield powerup with probability of 1/5000

        :param state:
            Current game state
        """
        p = random.randint(0, 5000)
        if p < 1:
            state.add_powerup(Shield())

    @staticmethod
    def generate_bomb(state):
        """
        Generate bomb powerup with probability of 1/10000.

        :param state:
            Current game state.
        """
        p = random.randint(0, 10000)
        if p < 1:
            state.add_powerup(Bomb())
