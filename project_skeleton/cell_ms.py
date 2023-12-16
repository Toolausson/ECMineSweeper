import pygame
import random


class Cell:
    """This file contains the cell class representing each square in the game"""

    def __init__(self, x, y, width, height, bomb_chance):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.color = (0, 64, 0)
        self.cell_thickness = 2
        self.neighbouring_bombs = 0
        #self.selected = False
        self.cell_center = (self.x + self.width // 2, self.y + self.width // 2)
        self.bomb = random.random() < bomb_chance
        self.hidden = True


    def draw(self, screen):
        """This method is called in the main.py files draw_cells fkn"""
        pygame.draw.rect(screen, "black", (self.x, self.y, self.width, self.height), self.cell_thickness)
        if not self.hidden:
            pygame.draw.rect(screen, "black", (self.x, self.y, self.width, self.height), self.cell_thickness)
            if self.bomb:
                font = pygame.font.Font(None, 36)
                text = font.render('X', True, (255, 0, 0))
                text_rect = text.get_rect(center=self.cell_center)
                screen.blit(text, text_rect)
            else:
                font = pygame.font.Font(None, 36)
                text = font.render(str(self.neighbouring_bombs), True, (0, 0, 0))
                text_rect = text.get_rect(center=self.cell_center)
                screen.blit(text, text_rect)

    def show(self):
        self.hidden = False