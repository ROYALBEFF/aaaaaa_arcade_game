from aaaaaa.Powerup import Powerup


class Multiplier(Powerup):

    def __init__(self, mul):
        """
        Initialize Multiplier Powerup.

        :param mul:
            Value of multiplier.
        """
        self.__mul = mul
        # set color to blue for x2 multiplier and to purple for x3 multiplier
        if mul == 2:
            color = (30, 70, 255, 255)
        else:
            color = (255, 10, 255, 255)

        # call Powerup constructor
        super().__init__(color, 250)

    @property
    def multiplier(self):
        """
        Value of multiplier.
        """
        return self.__mul
