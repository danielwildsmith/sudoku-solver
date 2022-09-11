from settings import *
from solve import is_valid_move


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
            tile_surf = self.font.render(str(self.value), False, 'black')
            tile_rect = tile_surf.get_rect(center=self.pos)
            surface.blit(tile_surf, tile_rect)
        elif self.value == 0 and self.temp_value != 0:
            tile_surf = self.font.render(str(self.temp_value), False, 'grey')
            tile_rect = tile_surf.get_rect(center=self.pos)
            surface.blit(tile_surf, tile_rect)
    
        pygame.draw.rect(surface, 'grey', self.rect, 1)
        
    def highlight(self):
        pass
    
    def check_valid_tile(self):
        return is_valid_move(BOARD, self.temp_value, (self.row, self.col))
    