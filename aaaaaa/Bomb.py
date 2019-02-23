from aaaaaa.Powerup import Powerup


class Bomb(Powerup):

    def __init__(self):
        super().__init__((255, 10, 10, 255), 250)
