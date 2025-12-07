import pygame
from settings import*
import math

class button:
    def __init__(self, text, pos, size, text_background_colour, gameState, action):
        self.textS = dafont.render(text, True, BUTTON_TEXT)
        self.textR = self.textS.get_rect()
        self.textR.center = pos

        self.id = gameState
        self.action = action

        self.bg = pygame.Surface(size)
        self.bg.fill(text_background_colour)
        self.bgr = self.bg.get_frect(center=pos)

    def update(self, mpos, mbut):
        if self.bgr.collidepoint(mpos) and mbut[0]:
            self.action()


    def draw(self,screen):
        screen.blit(self.bg,self.bgr)
        screen.blit(self.textS,self.textR)

class slider:
    def __init__(self, text, pos, size, text_background_colour, gameState, action, multiplier):
        self.barS = pygame.Surface(size)
        self.barS.fill(text_background_colour)
        self.barR = self.barS.get_frect(center=pos)

        self.size= size
        self.multiplier = multiplier
        ya = pos[0]-(size[0]/2)
        da = pos[1]-(size[1])

        self.sliderS = pygame.Surface((25,50))
        self.sliderR = self.sliderS.get_frect(midleft = (self.barR.midleft[0]-(25/2),self.barR.centery))

        self.textS = dafont.render(text, True, BUTTON_TEXT)
        self.textR = self.textS.get_rect(midright =(self.barR.midleft[0]-(25/2),self.barR.centery))

        self.id = gameState
        self.action = action

    def update(self, mpos):
        mbut = pygame.mouse.get_pressed()
        if self.barR.collidepoint(mpos) and mbut[0]:
            self.sliderR.centerx = mpos[0]
            self.action(( (self.sliderR.centerx - self.barR.midleft[0]) / self.size[0]) * self.multiplier)
            return
        if self.sliderR.collidepoint(mpos) and mbut[0]:
            if self.barR.midleft[0] < mpos[0] < self.barR.midright[0]:
                self.sliderR.centerx = mpos[0]
                self.action(((self.sliderR.centerx-self.barR.midleft[0])/self.size[0])*self.multiplier)



    def draw(self,screen):
        screen.blit(self.textS,self.textR)
        screen.blit(self.barS, self.barR)
        screen.blit(self.sliderS,self.sliderR)

class interactives_manager:
    def __init__(self):
        self.buttons = []
        self.sliders = []

    def manage(self,screen, mpos, mbut):
        for buttonn in self.buttons:
            if buttonn.id != PROGRAM_DATA["PROGRAM_STATE"]:
                continue
            buttonn.draw(screen)
            buttonn.update(mpos,mbut)

        for sliderr in self.sliders:
            if sliderr.id != PROGRAM_DATA["PROGRAM_STATE"]:
                continue
            sliderr.update(mpos)
            sliderr.draw(screen)


    def create_slider(self, text, pos, size, text_background_colour, gameState, action, multiplier):
        self.sliders.append(slider(text, pos, size, text_background_colour, gameState, action, multiplier))

    def create_button(self,text, pos, size, text_background_colour, gameState, action):
        self.buttons.append(button(text, pos, size, text_background_colour, gameState, action))

