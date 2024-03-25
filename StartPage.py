from Constrains import *
from WhiteasPlayer import start
# from BlackasPlayer import start_2

# Options
options = ['Play as White', 'Play as Black']
option_height = 50  # Height of each option
selected_option = 0  # Index of the currently selected option

def start_game():
    selected_option = 0  # Initialize the selected option
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:  # Enter key
                    if options[selected_option] == 'Play as White':

                        start()
                    if options[selected_option] == 'Play as Black':
                        start_2()
                        


            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    for i, option in enumerate(options):
                        y = 200 + i * option_height
                        if pygame.Rect(WINDOW_WIDTH // 2 - 100, y - 25, 200, 50).collidepoint(mouse_x, mouse_y):
                            selected_option = i
                            if option == 'Play as White':
                                start()
                            if option == 'Play as Black':
                                start_2()
                                
        # Clear the screen
        window.fill(WHITE)

        # Display options
        for i, option in enumerate(options):
            y = 200 + i * option_height
            if i == selected_option:
                display_text(option, WINDOW_WIDTH // 2, y, BLACK, BLUE_TRANSPARENT)
            else:
                display_text(option, WINDOW_WIDTH // 2, y)

        # Update the display
        pygame.display.update()