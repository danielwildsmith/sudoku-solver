from src.settings import *
from src.solve import is_valid_move


class Tile:
    def __init__(self, value, pos, font, fixed, row, col):
        self.value = value
        self.pos = pos
        self.font = font
        self.rect = pygame.rect.Rect(pos[0] - TILE_SIZE / 2, pos[1] - TILE_SIZE / 2, TILE_SIZE, TILE_SIZE)
        self.temp_value = 0
        self.fixed = fixed
        self.row = row
        self.col = col

    def draw(self, surface, background_color=None):
        if background_color:
            pygame.draw.rect(surface, background_color, self.rect)
            
        if not self.value == 0:
            tile_surf = self.font.render(str(self.value), False, '#293640')
            tile_rect = tile_surf.get_rect(center=self.pos)
            surface.blit(tile_surf, tile_rect)
        elif self.value == 0 and self.temp_value != 0:
            tile_surf = self.font.render(str(self.temp_value), False, 'grey')
            tile_rect = tile_surf.get_rect(center=self.pos)
            surface.blit(tile_surf, tile_rect)
    
        pygame.draw.rect(surface, 'grey', self.rect, 1)
        
    def visualize_algorithm(self, surface, green):
        container = pygame.rect.Rect(self.pos[0] - TILE_SIZE / 2 + 2, self.pos[1] - TILE_SIZE / 2 + 2,
                                     TILE_SIZE - 2, TILE_SIZE - 2)
        if green:
            pygame.draw.rect(surface, '#5eb873', container)
        else:
            pygame.draw.rect(surface, '#a85b5b', container)
            
        tile_surf = self.font.render(str(self.value), False, '#293640')
        tile_rect = tile_surf.get_rect(center=self.pos)
        surface.blit(tile_surf, tile_rect)
        
    def check_valid_tile(self):
        return is_valid_move(BOARD, self.temp_value, (self.row, self.col))
    