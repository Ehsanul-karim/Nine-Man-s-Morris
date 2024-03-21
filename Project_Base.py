from StartPage import start_game
from Constrains import *

# Options
options = ['Start', 'How to play', 'Gameplay', 'Settings' , 'Exit']
option_height = 50  # Height of each option
selected_option = 0  # Index of the currently selected option

# Main loop
def main():
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
                    if options[selected_option] == 'Exit':
                        pygame.quit()
                        sys.exit()
                    if options[selected_option] == 'Start':
                        start_game()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    for i, option in enumerate(options):
                        y = 200 + i * option_height
                        if pygame.Rect(WINDOW_WIDTH // 2 - 100, y - 25, 200, 50).collidepoint(mouse_x, mouse_y):
                            selected_option = i
                            if option == 'Exit':
                                pygame.quit()
                                sys.exit()
                            if option == 'Start':
                                start_game()
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


if __name__ == "__main__":
    print("Hello")
    main()