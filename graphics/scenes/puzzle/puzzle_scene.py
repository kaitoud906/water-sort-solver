import pygame as pg
import pygame.display
# import pygame_widgets
import logging
import time

from pygame_widgets import WidgetHandler

# from constants import UPDATE_TUBE_EVENT, HINT_BUTTON_EVENT, WIDTH, HEIGHT, DEBUG_LOGGING
from graphics.scenes.puzzle.puzzle_renderer import create_tube_graphics, draw_window, draw_text_center_screen
from data.node import Node

class_name = "PuzzleScene"
class SceneBase:
    def __init__(self):
        self.next = self

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen, events):
        """
        events *really* shouldn't be used in the Render function,
        but it's necessary for pygame_widgets to work as it handles everything at once
        :param screen:
        :param events:
        :return:
        """

        print("uh-oh, you didn't override this in the child class")

    def ClearWidgets(self):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.ClearWidgets()
        self.next = next_scene

    def Terminate(self):
        logging.info("Terminate Scene (end game)")
        self.SwitchToScene(None)


class PuzzleScene(SceneBase):
    def __init__(self, game_puzzle: Node):
        SceneBase.__init__(self)

        # pygame setup
        pg.display.set_caption("Water Sorting Puzzle - " + str(game_puzzle.num_id))

        # Scene content
        self.puzzle = game_puzzle
        self.tube_graphics = create_tube_graphics(game_puzzle)

        # default initializations
        self.move_counter = 0

        # auto solver stuff
        self.puzzle_solved = False
        self.puzzle_failed = False
        self.hint_button_pressed = False
        self.puzzle_solver_attempted = False
        self.solved_node_move_index = 0
        self.solved_node = None

        # widgets
        self.hint_button = None

    def start(self, scene):
        self.SwitchToScene(scene)
        
    def Update(self, move):
        self.tube_graphics[move[0]].tube.move_liquid(self.tube_graphics[move[1]].tube)
        time.sleep(0.8)

    def Render(self, screen, events):
        draw_window(screen, self.tube_graphics, self.move_counter)

        # if self.puzzle_solved:
        #     logging.info("puzzle_solved - win! draw win text on screen and Terminate()")
        #     draw_text_center_screen(screen, 'DONE')
        #     pg.time.delay(5000)

        pygame.display.update()

    def ClearWidgets(self):
        logging.info(f"{class_name}: Clear Widgets")
        widgets = WidgetHandler.getWidgets()
        widgets.remove(self.hint_button)
