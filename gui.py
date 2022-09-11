from settings import *
from tile import Tile


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Sudoku')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(GAME_FONT, 30)
        self.tiles = self.init_tiles()
        self.loc = [0, 0]
        
        self.selection_time = None
        self.can_move = True
    
    def draw_grid(self):
        title_surf = self.font.render('Sudoku', False, '#293640')
        title_rect = title_surf.get_rect(midbottom=(WIDTH / 2, 55))
        self.screen.blit(title_surf, title_rect)
        
        grid_gap = GRID_SIZE / 3
        # outer lines
        for i in range(0, 4):
            pygame.draw.line(self.screen, 'black', (125 + grid_gap * i, 75), (125 + grid_gap * i, 525), 2)
            pygame.draw.line(self.screen, 'black', (125, 75 + grid_gap * i), (575, 75 + grid_gap * i), 2)
    
    def init_tiles(self):
        # 9x9: creating tile objects
        tiles = [
            [], [], [], [], [], [], [], [], []
        ]
        for i in range(0, BOARD_SIZE):
            for j in range(0, BOARD_SIZE):
                tile = Tile(BOARD[i][j],
                            ((GRID_TOPLEFT[0] + TILE_SIZE * j) + TILE_SIZE / 2,
                             (GRID_TOPLEFT[1] + TILE_SIZE * i) + TILE_SIZE / 2),
                            self.font, BOARD[i][j] != 0, i, j)
                tiles[i].append(tile)
        return tiles
    
    def draw_board(self):
        for i in range(0, len(self.tiles)):
            for j in range(0, len(self.tiles[0])):
                if self.tiles[i][j].row == self.loc[0] and self.tiles[i][j].col == self.loc[1]:
                    self.tiles[i][j].draw(self.screen, background_color=SELECTED_COLOR)
                else:
                    self.tiles[i][j].draw(self.screen)
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if self.can_move:
            if keys[pygame.K_RIGHT] and self.loc[1] < BOARD_SIZE - 1:
                self.loc[1] += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            if keys[pygame.K_LEFT] and self.loc[1] > 0:
                self.loc[1] -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            if keys[pygame.K_DOWN] and self.loc[0] < BOARD_SIZE - 1:
                self.loc[0] += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            if keys[pygame.K_UP] and self.loc[0] > 0:
                self.loc[0] -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            
            if keys[pygame.K_1]:
                self.tiles[self.loc[0]][self.loc[1]].temp_value = 1
            if keys[pygame.K_2]:
                self.tiles[self.loc[0]][self.loc[1]].temp_value = 2
            if keys[pygame.K_3]:
                self.tiles[self.loc[0]][self.loc[1]].temp_value = 3
            if keys[pygame.K_4]:
                self.tiles[self.loc[0]][self.loc[1]].temp_value = 4
            if keys[pygame.K_5]:
                self.tiles[self.loc[0]][self.loc[1]].temp_value = 5
            if keys[pygame.K_6]:
                self.tiles[self.loc[0]][self.loc[1]].temp_value = 6
            if keys[pygame.K_7]:
                self.tiles[self.loc[0]][self.loc[1]].temp_value = 7
            if keys[pygame.K_8]:
                self.tiles[self.loc[0]][self.loc[1]].temp_value = 8
            if keys[pygame.K_9]:
                self.tiles[self.loc[0]][self.loc[1]].temp_value = 9
            if keys[pygame.K_BACKSPACE] and not self.tiles[self.loc[0]][self.loc[1]].fixed:
                self.tiles[self.loc[0]][self.loc[1]].value = 0
                self.tiles[self.loc[0]][self.loc[1]].temp_value = 0
            if keys[pygame.K_RETURN] and self.tiles[self.loc[0]][self.loc[1]].temp_value != 0 and \
                self.tiles[self.loc[0]][self.loc[1]].value == 0:
                if self.tiles[self.loc[0]][self.loc[1]].temp_value == SOLUTION_BOARD[self.loc[0]][self.loc[1]]:
                    self.tiles[self.loc[0]][self.loc[1]].value = \
                        self.tiles[self.loc[0]][self.loc[1]].temp_value
                    self.tiles[self.loc[0]][self.loc[1]].temp_value = 0
                else:
                    self.tiles[self.loc[0]][self.loc[1]].temp_value = 0
                    
    
    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 100:
                self.can_move = True
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill(BACKGROUND_COLOR)
            
            self.input()
            self.selection_cooldown()
            
            self.draw_board()
            self.draw_grid()
            
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
