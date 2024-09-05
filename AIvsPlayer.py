from Constrains import *
import math
import minmax as mx
import functions as func
import min as alpha
import sys
from datetime import datetime

Total_number_of_move = 0
GREEN = (0, 255, 0)

RED = (255, 0, 0)
BLUE=(0,0,255)

# Define positions and dimensions for left side info
left_info_rect = pygame.Rect(0, 0, WINDOW_WIDTH * 0.2, WINDOW_HEIGHT)
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

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
 
def get_position_key(input_value, positions_dict):
    for key, value in positions_dict.items():
        if value == input_value:
            return key
    return None  # If input_value is not found in the dictionary

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
                element_index = positon.index(element)
                move_index = positon.index(move)
                if abs(element_index - move_index) == 1:
                    if is_valid_move(element):
                        coordinates = positions_for_Board['position_'+str(element+1)]
                        temp_available_spaces.append(list(coordinates))

    return temp_available_spaces

def search_white():
	move=0
	for i in range(24):
		move=move+i
		if(board[move]=='W'):
			break
	 	
	return move

def place_piece(move, player, phase_check = True):
        global phase1_pieces
        if phase_check:
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
        else:
                if is_valid_move(move):
                    board[move] = player
                    return True
                else:
                    print("Invalid move. Please try again.(p)")
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
    global black_turn, white_turn, start_ticks
    left_info_surface = pygame.Surface((WINDOW_WIDTH * 0.2, WINDOW_HEIGHT))
    left_info_surface.fill(left_info_color)
    # Display player information
    display_text('White: ' + str(white_placed), WINDOW_WIDTH * 0.1, 50, color=BLACK, surface=left_info_surface)
    display_text('Black: ' + str(red_placed), WINDOW_WIDTH * 0.1, 100, color=BLACK, surface=left_info_surface)
    display_text('Point B: ' + str(white_removed), WINDOW_WIDTH * 0.1, 150, color=BLACK, surface=left_info_surface)
    display_text('Point W: ' + str(red_removed), WINDOW_WIDTH * 0.1, 200, color=BLACK, surface=left_info_surface)
    
    
# Display the timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000  # Get elapsed time in seconds
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    time_display = f'{minutes:02}:{seconds:02}'  # Format as MM:SS

    display_text('Time:', WINDOW_WIDTH * 0.1, 250, color=BLACK, surface=left_info_surface)
    display_text(time_display, WINDOW_WIDTH * 0.1, 300, color=BLACK, surface=left_info_surface)

    display_text('Now Turn ', WINDOW_WIDTH * 0.1, 350, color=BLACK, surface=left_info_surface)
    if white_turn:
        display_text('White', WINDOW_WIDTH * 0.1, 400, color=BLACK, surface=left_info_surface)
    else:
        display_text('Black', WINDOW_WIDTH * 0.1, 400, color=BLACK, surface=left_info_surface)   
    window.blit(left_info_surface, (0, 0))
    return left_info_surface

def check_game_end():
    white_pieces = board.count('W')
    black_pieces = board.count('B')

    if white_pieces < 3:
        return 'AI Won!'
    elif black_pieces < 3:
        return 'You Won!'
    elif not any(is_valid_move(i) for i in range(24)):
        return 'Draw!'
    else:
        return None

def seconds_membership(crisp_second):
    degree = {}
    degree['very_early'] = 0
    degree['early'] = 0
    degree['ok'] = 0
    degree['late'] = 0
    degree['very_late'] = 0
    if 0<=crisp_second<15:
        degree['very_early'] = 1
    elif 15<=crisp_second<20:
        degree['very_early'] = (20-crisp_second)/(20-15)
        degree['early'] = (crisp_second-15)/(25-15)
    elif 20<=crisp_second<25:
        degree['early'] = (crisp_second-15)/(25-15)
    elif 25<=crisp_second<27:
        degree['early'] = (30-crisp_second)/(30-25)
    elif 27<=crisp_second<30:
        degree['early'] = (30-crisp_second)/(30-25)
        degree['ok'] = (crisp_second-27)/(34-27)
    elif 30<=crisp_second<34:
        degree['ok'] = (crisp_second-27)/(34-27)
    elif 34<=crisp_second<40:
        degree['ok'] = (40-crisp_second)/(40-34)
        degree['late'] = (crisp_second-34)/(45-34)
    elif 40<=crisp_second<45:
        degree['late'] = (crisp_second-34)/(45-34)
    elif 45<=crisp_second<55:
        degree['late'] = 1
    elif 55<=crisp_second<65:
        degree['late'] = (65-crisp_second)/(65-55)
        degree['very_late'] = (crisp_second-55)/(65-55)
    elif crisp_second>=65:
        degree['very_late'] = 1
    
    return degree
         

