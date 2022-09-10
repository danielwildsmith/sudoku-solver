import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 600))
        pygame.display.set_caption('Sudoku')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('joystix.ttf', 30)
        
    def draw_grid(self):
        title_surf = self.font.render('Sudoku', False, '#293640')
        title_rect = title_surf.get_rect(midbottom=(700/2, 55))
        self.screen.blit(title_surf, title_rect)

        grid_gap = 150
        # outer lines lines
        for i in range(0, 4):
            pygame.draw.line(self.screen, 'black', (125 + grid_gap * i, 75), (125 + grid_gap * i, 525), 2)
            pygame.draw.line(self.screen, 'black', (125, 75 + grid_gap * i), (575, 75 + grid_gap * i), 2)
            
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill('#edf6f7')
            self.draw_grid()
            
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
