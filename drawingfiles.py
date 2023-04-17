import pygame

gameFont = pygame.font.SysFont('Segoe UI', 18)

class Organizer:
    def __init__(self):
        self.currentDisplay = None
        self.width = 750
        self.height = 24
        self.xmarg = 6
        self.ymarg = 50
    def drawFiles(self, files):
        rung = 1
        for file in files.sprites():
            file.drawSelf((self.width, self.height), (rung*16, 25), self.xmarg, self.ymarg)
            rung += 1