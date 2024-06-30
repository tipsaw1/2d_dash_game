import pygame
class CustomGroup(pygame.sprite.Group):
    def __init__(self, game):
      self.game = game
      self.offset_2 = 0
      self.offset = pygame.math.Vector2()
      self.offset.x = game.player.rect.x - game.screen.get_width()//2 - self.offset_2
      self.offset.y = game.player.rect.y - game.screen.get_height()//2 
      
    
    