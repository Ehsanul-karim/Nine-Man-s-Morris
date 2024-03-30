from Constrains import *
import math

# Define positions and dimensions for left side info
left_info_rect = pygame.Rect(0, 0, WINDOW_WIDTH * 0.2, WINDOW_HEIGHT)


# Define initial player information
white_placed = 0
red_placed = 0
white_removed = 0
red_removed = 0

cache_postion = -1

black_turn = False
white_turn = True
global phase1_pieces
phase1_pieces = 18

board=[' ']*24

positions_for_Board = {
    'position_1': [188, 28], 'position_2': [480, 26], 'position_3': [770, 26],
    'position_4': [288, 121], 'position_5': [484, 120], 'position_6': [674, 121],
    'position_7': [384, 215], 'position_8': [477, 213], 'position_9': [578, 212],
    'position_10': [189, 300], 'position_11': [286, 301], 'position_12': [382, 302],
    'position_13': [575, 299], 'position_14': [677, 301], 'position_15': [778, 301],
    'position_16': [385, 386], 'position_17': [481, 399], 'position_18': [582, 387],
    'position_19': [287, 485], 'position_20': [478, 484], 'position_21': [676, 487],
    'position_22': [188, 577], 'position_23': [478, 579], 'position_24': [770, 578]
}

positions_for_cal = {
    'position_1' : 0, 'position_2' : 1, 'position_3' : 2,
    'position_4': 3, 'position_5': 4, 'position_6': 5,
    'position_7': 6, 'position_8': 7, 'position_9': 8,
    'position_10': 9, 'position_11': 10, 'position_12': 11,
    'position_13': 12, 'position_14': 13, 'position_15': 14,
    'position_16': 15, 'position_17': 16, 'position_18': 17,
    'position_19': 18, 'position_20': 19, 'position_21': 20,
    'position_22': 21, 'position_23': 22, 'position_24': 23
}



def closest_position(clicked_pos):
    min_distance = float('inf')
    closest_pos = None
    for  pos in positions:
        distance = math.sqrt((clicked_pos[0] - pos[0])**2 + (clicked_pos[1] - pos[1])**2)
        if distance < min_distance and distance<=10:
            min_distance = distance
            closest_pos = pos
    return closest_pos  

def pos_name(pos):
    for key, value in positions_for_Board.items():
        list_equals_array = all(x == y for x, y in zip(value, pos))
        if list_equals_array:
            return key

mills = [(0,1,2), (3,4,5), (6,7,8), (9,10,11), (12,13,14), (15,16,17), (18,19,20), (21,22,23),
                      (0,9,21), (3,10,18), (6,11,15), (1,4,7), (16,19,22), (8,12,17), (5,13,20), (2,14,23)]

def is_valid_move(move):
        if board[move] == ' ':
            return True
        return False

def is_he_here(move,player):
        if board[move] == player:
            return True
        return False

def check_mill(move,player):
        for mill in mills:
            if move in mill:
                pos1, pos2, pos3 = mill
                if board[pos1] == board[pos2] == board[pos3] == player:
                    return True
        return False

def show_available_position(move):
    temp_available_spaces = []
    for positon in mills:
        if move in positon:
            for element in positon:
                if is_valid_move(element):
                    coordinates = positions_for_Board['position_'+str(element+1)]
                    temp_available_spaces.append(list(coordinates))

    return temp_available_spaces


def place_piece(move, player):
        global phase1_pieces
        if phase1_pieces > 0:
            if is_valid_move(move):
                board[move] = player
                phase1_pieces -= 1
                return True
            else:
                print("Invalid move. Please try again.(p)")
                return False
        else:
            # print("All pieces have been placed. Please proceed to the next phase.")
            return False

def remove_piece(move,player):
        global phase1_pieces
        if board[move] != ' ' and board[move] !=player:
            board[move] = ' '
            # phase1_pieces -= 1
        else:
            print("Invalid move. Please try again.(r)")
            

