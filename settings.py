import pygame

def set_game_state(value):
    PROGRAM_DATA["PROGRAM_STATE"] = value
    PROGRAM_DATA["PROGRAM_STATE_HISTORY"].append(value)

def previous_game_state():
    global PROGRAM_DATA
    PROGRAM_DATA["PROGRAM_STATE_HISTORY"].pop(-1)
    PROGRAM_DATA["PROGRAM_STATE"] = PROGRAM_DATA["PROGRAM_STATE_HISTORY"][-1]
def set_animation_speed(value):
    if value !=0: PROGRAM_DATA["ANIMATION_SPEED"] = 0.6/value
    print(PROGRAM_DATA["ANIMATION_SPEED"])

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900

PROGRAM_DATA = {
    "PROGRAM_STATE" : 0,
    "PROGRAM_STATE_HISTORY" : [0],
    "BACK_BUTTON_IMAGE": pygame.image.load("assets/back.png"),
    "NODE_IMAGE": pygame.image.load("assets/node.png"),
    "USER_TEXT": "",
    "INPUT_ACTIVE": False,
    "LOADER":-1,
    "BUTTON_INIT":False,
    "ANIMATION_SPEED": 0.6,
    "set_program_state":set_game_state,
    "prev_program_state":previous_game_state,
    "set_animation_speed":set_animation_speed,
    "changes": [],
}


pygame.font.init()
dafont = pygame.font.SysFont("Comic Sans MS", 20)
#back_button_image = pygame.image.load("assets/back.png")

#colour theme
PRIMARY_BUTTON = (0,128,128)
SECONDARY_BUTTON =(70,130,180)
WARNING_BUTTON = (255,127,80)
BUTTON_TEXT = (255,255,255)
LINE_COLOUR = (200,200,200)
FAIL_COLOUR = (240,72,72)
SUCCESS_COLOUR =(74,235,106)

