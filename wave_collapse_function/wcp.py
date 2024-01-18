import pygame
from pygame.locals import *

class Game:
    W = 1280
    H = 720
    SIZE = W, H

    def __init__(self, tileset_path, TILE_SIZE=32):
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SIZE)
        pygame.display.set_caption("Pygame Tiled Demo")
        self.tileset = pygame.image.load(tileset_path)
        self.TILE_SIZE = TILE_SIZE
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            self.load_map()
        pygame.quit()

    def load_map(self):
        # Create a 2D array to represent your map
        map_data = [
            [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2],
            [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2],
            [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2],
            [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2],
            # Add more rows here
        ]
            # Draw the map
        for y, row in enumerate(map_data):
            for x, tile_id in enumerate(row):
                # Calculate the position to blit the tile
                tile_x = x * self.TILE_SIZE
                tile_y = y * self.TILE_SIZE
                # Blit the tile from the tileset onto the screen
                self.screen.blit(self.tileset, (tile_x, tile_y), (tile_id * self.TILE_SIZE, 0, self.TILE_SIZE, self.TILE_SIZE))

        # Draw the grid
        for row in range(int(self.H/self.TILE_SIZE)):
            for col in range(int(self.W/self.TILE_SIZE)):
                x = col * self.TILE_SIZE
                y = row * self.TILE_SIZE
                pygame.draw.rect(self.screen, (255, 255, 255), (x, y, self.TILE_SIZE, self.TILE_SIZE), 1)  # 1 is the thickness of the grid lines
        # Update the display
        pygame.display.flip()


tileset_path = "C:\\Users\\Acer\\Desktop\\GITHUB_REPO\\silly-coding\\wave_collapse_function\\tiles\\tilemap.png"
game = Game(tileset_path,32)
game.run()