def display_board():
    board_surface = pygame.Surface((WINDOW_WIDTH * 0.8, WINDOW_HEIGHT))
    board_image = pygame.image.load('./Images/Board.png')
    board_image = pygame.transform.scale(board_image, (int(WINDOW_WIDTH * 0.8), WINDOW_HEIGHT))    
    board_surface.blit(board_image, (0, 0))
    #for pos in positions:
      #pygame.draw.rect(board_surface, BLACK, (pos[0], pos[1], RECTANGLE_SIZE, RECTANGLE_SIZE), 1)
    window.blit(board_surface, (WINDOW_WIDTH * 0.2, 0))
    return board_surface


def update_left_info():
    global black_turn, white_turn
    left_info_surface = pygame.Surface((WINDOW_WIDTH * 0.2, WINDOW_HEIGHT))
    left_info_surface.fill(left_info_color)
    # Display player information
    display_text('White: ' + str(white_placed), WINDOW_WIDTH * 0.1, 50, color=BLACK, surface=left_info_surface)
    display_text('Black: ' + str(red_placed), WINDOW_WIDTH * 0.1, 100, color=BLACK, surface=left_info_surface)
    display_text('Point B: ' + str(white_removed), WINDOW_WIDTH * 0.1, 150, color=BLACK, surface=left_info_surface)
    display_text('Point W: ' + str(red_removed), WINDOW_WIDTH * 0.1, 200, color=BLACK, surface=left_info_surface)
    display_text('Now Turn ', WINDOW_WIDTH * 0.1, 250, color=BLACK, surface=left_info_surface)
    if white_turn:
        display_text('White', WINDOW_WIDTH * 0.1, 300, color=BLACK, surface=left_info_surface)
    else:
        display_text('Black', WINDOW_WIDTH * 0.1, 300, color=BLACK, surface=left_info_surface)   
    window.blit(left_info_surface, (0, 0))
    return left_info_surface



