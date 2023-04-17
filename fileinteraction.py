# the purpose of this file is to provide
# the user with file interaction such as
# adding a new file, opening a file, or opening a directory
import pygame

gameFont = pygame.font.SysFont('Segoe UI', 14)

class File:
    def __init__(self, fileType='txt'):
        self.name = ''
        self.hasName = False
        self.fileType = fileType
        self.children = pygame.sprite.Group() if fileType=='dir' else None
    def writeName(self, event, fileType):
        if self.hasName: return None
        self.fileType = fileType
        if event.key == pygame.K_BACKSPACE:
            self.name = self.name[:-1]
        elif event.key == pygame.K_RETURN:
            self.hasName = True
            return None
        else:
            self.name += event.unicode
        return self

def newFile(event, fileType):
    file = File(fileType)
    return file