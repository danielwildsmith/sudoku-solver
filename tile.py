import pygame

from settings import *


class Tile:
    def __init__(self, value, pos, font):
        self.value = value
        self.pos = pos
        self.font = font
        self.rect = pygame.rect.Rect(pos[0] - TILE_SIZE / 2, pos[1] - TILE_SIZE / 2, TILE_SIZE, TILE_SIZE)

    def draw(self, surface):
        if not self.value == 0:
            tile_surf = self.font.render(str(self.value), False, 'black')
            tile_rect = tile_surf.get_rect(center=self.pos)
            surface.blit(tile_surf, tile_rect)
        pygame.draw.rect(surface, 'grey', self.rect, 1)
    
    def highlight(self):
        pass
    