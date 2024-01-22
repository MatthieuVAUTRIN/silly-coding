import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32  # Adjust this to match your tile size
MAP_WIDTH = 20  # Adjust this to match your map dimensions
MAP_HEIGHT = 15

# Load the tileset image
tileset = pygame.image.load("C:\\Users\\Acer\\Desktop\\GITHUB_REPO\\silly-coding\\wave_collapse_function\\tiles\\tilemap.png")

# Create a 2D array to represent your map
map_data = [
    [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2],
    [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2],
    [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2],

    [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2],

    # Add more rows here
]

# Initialize the Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tilemap Example")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the map
    for y, row in enumerate(map_data):
        for x, tile_id in enumerate(row):
            # Calculate the position to blit the tile
            tile_x = x * TILE_SIZE
            tile_y = y * TILE_SIZE
            print(f"tile_x: {tile_x}, tile_y: {tile_y}, tile_id: {tile_id}""")

            # Blit the tile from the tileset onto the screen
            screen.blit(tileset, (tile_x, tile_y), (tile_id * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
