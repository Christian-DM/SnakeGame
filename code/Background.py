import pygame

from code.Const import width, height

pygame.init()
pygame.display.set_caption("Jogo Snake Python")
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()