def total_number_move_membership(n):
    degree = {}
    degree['low'] = 0
    degree['avg'] = 0
    degree['huge'] = 0
    if 0<=n<7:
        degree['low'] = 1
    elif 7<=n<10:
        degree['low'] = (10-n)/(10-7)
        degree['avg'] = (n-7)/(10-7)
    elif 10<=n<11:
        degree['avg'] = (12-n)/(12-10)
    elif 11<=n<12:
        degree['avg'] = (12-n)/(12-10)
        degree['huge'] = (n-11)/(13-11)
    elif 12<=n<13:
        degree['huge'] = (n-11)/(13-11)
    elif n>=13:
        degree['huge'] = 1
    
    return degree

def guti_membership(n):
    degree = {}
    degree['poor'] = 0
    degree['good'] = 0
    degree['best'] = 0

    if 0<=n<3:
        degree['poor'] = 1
    elif 3<=n<5:
        degree['poor'] = (5-n)/(5-3)
        degree['good'] = (n-3)/(5-3)
    elif 5<=n<7:
        degree['good'] = (7-n)/(7-5)
        degree['best'] = (n-5)/(7-5)
    elif n>=7:
        degree['best'] = 1

    return degree

def evaluate_black_player_rating(sec_degree, M_degree, W_degree, B_degree):
    rating = {
        'worst': 0,
        'bad': 0,
        'moderate': 0,
        'good': 0,
        'excellent': 0
    }
    rating['excellent'] = max(
                        min(
                            min( max(B_degree['good'],B_degree['best']),max(W_degree['good'],W_degree['poor'])),max(max(sec_degree['very_early'],sec_degree['early']), max(M_degree['avg'],M_degree['low']))
                            ),
                        min(
                            min( B_degree['best'],max(W_degree['good'],W_degree['poor'])),max(max(sec_degree['ok'],sec_degree['early']), max(M_degree['avg'],M_degree['low']))
                            )
                        )
    
    rating['good'] = max(
                        min(
                            min( max(B_degree['good'],B_degree['best']),max(W_degree['good'],W_degree['poor'])),max(max(sec_degree['ok'],sec_degree['late']), max(M_degree['huge'],M_degree['avg']))
                            ),
                        min(
                            min( max(B_degree['good'],B_degree['best']),max(W_degree['good'],W_degree['poor'])),max(max(sec_degree['ok'],sec_degree['early']), max(M_degree['avg'],M_degree['low']))
                            )
                        )
    
    rating['moderate'] = max(
                            min(
                                min(max(B_degree['poor'],B_degree['good']),max(W_degree['best'],W_degree['good'])),min(max(sec_degree['late'],sec_degree['ok']), M_degree['huge'])
                                ),
                            min(
                                min(max(B_degree['poor'],B_degree['good']),max(W_degree['best'],W_degree['good'])),min(max(sec_degree['early'],sec_degree['ok']), M_degree['avg'])
                                )
                            )
    
    rating['bad'] =  max( 
                        max(
                            min(
                                max(B_degree['poor'],max(W_degree['best'],W_degree['good'])),max(sec_degree['late'], M_degree['huge'])
                                ),
                            min(
                                max(B_degree['poor'],max(W_degree['best'],W_degree['good'])),max(sec_degree['ok'], M_degree['huge'])
                                )
                            ),
                        max(
                            min(
                                max(B_degree['poor'], max(W_degree['best'],W_degree['good'])), max(sec_degree['late'], M_degree['avg'])
                               ),
                            min(
                                max(B_degree['poor'], max(W_degree['best'],W_degree['good'])), max(sec_degree['ok'], M_degree['avg'])
                                )
                            )
                        )
    
    rating['worst'] = max( 
                        max(
                            min(
                                max(B_degree['poor'], W_degree['best']),max(sec_degree['very_late'], M_degree['huge'])
                                ),
                            min(
                                max(B_degree['poor'], W_degree['best']),max(sec_degree['late'], M_degree['huge'])
                                )
                            ),
                        max(
                            min(
                                max(B_degree['poor'], W_degree['best']), max(sec_degree['very_late'], M_degree['avg'])
                               ),
                            min(
                                max(B_degree['poor'], W_degree['best']), max(sec_degree['late'], M_degree['avg'])
                                )
                            )
                        )    


    return rating

