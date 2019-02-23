from aaaaaa.GameState import GameState
from aaaaaa.Player import Player
from aaaaaa.PowerUpHandler import PowerUpHandler
from aaaaaa.ObstacleHandler import ObstacleHandler
from aaaaaa.Screen import Screen
from aaaaaa.InputHandler import InputHandler
from aaaaaa.CollisionHandler import CollisionHandler
import pygame


def main(args=None):
    # initialize pygame and game state
    pygame.init()
    screen = Screen()
    state = GameState()
    # create player and set position
    player = Player(500, 400)

    while not state.quit:
        # if player is dead press enter to restart or escape to end the game
        if player.dead:
            # update highscore if necessary
            if state.update_highscore:
                # add new highscore entry if current player score is higher than any in the top ten
                if state.new_highscore:
                    state.add_highscore_entry()
                # set to False such that the highscore is only updated once
                state.highscore_updated()

            if state.new_highscore and state.input_nick:
                # handle input for nickname
                InputHandler.name_input(state)

            # show highscore screen
            screen.show_highscore(state)
            # do not check further pressed buttons while input player nick
            if state.new_highscore and state.input_nick:
                screen.update()
                continue

            # show try again text
            screen.show_try_again()
            # try again or back to title
            if InputHandler.try_again_input(state):
                # reset state, player and screen
                state.reset()
                player = Player(500, 400)
                screen = Screen()

            screen.update()
            continue

        # show pause screen
        if state.pause:
            screen.show_pause()
            screen.update()
            InputHandler.resume_input(state)
            continue

        # show title screen
        if state.title:
            screen.show_title()
            screen.update()
            InputHandler.start_input(state)
            continue

        # generate random objects
        ObstacleHandler.generate_obstacle(state)
        PowerUpHandler.generate_powerups(state)

        # show game screen
        screen.show_game(state, player)
        # update info bar
        screen.write_score_and_multiplier(state)
        screen.write_extra_lives(player)
        screen.show_info()

        # powerup obstacles every 10000 points
        if state.power_up_obstacles >= 10000:
            prop = ObstacleHandler.powerup_obstacles(state)
            if prop == 'speed':
                screen.set_message('GEOMETRY SPEED UP!')
            if prop == 'prob':
                screen.set_message('GEOMETRY INTENSIFIES!')

        # check collision with obstacles, reset multiplier, decrease extra lives
        for obstacle in state.obstacles:
            CollisionHandler.check_player_obstacle_collision(player, obstacle, state, screen)
            if player.dead:
                break

        # check collision with powerups and increase extra lives or multiplier respectively
        for powerup in state.powerups:
            CollisionHandler.check_player_powerup_collision(player, powerup, state, screen)

        # check pressed buttons for player movement
        InputHandler.in_game_input(state, player, screen)
        # update player position
        player.move()
        screen.show_player(player)

        # update obstacle positions
        ObstacleHandler.update_obstacles(state)
        # show obstacles
        for obstacle in state.obstacles:
            screen.show_obstacle(obstacle)

        # check if any powerups must be removed
        PowerUpHandler.update_powerups(state)
        # show powerups
        for powerup in state.powerups:
            screen.show_powerup(powerup)

        # render screen
        screen.update()

    pygame.quit()
