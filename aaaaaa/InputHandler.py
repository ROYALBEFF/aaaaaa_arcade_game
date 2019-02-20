import pygame


class InputHandler:

    def __init__(self):
        pass

    @staticmethod
    def in_game_input(state, player, screen):
        """
        Handle keyboard input while in-game.
        Handles movement, use of items and pause.

        :param state:
            Current game state.
        :param player:
            Player object.
        :param screen:
            Screen object.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player.kill()
                    state.quit_game()
                    continue
                if event.key == pygame.K_LEFT:
                    player.set_move_left(True)
                    player.set_move_right(False)
                if event.key == pygame.K_RIGHT:
                    player.set_move_left(False)
                    player.set_move_right(True)
                if event.key == pygame.K_RETURN:
                    state.pause_game()
                if event.key == pygame.K_SPACE and player.bombs > 0:
                    player.remove_bomb()
                    state.destroy_obstacles_powerups()
                    screen.set_message("BOOM!!!")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.set_move_left(False)
                if event.key == pygame.K_RIGHT:
                    player.set_move_right(False)

    @staticmethod
    def name_input(state):
        """
        Handle keyboard input while name input.

        :param state:
            Current game state.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    state.next_char()
                if event.key == pygame.K_DOWN:
                    state.prev_char()
                if event.key == pygame.K_LEFT:
                    state.prev_nick_pos()
                if event.key == pygame.K_RIGHT:
                    state.next_nick_pos()
                if event.key == pygame.K_RETURN:
                    state.set_nick()

    @staticmethod
    def try_again_input(state):
        """
        Handle keyboard input while showing the try again screen.

        :param state:
            Current game state.
        :return:
            True for try again, False for back to title.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # ESC -> quit game
                if event.key == pygame.K_ESCAPE:
                    state.back_to_title()
                    return True
                # RETURN -> restart game
                if event.key == pygame.K_RETURN:
                    return True

    @staticmethod
    def resume_input(state):
        """
        Handle keyboard input while pause.

        :param state:
            Current game state.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # ESC -> quit game
                if event.key == pygame.K_ESCAPE:
                    state.back_to_title()
                # RETURN -> resume game
                if event.key == pygame.K_RETURN:
                    state.resume_game()

    @staticmethod
    def start_input(state):
        """
        Handle keyboard input on title screen.

        :param state:
            Current game state.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # ESC -> back to title
                if event.key == pygame.K_ESCAPE:
                    state.quit_game()
                # RETURN -> start game
                if event.key == pygame.K_RETURN:
                    state.start_game()
