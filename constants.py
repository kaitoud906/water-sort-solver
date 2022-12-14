import pygame as pg

DEBUG_LOGGING = True

EMPTY_SYMBOL = '-'
TUBE_HEIGHT = 4

FPS = 15

# define all the colors used as RGB values
COLORS = {
    "BLACK": (0, 0, 0),
    "GRAY": (63, 63, 63),
    "WHITE": (255, 255, 255),
    "BLUE": (0, 0, 255),
    "ORANGE": (255, 215, 0),
    "MINT_GREEN": (152, 255, 152),
    "BROWN": (165, 42, 42),
    "RED": (255, 0, 0),
    "BEIGE": (244, 226, 198),
    "YELLOW": (255, 255, 0),
    "DARK_GREEN": (0, 100, 0),
    "GREEN": (0, 255, 0),
    "PINK": (255, 192, 203),
    "CYAN": (0, 255, 255),
    "PURPLE": (128, 0, 128),
    "INDIGO": (75, 0, 130),
    "VIOLET": (138, 43, 226),
    EMPTY_SYMBOL: (127, 127, 127)  # GRAY - default background color
}

# set default background color
BACKGROUND_COLOR = COLORS[EMPTY_SYMBOL]

# graphics constants
# WIDTH, HEIGHT = WINDOW_SIZE = (1600, 900)
WIDTH, HEIGHT = WINDOW_SIZE = (800, 450)

TUBE_GRAPHIC_WIDTH, TUBE_GRAPHIC_HEIGHT = WIDTH // 16, HEIGHT // 3
TUBE_BORDER_WIDTH = 5
TUBE_BORDER_RADIUS = TUBE_GRAPHIC_WIDTH // 2
TUBE_VISUAL_INDICATOR_OFFSET = 20

PUZZLES_PER_ROW = 4
PUZZLES_PER_COLUMN = 4
PUZZLES_PER_PAGE = PUZZLES_PER_ROW * PUZZLES_PER_COLUMN

# pygame events
user_event_offset = 0

def define_event():
    global user_event_offset
    user_event_offset += 1
    return pg.USEREVENT + user_event_offset


# title_scene events
PUZZLE_SELECTION_EVENT = define_event()

# puzzle_scene events
UPDATE_TUBE_EVENT = define_event()
HINT_BUTTON_EVENT = define_event()
