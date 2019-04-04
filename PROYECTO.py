import pygame

WIDTH = 500
HEIGHT = 500
FPS = 30

pygame.init() 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048 PLUS")
clock = pygame.time.Clock()

