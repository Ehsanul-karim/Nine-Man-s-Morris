from Constrains import *


# Define positions and dimensions for left side info
left_info_rect = pygame.Rect(0, 0, WINDOW_WIDTH * 0.2, WINDOW_HEIGHT)
left_info_color = (200, 200, 200)

# Define initial player information
white_count = 9
black_count = 9
point_white = 0
point_black = 0

def update_left_info():
    left_info_surface = pygame.Surface((WINDOW_WIDTH * 0.2, WINDOW_HEIGHT))
    left_info_surface.fill(left_info_color)
    # Display player information
    display_text('white: ' + str(white_count), WINDOW_WIDTH * 0.1, 50, color=BLACK, surface=left_info_surface)
    display_text('black: ' + str(black_count), WINDOW_WIDTH * 0.1, 100, color=BLACK, surface=left_info_surface)
    display_text('point_white: ' + str(point_white), WINDOW_WIDTH * 0.1, 150, color=BLACK, surface=left_info_surface)
    display_text('point_black: ' + str(point_black), WINDOW_WIDTH * 0.1, 200, color=BLACK, surface=left_info_surface)
    window.blit(left_info_surface, (0, 0))

# Main loop
def start():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                           
        # Update the display
        update_left_info()
        pygame.display.update()


def start():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                                
        # Clear the screen
        window.fill(WHITE)

        # Update the display
        pygame.display.update()