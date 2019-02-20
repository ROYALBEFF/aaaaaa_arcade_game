from Obstacle import Obstacle
import random


class ObstacleHandler:

    def __init__(self):
        pass

    @staticmethod
    def generate_obstacle(state):
        """
        Generate a new obstacle with a probability of obstacle_prob percent.
        """
        p = random.randint(0, 100)
        if p < state.obstacle_prob:
            if len(state.obstacles) < 10:
                state.add_obstacle(Obstacle(state.obstacle_speed))

    @staticmethod
    def update_obstacles(state):
        """
        Update position of obstacle. Remove obstacle from game state if it's out of bounds.

        :param state:
            Current game state.
        """
        for obstacle in state.obstacles:
            obstacle.move()
            if obstacle.out_of_bounds():
                state.remove_obstacle(obstacle)

    @staticmethod
    def powerup_obstacles(state):
        """
        Make obstacles faster or appear more often.

        :param state:
            Current game state.
        :return:
            'speed' if obstacles become faster, 'prob' if obstacles appear more often.
        """
        # powerup obstacles if player reaches another 10000 points
        # reset counter
        state.reset_power_up_obstacles()
        p = random.randint(0, 100)
        # with probability of 1/3 increase obstacle speed by 1
        if p <= 33:
            state.increase_obstacle_speed()
            return "speed"
        # with probability of 2/3 increase obstacle spawn probability by 1 percent
        else:
            state.increase_obstacle_prob()
            return "prob"
