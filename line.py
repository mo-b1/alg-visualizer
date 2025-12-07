import time
from settings import*
import pygame


class Line:
    def __init__(self, node1,node2, colour, weight):
        self.node1 = node1
        self.node2 = node2
        self.colour = colour
        self.midpoint = ((self.node1.rect.x+self.node2.rect.x)/2+20,(self.node1.rect.y+self.node2.rect.y)/2+20)

        self.weight = weight
        self.text = dafont.render(str(self.weight), True, BUTTON_TEXT, bgcolor=(0,0,0))
        self.textr = self.text.get_frect(center=self.midpoint)

        self.time = 0

    def update(self):
        if time.time()-self.time >PROGRAM_DATA["ANIMATION_SPEED"] and self.colour != "red":
            self.colour = LINE_COLOUR

    def draw(self, screen):
        self.textr.center = ((self.node1.rect.x+self.node2.rect.x)/2+20,(self.node1.rect.y+self.node2.rect.y)/2+20)
        pygame.draw.line(screen, self.colour, self.node1.rect.center, self.node2.rect.center, width = 7)
        screen.blit(self.text,self.textr)
