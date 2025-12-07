import time
import pygame
from settings import*
from _thread import start_new_thread
import win2

def USER_TEXT_INPUT(text, pos, screen, size, text_background_colour):
    surf= pygame.Surface(size)
    surf.fill(text_background_colour)
    rectt = surf.get_frect(center=pos)
    texts = dafont.render(text, True, BUTTON_TEXT)
    textr = texts.get_rect(topleft=(pos[0]-(size[0]/2),pos[1]-(size[1]/3)))
    screen.blit(surf,rectt)
    screen.blit(texts,textr)


def back_buttonn(screen):
    '''back_button_image = PROGRAM_DATA["BACK_BUTTON_IMAGE"].convert_alpha()
    back_button_image = pygame.transform.scale_by(back_button_image, 0.08)
    back_rect= back_button_image.get_frect(topleft = (0,0))
    screen.blit(back_button_image,back_rect)
    return back_rect'''
    for i in range(1,4):
        pygame.draw.line(screen, "white", (20,i*10+5),(45,i*10+5), width = 3)
    return pygame.Rect((20,15),(20,20))


def button_init(screen, allNodes, r, prompts, interactives):
    if not PROGRAM_DATA["BUTTON_INIT"]:
        interactives.create_button("Start", (WINDOW_WIDTH/2, WINDOW_HEIGHT/2-27), (100,50),PRIMARY_BUTTON, 0,lambda : PROGRAM_DATA["set_program_state"](1))
        interactives.create_button("Settings", (WINDOW_WIDTH/2, WINDOW_HEIGHT/2+27), (100,50),PRIMARY_BUTTON, 0,lambda : PROGRAM_DATA["set_program_state"](3))

        interactives.create_slider("Animation speed: ", (WINDOW_WIDTH/2, WINDOW_HEIGHT/10), (300,25),PRIMARY_BUTTON, 3, PROGRAM_DATA["set_animation_speed"],3)

        interactives.create_button("New NODE", (WINDOW_WIDTH - 60, 30),  (110, 50), PRIMARY_BUTTON, 1,allNodes.add_new_node)
        interactives.create_button("New LINE", (WINDOW_WIDTH - 60, 100),  (110, 50), SECONDARY_BUTTON, 1,lambda: PROGRAM_DATA.update(INPUT_ACTIVE=True))

        interactives.create_button("Show matrix", (WINDOW_WIDTH - 60, 240),  (110, 50), SECONDARY_BUTTON, 1,lambda: start_new_thread(win2.show_matrix, (allNodes.matrix,)))
        interactives.create_button("Show list", (WINDOW_WIDTH - 60, 310),  (110, 50), SECONDARY_BUTTON, 1, allNodes.show_list_format )

        interactives.create_button("DELETE", (60, WINDOW_HEIGHT-30),(110,50), WARNING_BUTTON, 1, lambda:prompts.create_prompt(r.delete_matrix(allNodes.matrix, allNodes.RESET()),(225,50),(WINDOW_WIDTH/2,30), time.time()))
        interactives.create_button("Save", (WINDOW_WIDTH - 300, WINDOW_HEIGHT - 30),  (110, 50), PRIMARY_BUTTON, 1,lambda: prompts.create_prompt(r.save_matrix(allNodes), (225, 50), (WINDOW_WIDTH/2,30),time.time()))
        interactives.create_button("Load", (WINDOW_WIDTH - 180, WINDOW_HEIGHT - 30), (110, 50), PRIMARY_BUTTON, 1,lambda: allNodes.load_matrix(r.load_matrix(PROGRAM_DATA["LOADER"])))
        interactives.create_button("RESET", (WINDOW_WIDTH - 60, WINDOW_HEIGHT - 30), (110, 50), WARNING_BUTTON, 1,allNodes.RESET)

        interactives.create_button("Algorithms", (WINDOW_WIDTH - 60, 380),  (110, 50), PRIMARY_BUTTON, 1, lambda :PROGRAM_DATA["set_program_state"](2))
        interactives.create_button("Reset alg", (WINDOW_WIDTH - 60, WINDOW_HEIGHT - 30),  (110, 50), PRIMARY_BUTTON, 2, allNodes.reset_animation)
        interactives.create_slider(" ", (WINDOW_WIDTH-240, WINDOW_HEIGHT-30), (230,25),PRIMARY_BUTTON, 2, PROGRAM_DATA["set_animation_speed"], 3)

        interactives.create_button("PRIMS", (WINDOW_WIDTH - 60, 30),  (110, 50), PRIMARY_BUTTON, 2,lambda: prompts.create_prompt(allNodes.prims(), (225, 50), (WINDOW_WIDTH/2,30),time.time()))
        interactives.create_button("Floyds", (WINDOW_WIDTH - 60, 90),  (110, 50), PRIMARY_BUTTON, 2,lambda: prompts.create_prompt(allNodes.floyd(), (225, 50), (WINDOW_WIDTH/2,30),time.time()))
        interactives.create_button("Show shortest", (WINDOW_WIDTH - 60, 150),  (110, 50), PRIMARY_BUTTON, 2,lambda: prompts.create_prompt(allNodes.show_shortest(), (225, 50), (WINDOW_WIDTH/2,30),time.time()))

        PROGRAM_DATA["BUTTON_INIT"] = True
def setting(screen,allNodes,r,prompts,interactives):
    mpos = pygame.mouse.get_pos()
    mbut = pygame.mouse.get_just_pressed()

    back_button = back_buttonn(screen)
    if back_button.collidepoint(mpos) and mbut[0]:
        previous_game_state()

    prompts.handle(screen)
    interactives.manage(screen, mpos, mbut)


def home_screen(screen, allNodes, r, prompts, interactives):
    mpos = pygame.mouse.get_pos()
    mbut = pygame.mouse.get_just_pressed()
    k = pygame.key.get_just_pressed()
    button_init(screen, allNodes, r, prompts, interactives)
    interactives.manage(screen,mpos,mbut)

def editor(screen, allNodes, r, prompts, interactives):
    mpos = pygame.mouse.get_pos()
    mbut = pygame.mouse.get_just_pressed()

    prompts.handle(screen)
    interactives.manage(screen, mpos, mbut)

    back_button = back_buttonn(screen)
    if back_button.collidepoint(mpos) and mbut[0]:
        previous_game_state()

    if PROGRAM_DATA["INPUT_ACTIVE"]:
        USER_TEXT_INPUT(PROGRAM_DATA["USER_TEXT"],(WINDOW_WIDTH-60, 170), screen,(110,50), WARNING_BUTTON)

    #nodes.DELETE()
    allNodes.update(screen)

def algorithm_menu(screen, allNodes, r, prompts, interactives):
    mpos = pygame.mouse.get_pos()
    mbut = pygame.mouse.get_just_pressed()

    prompts.handle(screen)
    interactives.manage(screen, mpos, mbut)

    back_button = back_buttonn(screen)
    if back_button.collidepoint(mpos) and mbut[0]:
        previous_game_state()

    allNodes.update(screen)










