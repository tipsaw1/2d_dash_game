from .map_key import swap_map_key
import pygame
class Level:
  def __init__(self, map, game):
    self.map = map
    self.game = game
    self.enemies = pygame.sprite.Group()
    self.reset()
    
  def reset(self):
    y = 0
    for row in self.map:
      x = 0
      for item in row:
        swap_map_key(item, (x*self.game.TILESIZE,y*self.game.TILESIZE), self.game.TILESIZE, self, self.game.screen)
        x += 1
      y += 1
      
  def draw(self):
    self.enemies.draw(self.game.screen)
    
    