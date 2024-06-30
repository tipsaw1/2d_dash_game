import physics
import game
import maps

import pygame
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("SILKSONG IS REAL")
main_game = game.Game(screen)

level1 = game.Level(maps.map_1, main_game)

font = pygame.font.Font(None, 24)

while not main_game.quit:
  for event in pygame.event.get():
    if event.type == QUIT:
      main_game.quit = True
    if event.type == KEYDOWN:
      if event.key == K_RIGHT:
        main_game.offset.x += main_game.TILESIZE
      if event.key == K_LEFT:
        main_game.offset.x -= main_game.TILESIZE
      if event.key == K_UP:
        main_game.offset.y -= main_game.TILESIZE
      if event.key == K_DOWN:
        main_game.offset.y += main_game.TILESIZE
  
  screen.fill("black")
  level1.draw()
  pygame.draw.rect(screen, "blue", (main_game.TILESIZE*(1280//main_game.TILESIZE//2), main_game.TILESIZE*(720//main_game.TILESIZE//2), main_game.TILESIZE, main_game.TILESIZE))
  render = font.render(str(main_game.offset), True, "blue")
  render_rect = render.get_rect(midbottom = (main_game.TILESIZE*(1280//main_game.TILESIZE//2), main_game.TILESIZE*(720//main_game.TILESIZE//2)))
  screen.blit(render, render_rect)
  
  pygame.display.flip()
  clock.tick(60)
  
pygame.quit()