def find_fuzzy_score(time):
    score = 0
    crisp_second = (time - start_ticks) // 1000  # Get elapsed time in seconds
    print(crisp_second)
    sec_degree = seconds_membership(crisp_second)
    print(sec_degree)
    global Total_number_of_move
    M_degree = total_number_move_membership(Total_number_of_move)
    print(Total_number_of_move)
    print(M_degree)
    white_pieces = board.count('W')
    black_pieces = board.count('B')
    W_degree = guti_membership(white_pieces)
    print(white_pieces)
    print(W_degree)
    B_degree = guti_membership(black_pieces)
    print(black_pieces)
    print(B_degree)
    ratings_detail = evaluate_black_player_rating(sec_degree, M_degree, W_degree, B_degree)
    print(ratings_detail)
    values_list = np.array(list(ratings_detail.values())) * 100
    try:
        score  = ((values_list[0] * 40) + (values_list[1] * 50) + (values_list[2] * 60) + (values_list[3] * 70) + (values_list[4] * 80))/values_list.sum()
    except Exception as e:
        score = 0.6*100
    return score


# Function to display the end game message
# Function to display text at a specific position
def display_text(text, x, y, color, surface, font_size=32):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))  # Center the text
    surface.blit(text_surface, text_rect)

# Function to display the end game message
def display_end_game_message(message, time):
    fuzzy_score = find_fuzzy_score(time)
    end_game_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    end_game_surface.fill(WHITE)
    message += " AI Intelligence is "
    message += str(fuzzy_score)
    display_text(message, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, color=BLACK, surface=end_game_surface)
    window.blit(end_game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(3000)  # Show the message for 3 seconds
 # Show the message for 3 seconds

# Main loop
def start_2():
    global green_rect_pos
    green_rect_pos=None
    global red_rect_pos
    red_rect_pos=None
    global blue_rect_pos
    blue_rect_pos=None
    global cache_postion
    global phase1_pieces
    global white_removed, red_removed, white_placed, red_placed, Total_number_of_move
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
            
            print(board)
            if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            if white_turn:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                green_rect_pos = None
                                if event.button == 1:  # Left mouse button
                                    clicked_pos = event.pos
                                    closest_pos = closest_position(clicked_pos)
                                    
                                    if closest_pos is not None:
                                        #print("Clicked position:", clicked_pos)
                                        #print("Closest matched position:", closest_pos)
                                        move=pos_name(closest_pos)
                                        #print(move)
                                        #print(positions_for_cal.get(move))
                                        if first_phase == True:
                                            if place_piece(positions_for_cal.get(move),'W'):
                                                white_circle_positions.append(list(closest_pos))
                                                white_placed+=1
                                                Total_number_of_move+=1
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
                                                        print("Black Turn")
                                                        black_turn = True
                                                        white_turn = False
                                                        mil = False

                                        elif second_phase == True:
                                            if round_1:
                                                if is_he_here(positions_for_cal.get(move),'W'):
                                                    temp_available_spaces = show_available_position(positions_for_cal.get(move))
                                                    if temp_available_spaces is not None:
                                                        round_1 = False
                                                        cache_postion = closest_pos
                                                    else:
                                                        print("No vacancy. Choose another white")
                                                else:
                                                    print("White- Second Phase Running. Invalid move. Please try again.(p)")
                                            else:
                                                temp_available_spaces_np = np.array(temp_available_spaces)
                                                closest_pos_np = np.array(closest_pos)
                                                if any(np.array_equal(newpos, closest_pos_np) for newpos in temp_available_spaces_np):
                                                    remove=pos_name(cache_postion)
                                                    remove_piece(positions_for_cal.get(remove),'B') # B means, B can not present in that cell. It is obiously, as There must be White in that cell.
                                                    white_circle_positions.remove(list(cache_postion))

                                                    place_piece(positions_for_cal.get(move),'W',phase_check = False)
                                                    white_circle_positions.append(list(closest_pos))
                                                    Total_number_of_move+=1

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
                                                else:
                                                    temp_available_spaces.clear()
                                                    cache_postion = -1
                                                    round_1 = True
                                                    print("invalid Move by this white piece")
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
                              
                            move=mx.ai_move(board,4,'B',first_phase,mil,red_placed,white_placed)
                            
                            print(move)
                            if isinstance(move, tuple):
                                old_black, new_black = move
                                position_key_old = get_position_key(old_black, positions_for_cal)
                                position_key_new = get_position_key(new_black, positions_for_cal)
                                closest_pos_old=positions_for_Board.get(position_key_old) 
                                closest_pos_new=positions_for_Board.get(position_key_new) 

                            else:
                                position_key = get_position_key(move, positions_for_cal)
                                closest_pos=positions_for_Board.get(position_key) 
                                     
                            if first_phase == True:
                                
                                if place_piece(move,'B'):
                                    red_circle_positions.append(list(closest_pos))
                                    red_placed+=1
                                    if red_placed ==9 and white_placed==9:
                                        first_phase = False
                                        second_phase = True
                                    if check_mill(move,'B'):
                                        mil=True
                                        if second_phase:
                                            second_phase = False # Temporary
                                            mother = 2
                                        else:    
                                            first_phase = False 
                                            mother = 1
                                    else:
                                        black_turn = False
                                        white_turn = True
                                        mil = False

                            elif second_phase == True:
                                        
                                            #green_rect_pos = list(cache_postion)
                                            remove=pos_name(closest_pos_old)
                                            red_rect_pos=list(closest_pos_old)
                                            remove_piece(positions_for_cal.get(remove),'W') # W means, W can not present in that cell. It is obiously, as There must be Black in that cell.
                                            red_circle_positions.remove(list(closest_pos_old))

                                            place_piece(new_black,'B', phase_check = False)
                                            red_circle_positions.append(list(closest_pos_new))
                                            blue_rect_pos=list(closest_pos_new)
                                            if check_mill(new_black,'B'):
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
                            elif mil:
                                    # print(move)
                                    if(board[move]==' ' or board[move]=='B'):
                                        move=mx.ai_move_for_eat(board,4,'B','W',mother,red_placed,white_placed)
                                        position_key = get_position_key(move, positions_for_cal)
                                        closest_pos=positions_for_Board.get(position_key)
        
                                    if is_he_here(move,'W'):
                                        green_rect_pos = list(closest_pos)
                                        remove_piece(move,'B')
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
                                            print("Ai select Wrong Piece to kill")

        # Update the display
        left_info_surface = update_left_info()
        board_surface = display_board()
        if green_rect_pos is not None:
            pygame.draw.rect(board_surface, GREEN, (green_rect_pos[0]-173, green_rect_pos[1]-15, RECTANGLE_SIZE, RECTANGLE_SIZE), 2)
        
        if red_rect_pos is not None:
            pygame.draw.rect(board_surface, RED, (red_rect_pos[0]-173, red_rect_pos[1]-15, RECTANGLE_SIZE, RECTANGLE_SIZE), 2)
        if blue_rect_pos is not None:
            pygame.draw.rect(board_surface, BLUE, (blue_rect_pos[0]-173, blue_rect_pos[1]-15, RECTANGLE_SIZE, RECTANGLE_SIZE), 2)
        
        
        
        
        for pos in temp_available_spaces:  # Draw all the circles
            pygame.draw.rect(board_surface, BLACK, (pos[0]-173, pos[1]-15, RECTANGLE_SIZE, RECTANGLE_SIZE), 1)
            window.blit(board_surface, (WINDOW_WIDTH * 0.2, 0))

        # temp_available_spaces.clear()
        if second_phase == True:
            result = check_game_end()
            if result:
                elapsed_time = pygame.time.get_ticks()
                display_end_game_message(result, elapsed_time)
                break 

        for pos in red_circle_positions:  # Draw all the circles
            pygame.draw.circle(board_surface, RED, (pos[0]-160,pos[1]), 15)
            window.blit(board_surface, (WINDOW_WIDTH * 0.2, 0))
        for pos in white_circle_positions:  # Draw all the circles
            pygame.draw.circle(board_surface, WHITE, (pos[0]-160,pos[1]), 15)
            window.blit(board_surface, (WINDOW_WIDTH * 0.2, 0))
        # board_surface = show_push_places(board_surface)
        pygame.display.update()
        clock.tick(60)

# start()

# ['B', 'B', 'W', 'B', 'W', 'W', 'W', 'B', ' ', 'B', ' ', 'B', 'B', 'W', 'W', ' ', 'W', ' ', ' ', 'W', 'B', ' ', ' ', 'W']
# ['B', 'B', ' ', ' ', 'W', 'W', 'W', 'B', ' ', 'B', 'B', 'B', 'B', 'W', 'W', ' ', 'W', ' ', ' ', 'W', 'B', ' ', ' ', 'W']
# [' ', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', 'B', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W']