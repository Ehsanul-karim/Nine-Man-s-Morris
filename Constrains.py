import pygame
import numpy as np
import sys

pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nine Men Morris')

# Load logo
logo = pygame.image.load('E:\\4th year, 1st semester\\AI lab\\Images\\nineman.png')
pygame.display.set_icon(logo)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE_TRANSPARENT = (0, 0, 255, 128)
RECTANGLE_SIZE = 30

left_info_color = (200, 200, 200)
# Font
font = pygame.font.Font(None, 36)

position_1 = (15,12)
position_2 = (305,12)
position_3= (595,12)

position_4= (111,102)
position_5= (305,102)
position_6= (500,102)

position_7= (208,194)
position_8= (305,194)
position_9= (402,194)

position_10= (15,286)
position_11= (111,286)
position_12= (208,286)
position_13= (402,286)
position_14= (500,286)
position_15= (595,286)

position_16= (208,378)
position_17= (305,378)
position_18= (402,378)

position_19= (111,470)
position_20= (305,470)
position_21= (500,470)

position_22= (15,560)
position_23= (305,560)
position_24= (595,560)




positions = np.array([globals()[f"position_{i}"] for i in range(1, 25)])

# positions = [position_1,position_2]

# Function to display text
def display_text(text, x, y, color=BLACK, background=None, surface=None):
    text_surface = font.render(text, True, color, background)
    text_rect = text_surface.get_rect(center=(x, y))
    if surface is None:
        window.blit(text_surface, text_rect)
    else:
        surface.blit(text_surface, text_rect)