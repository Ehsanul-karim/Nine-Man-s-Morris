import pygame
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
BLACK = (0, 0, 0)
BLUE_TRANSPARENT = (0, 0, 255, 128)

left_info_color = (200, 200, 200)
# Font
font = pygame.font.Font(None, 36)

# Function to display text
def display_text(text, x, y, color=BLACK, background=None, surface=None):
    text_surface = font.render(text, True, color, background)
    text_rect = text_surface.get_rect(center=(x, y))
    if surface is None:
        window.blit(text_surface, text_rect)
    else:
        surface.blit(text_surface, text_rect)