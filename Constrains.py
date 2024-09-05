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
logo = pygame.image.load('./Images/nineman.png')
pygame.display.set_icon(logo)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
option_height = 50  # Height of each option
BLUE_TRANSPARENT = (0, 0, 255, 128)
SOFT_GREEN = (102, 255, 102, 128)
RECTANGLE_SIZE = 30

left_info_color = (200, 200, 200)
# Font
font = pygame.font.Font(None, 36)

position_1 = (188, 28)
position_2 = (480, 26)
position_3= (770, 26)

position_4= (288, 121)
position_5= (484, 120)
position_6= (674, 121)

position_7= (384, 215)
position_8= (477, 213)
position_9= (578, 212)

position_10= (189, 300)
position_11= (286, 301)
position_12= (382, 302)
position_13= (575, 299)
position_14= (677, 301)
position_15= (778, 301)

position_16= (385, 386)
position_17= (481, 399)
position_18= (582, 387)

position_19= (287, 485)
position_20= (478, 484)
position_21= (676, 487)

position_22= (188, 577)
position_23= (478, 579)
position_24= (770, 578)




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