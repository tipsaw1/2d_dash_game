import pygame
class Enemy(pygame.sprite.Sprite):
  def __init__(self, pos, image, level, group):
    super().__init__(group)
    self.level = level
    self.image = image
    self.rect = self.image.get_rect(topleft = pos)
    
    