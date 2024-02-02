import pygame
import numpy as np
from pygame.locals import *

class Game:
    W = 1280
    H = 720
    SIZE = W, H

    def __init__(self, tileset_path):
        pygame.init()
        self.tileMap = TileMap(tileset_path)
        self.screen = pygame.display.set_mode(Game.SIZE)
        pygame.display.set_caption("Pygame Tiled Demo")
        self.TILE_SIZE = self.tileMap.TILE_SIZE
        self.running = True
        self.HEIGTH = int(self.H / self.TILE_SIZE)
        self.WIDTH = int(self.W / self.TILE_SIZE)
        self.map_data = np.full((self.HEIGTH, self.WIDTH),5)


    def run(self):
        self.load_map()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
        pygame.quit()


    def load_map(self):
        # Create a 2D array to represent your map
        print(self.map_data)
        tile_x = np.random.randint(0,self.WIDTH) * self.TILE_SIZE
        tile_y = np.random.randint(0,self.HEIGTH) * self.TILE_SIZE
        random_tile_id = np.random.randint(0,4)
        self.screen.blit(self.tileMap.tileset, (tile_x, tile_y),(random_tile_id * self.TILE_SIZE, 0, self.TILE_SIZE, self.TILE_SIZE))
        
        #print(f"tile_x: {tile_x}, tile_y: {tile_y}, tile_id: {tile_id}""")
        # Draw the grid
        for row in range(self.HEIGTH):
            for col in range(self.WIDTH):
                x = col * self.TILE_SIZE
                y = row * self.TILE_SIZE
                pygame.draw.rect(self.screen, (255, 255, 255), (x, y, self.TILE_SIZE, self.TILE_SIZE), 1)  # 1 is the thickness of the grid lines
                font = pygame.font.Font(None, 20)  # You can change the font and size
                text = font.render(f'{self.map_data[row][col]}', True, (255, 255, 255))  # Create text surface
                text_rect = text.get_rect(center=(x + self.TILE_SIZE // 2, y + self.TILE_SIZE // 2))  # Center text
                self.screen.blit(text, text_rect)  # Blit text onto the screen

        # Update the display
        pygame.display.flip()

    def calculate_entropy(self):
        pass
        

class TileMap:
    def __init__ (self, tileset_path, TILE_SIZE=32):
        # first is left side, then clockwise
        self.TILE_0_RULE = [(0,1,3),(0,3,4),(0,2,4),(0,1,2)]
        self.TILE_1_RULE = [(2,4),(0,3,4),(0,2,4),(3,4)]
        self.TILE_2_RULE = [(0,1,3),(0,3,4),(1,3),(0,1,3)]
        self.TILE_3_RULE = [(2,4),(1,2),(0,2,4),(0,1,2)]
        self.TILE_4_RULE = [(0,1,3),(1,2),(1,3),(0,1,2)]
        self.TILE_RULES = [self.TILE_0_RULE, self.TILE_1_RULE, self.TILE_2_RULE, self.TILE_3_RULE, self.TILE_4_RULE]
        self.TILE_SIZE = TILE_SIZE
        self.tileset = pygame.image.load(tileset_path)




tileset_path = "C:\\Users\\Acer\\Desktop\\GITHUB_REPO\\silly-coding\\wave_collapse_function\\tiles\\tilemap.png"
game = Game(tileset_path,32)
game.run()

