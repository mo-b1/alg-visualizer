import pygame
from settings import*
from program_states import*
from node import*
from saver_loader import*
from prompt import*
from interactives import*

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))


def switcher():
    match PROGRAM_DATA["PROGRAM_STATE"]:
        case 0:
            home_screen(screen,allNodes,r,prompts,interactives)
        case 1:
            editor(screen,allNodes,r,prompts,interactives)
        case 2:
            algorithm_menu(screen,allNodes,r,prompts,interactives)
        case 3:
            setting(screen,allNodes,r,prompts,interactives)

coordinates = []
allNodes = Nodes()
r = records()
prompts = prompt_handler()
interactives = interactives_manager()

clock = pygame.time.Clock()
while True:
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if PROGRAM_DATA["INPUT_ACTIVE"]:
                if event.key == pygame.K_RETURN:
                    PROGRAM_DATA["INPUT_ACTIVE"] = False
                    allNodes.create_lines()
                elif event.key == pygame.K_BACKSPACE:
                    PROGRAM_DATA["USER_TEXT"] = PROGRAM_DATA["USER_TEXT"][:-1]
                else:
                    try:
                        if chr(event.key).isdigit():
                            PROGRAM_DATA["USER_TEXT"] += chr(event.key)#
                    except Exception as e:
                        print("Invalid character input, only numbers please")



    screen.fill((47, 79, 79))
    switcher()

    pygame.display.update()