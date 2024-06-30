import pygame
from .enemy_module import Enemy
def swap_map_key(key, pos, size, level, screen):
  pos -= level.game.offset
  rect_data = (pos[0], pos[1], size, size)
  image = pygame.Surface((size,size))
  match key:
    case "enemy":
      image.fill("red")
      Enemy(pos, image, level, level.enemies)
      
    case "npc":
      pygame.draw.rect(screen, "green", rect_data)
      
    case _:
      pygame.draw.rect(screen, "white", rect_data, 1)
      
