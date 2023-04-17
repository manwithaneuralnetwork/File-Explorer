import pygame
pygame.init()
pygame.font.init()
import sys
import drawingfiles
import fileinteraction

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('File Explorer')
gameFont = pygame.font.SysFont('Segoe UI', 24)

class Game:
    def __init__(self):
        self.currentPath = ''
        self.openFile = ''
        self.files = pygame.sprite.Group()
        self.fileWriting = None
        print('INIT COMPLETE')
        
    def draw(self):
        window.fill((255, 255, 255))
        pathText = gameFont.render('C:' + self.currentPath, False, (0, 0, 0))
        window.blit(pathText, (10, 10))

        pygame.display.flip()
                
    def loop(self):
        clock = pygame.time.Clock()
        clock.tick(60)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if not self.fileWriting == None:
                        self.fileWriting = self.fileWriting.writeName()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
            self.draw()
   
if __name__ == '__main__':
    game = Game()
    game.loop()