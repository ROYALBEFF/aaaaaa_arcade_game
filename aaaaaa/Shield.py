from aaaaaa.Powerup import Powerup


class Shield(Powerup):

    def __init__(self):
        super().__init__((255, 200, 10, 255), 250)
