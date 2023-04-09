import numpy as np
from PIL import Image, ImageFilter
import random
import ctypes
import os

# larger number corresponds to smaller tile size
tile_size = random.randint(2,8)
BLOCK_HEIGHT = int(2160/tile_size)
BLOCK_WIDTH = int(3840/tile_size)
BLUR_STRENGTH = 500

# color palette
BLACK = (0, 0, 0)
black_block = np.full((BLOCK_HEIGHT, BLOCK_WIDTH, 3), BLACK, dtype=np.uint8)

WHITE = (255, 255, 255)
white_block = np.full((BLOCK_HEIGHT, BLOCK_WIDTH, 3), WHITE, dtype=np.uint8)

rgb_1 = (random.randint(255,256), random.randint(0,256), random.randint(0,1))
rgb_1_block = np.full((BLOCK_HEIGHT, BLOCK_WIDTH, 3), rgb_1, dtype=np.uint8)

rgb_2 = (random.randint(0,256), random.randint(255,256), random.randint(0,1))
rgb_2_block = np.full((BLOCK_HEIGHT, BLOCK_WIDTH, 3), rgb_2, dtype=np.uint8)

rgb_3 = (random.randint(0,1), random.randint(255,256), random.randint(0,256))
rgb_3_block = np.full((BLOCK_HEIGHT, BLOCK_WIDTH, 3), rgb_3, dtype=np.uint8)

rgb_4 = (random.randint(0,1), random.randint(0,256), random.randint(255,256))
rgb_4_block = np.full((BLOCK_HEIGHT, BLOCK_WIDTH, 3), rgb_4, dtype=np.uint8)

rgb_5 = (random.randint(0,256), random.randint(0,1), random.randint(255,256))
rgb_5_block = np.full((BLOCK_HEIGHT, BLOCK_WIDTH, 3), rgb_5, dtype=np.uint8)

rgb_6 = (random.randint(255,256), random.randint(0,1), random.randint(0,256))
rgb_6_block = np.full((BLOCK_HEIGHT, BLOCK_WIDTH, 3), rgb_6, dtype=np.uint8)

block_choice = [
    black_block,
    white_block, 
    rgb_1_block, rgb_2_block, rgb_3_block, rgb_4_block, rgb_5_block, rgb_6_block,
]

block_list = []
block_mosaic = []

for column in range (tile_size):
    for row in range (tile_size):
        block_list.append(random.choice(block_choice))
    block_mosaic.append(np.hstack(block_list))
    block_list = []

block_mosaic_sharp = Image.fromarray(np.vstack(block_mosaic), "RGB")
block_mosaic_gradient = block_mosaic_sharp.filter(ImageFilter.GaussianBlur(radius=BLUR_STRENGTH))

# save the numpy array as image
image_filename = "wallpaper_sharp.jpeg"
block_mosaic_sharp.save(image_filename)

image_filename = "wallpaper_gradient.jpeg"
block_mosaic_gradient.save(image_filename)

SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath("wallpaper_gradient.jpeg"), 0)
