class Tile:
    def __init__(self, value, pos, font):
        self.value = value
        self.pos = pos
        self.font = font
        
    def draw(self, surface):
        if not self.value == 0:
            tile_surf = self.font.render(self.value, False, 'black')
            tile_rect = tile_surf.get_rect(center=self.pos)
            surface.blit(tile_surf, tile_rect)
    
    def highlight(self):
        pass
    