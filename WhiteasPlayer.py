from Constrains import *


# Define positions and dimensions for left side info
left_info_rect = pygame.Rect(0, 0, WINDOW_WIDTH * 0.2, WINDOW_HEIGHT)


# Define initial player information
white_count = 9
black_count = 9
point_white = 0
point_black = 0

black_turn = False
white_turn = True


def display_board():
    board_surface = pygame.Surface((WINDOW_WIDTH * 0.8, WINDOW_HEIGHT))
    board_image = pygame.image.load('E:\\4th year, 1st semester\\Nine-Man-s-Morris\\Images\\Board.png')
    board_image = pygame.transform.scale(board_image, (int(WINDOW_WIDTH * 0.8), WINDOW_HEIGHT))    
    board_surface.blit(board_image, (0, 0))
    for pos in positions:
        pygame.draw.rect(board_surface, BLACK, (pos[0], pos[1], RECTANGLE_SIZE, RECTANGLE_SIZE), 1)
    window.blit(board_surface, (WINDOW_WIDTH * 0.2, 0))
    return board_surface

def update_left_info():
    global black_turn, white_turn
    left_info_surface = pygame.Surface((WINDOW_WIDTH * 0.2, WINDOW_HEIGHT))
    left_info_surface.fill(left_info_color)
    # Display player information
    display_text('White: ' + str(white_count), WINDOW_WIDTH * 0.1, 50, color=BLACK, surface=left_info_surface)
    display_text('Black: ' + str(black_count), WINDOW_WIDTH * 0.1, 100, color=BLACK, surface=left_info_surface)
    display_text('Point W: ' + str(point_white), WINDOW_WIDTH * 0.1, 150, color=BLACK, surface=left_info_surface)
    display_text('Point B: ' + str(point_black), WINDOW_WIDTH * 0.1, 200, color=BLACK, surface=left_info_surface)
    display_text('Now Turn ', WINDOW_WIDTH * 0.1, 250, color=BLACK, surface=left_info_surface)
    if white_turn:
        display_text('White', WINDOW_WIDTH * 0.1, 300, color=BLACK, surface=left_info_surface)
    else:
        display_text('Black', WINDOW_WIDTH * 0.1, 300, color=BLACK, surface=left_info_surface)   
    window.blit(left_info_surface, (0, 0))
    return left_info_surface


# Main loop
def start():
    global black_turn, white_turn
    window.fill(WHITE)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if white_turn:
                        black_turn = True
                        white_turn = False
                    else:
                        black_turn = False
                        white_turn = True
                           
        # Update the display
        left_info_surface = update_left_info()
        board_surface = display_board()
        # board_surface = show_push_places(board_surface)
        pygame.display.update()

start()