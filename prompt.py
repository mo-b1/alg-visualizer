from settings import*
import time

class prompt:
    def __init__(self, status, size, pos, time):
        self.time = time
        self.image = pygame.Surface(size)
        if status[1]:
            self.image.fill(SUCCESS_COLOUR)
        else:
            self.image.fill(FAIL_COLOUR)
        self.rect = self.image.get_frect(center = pos)
        self.textS = dafont.render(status[0], True, "White")
        self.textR= self.textS.get_rect(center = pos)

    def draw(self, screen):
        screen.blit(self.image,self.rect)
        screen.blit(self.textS,self.textR)

    def update(self):
        if time.time() - self.time >0.5:
            return False
        else:
            return True

class prompt_handler:
    def __init__(self):
        self.prompts = []

    def create_prompt(self,status, size, pos,time):
        p  = prompt(status,size,pos,time)
        self.prompts.append(p)

    def handle(self,screen):
        for prompt in self.prompts:
            prompt.draw(screen)
            if not prompt.update(): self.prompts.remove(prompt)