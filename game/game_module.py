import pygame
class Game:
  quit = False
  TILESIZE = 64
  offset = pygame.math.Vector2(TILESIZE, TILESIZE)
  def __init__(self, screen):
    self.screen = screen