# Main loop
def start():
    global cache_postion
    global phase1_pieces
    global white_removed, red_removed, white_placed, red_placed
    phase1_pieces= 18
    temp_available_spaces = []
    red_circle_positions = []
    white_circle_positions=[]
    global black_turn, white_turn
    window.fill(WHITE)
    round_1 = True
    second_phase = False
    first_phase = True
    mother = -1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    clicked_pos = event.pos
                    closest_pos = closest_position(clicked_pos)
                    if closest_pos is not None:
                        print("Clicked position:", clicked_pos)
                        print("Closest matched position:", closest_pos)
                        move=pos_name(closest_pos)

                        print(positions_for_cal.get(move))
                        if white_turn:
                            if first_phase == True:
                                if place_piece(positions_for_cal.get(move),'W'):
                                    white_circle_positions.append(list(closest_pos))
                                    white_placed+=1
                                    if white_placed ==9 and red_placed ==9:
                                        second_phase = True
                                        first_phase = False
                                    if check_mill(positions_for_cal.get(move),'W'):
                                        mil=True
                                        if second_phase:
                                            second_phase = False # Temporary
                                            mother = 2
                                        else:    
                                            first_phase = False # Temporary
                                            mother = 1
                                    else:
                                        black_turn = True
                                        white_turn = False
                                        mil = False

                            elif second_phase == True:
                                if round_1:
                                    if is_he_here(positions_for_cal.get(move),'W'):
                                        print("White Found")
                                        temp_available_spaces = show_available_position(positions_for_cal.get(move))
                                        if temp_available_spaces is not None:
                                            round_1 = False
                                            cache_postion = closest_pos
                                        else:
                                            print("No vacancy. Choose another white")
                                    else:
                                        print("White- Second Phase Running. Invalid move. Please try again.(p)")
                                else:
                                    remove=pos_name(cache_postion)
                                    remove_piece(positions_for_cal.get(remove),'B') # B means, B can not present in that cell. It is obiously, as There must be White in that cell.
                                    white_circle_positions.remove(list(cache_postion))

                                    place_piece(positions_for_cal.get(move),'W')
                                    white_circle_positions.append(list(closest_pos))

                                    temp_available_spaces.clear()
                                    cache_postion = -1

                                    if check_mill(positions_for_cal.get(move),'W'):
                                        mil=True
                                        if second_phase:
                                            second_phase = False # Temporary
                                            mother = 2
                                        else:    
                                            first_phase = False # Temporary
                                            mother = 1
                                    else:
                                        black_turn = True
                                        white_turn = False
                                        mil = False
                                    round_1 = True
                            elif mil:
                                if is_he_here(positions_for_cal.get(move),'B'):
                                    remove_piece(positions_for_cal.get(move),'W')
                                    red_circle_positions.remove(list(closest_pos))
                                    red_removed+=1
                                    black_turn = True
                                    white_turn = False
                                    mil = False
                                    if mother == 1:
                                        first_phase = True # Turn on again
                                        second_phase = False
                                    elif mother == 2:
                                        first_phase = False
                                        second_phase = True # Turn on again
                                else:
                                    print("Select a black piece to kill")
                        else:
                            if first_phase == True:
                                if place_piece(positions_for_cal.get(move),'B'):
                                    red_circle_positions.append(list(closest_pos))
                                    red_placed+=1
                                    if red_placed ==9 and white_placed==9:
                                        first_phase = False
                                        second_phase = True
                                    if check_mill(positions_for_cal.get(move),'B'):
                                        mil=True
                                        if second_phase:
                                            second_phase = False # Temporary
                                            mother = 2
                                        else:    
                                            first_phase = False # Temporary
                                            mother = 1
                                    else:
                                        black_turn = False
                                        white_turn = True
                                        mil = False

                            elif second_phase == True:
                                if round_1:
                                    if is_he_here(positions_for_cal.get(move),'B'):
                                        print('black found')
                                        temp_available_spaces = show_available_position(positions_for_cal.get(move))
                                        if temp_available_spaces is not None:
                                            round_1 = False
                                            cache_postion = closest_pos
                                        else:
                                            print("No vacancy. Choose another red")
                                    else:
                                        print("Black- Second Phase Running. Invalid move. Please try again.(p)")
                                else:
                                    remove=pos_name(cache_postion)
                                    remove_piece(positions_for_cal.get(remove),'W')
                                    red_circle_positions.remove(list(cache_postion))

                                    place_piece(positions_for_cal.get(move),'B')
                                    red_circle_positions.append(list(closest_pos))

                                    temp_available_spaces.clear()
                                    cache_postion = -1

                                    if check_mill(positions_for_cal.get(move),'B'):
                                        mil=True
                                        if second_phase:
                                            second_phase = False # Temporary
                                            mother = 2
                                        else:    
                                            first_phase = False # Temporary
                                            mother = 1
                                    else:
                                        black_turn = False
                                        white_turn = True
                                        mil = False
                                    round_1 = True
                            elif mil:
                                if is_he_here(positions_for_cal.get(move),'W'):
                                    remove_piece(positions_for_cal.get(move),'B')
                                    white_circle_positions.remove(list(closest_pos))
                                    white_removed+=1
                                    black_turn = False
                                    white_turn = True
                                    mil = False
                                    if mother == 1:
                                        first_phase = True # Turn on again
                                        second_phase = False
                                    elif mother == 2:
                                        first_phase = False
                                        second_phase = True # Turn on again
                                else:
                                    print("Select a white piece to kill")

        # Update the display
        left_info_surface = update_left_info()
        board_surface = display_board()
        for pos in temp_available_spaces:  # Draw all the circles
            pygame.draw.rect(board_surface, BLACK, (pos[0]-173, pos[1]-15, RECTANGLE_SIZE, RECTANGLE_SIZE), 1)
            window.blit(board_surface, (WINDOW_WIDTH * 0.2, 0))

        # temp_available_spaces.clear()

        for pos in red_circle_positions:  # Draw all the circles
            pygame.draw.circle(board_surface, RED, (pos[0]-160,pos[1]), 15)
            window.blit(board_surface, (WINDOW_WIDTH * 0.2, 0))
        for pos in white_circle_positions:  # Draw all the circles
            pygame.draw.circle(board_surface, WHITE, (pos[0]-160,pos[1]), 15)
            window.blit(board_surface, (WINDOW_WIDTH * 0.2, 0))
        # board_surface = show_push_places(board_surface)
        pygame.display.update()

start()