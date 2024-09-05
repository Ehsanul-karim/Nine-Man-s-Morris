import math
import functions as func
import Genetic_secondPhase as gen_sec

WHITE = 'W'
BLACK = 'B'
global parent_board
parent_board=[]

mills = [(0,1,2), (3,4,5), (6,7,8), (9,10,11), (12,13,14), (15,16,17), (18,19,20), (21,22,23),
                      (0,9,21), (3,10,18), (6,11,15), (1,4,7), (16,19,22), (8,12,17), (5,13,20), (2,14,23)]


def check_mill(board,move,player):
        for mill in mills:
            if move in mill:
                pos1, pos2, pos3 = mill
                if board[pos1] == board[pos2] == board[pos3] == player:
                    return True
        return False


def evalute(board, phase,parent_board):
     #print(board)
    score=0
    score = 95* func.closedMorris(parent_board,board) + 70 * func.differceInNumberOfMills(board) +  1 * func.differenceInClosedPeaces(board) + 70 * func.differceInPieces(board) +  10 * func.differenceIn2PeacesConfig(board) +  7 * func.differenceIn3PeacesConfig(board)
    #  print(score)
    return score

# def evaluate_board(board, phase,parent_board):
# 	result=0
# 	if phase == 'first_phase':
#         print("1")
# 		result = 18 * func.closedMorris(parent_board,board) + \
# 				 26 * func.differceInNumberOfMills(board) + \
# 				 1 * func.differenceInClosedPeaces(board) + \
# 				 6 * func.differceInPieces(board) + \
# 				 21 * func.differenceIn2PeacesConfig(board) + \
# 				 7 * func.differenceIn3PeacesConfig(board)

# 	elif phase == 'second_phase':
# 		result = 42 * func.closedMorris(parent_board,board) + \
# 				 28 * func.differceInNumberOfMills(board) + \
# 				 16 * func.differenceInClosedPeaces(board) + \
# 				 8 * func.differceInPieces(board) + \
# 				 25 * func.differenceInDoubleMorrises(board) + \
# 				 949 * func.winningConfiguration(board)

# 	elif phase == 'FLY':
# 		result = 23 * func.differenceIn2PeacesConfig(board) + \
# 				 21 * func.differenceIn3PeacesConfig(board) + \
# 				 5 * func.closedMorris(parent_board,board) + \
# 				 1120 * func.winningConfiguration(board)
    
	# return result
  


# def evaluate_board(board, player):
#     score = 0
#     player_pieces = 0
#     opponent_pieces = 0
#     for piece in board:
#         if piece == player:
#             player_pieces += 1
#         elif piece != ' ':
#             opponent_pieces += 1
#     score += (player_pieces - opponent_pieces)

#     player_mills = count_mills(board, player)
#     opponent_mills = count_mills(board, opponent(player))
#     score += (player_mills - opponent_mills)
#     return score

def get_first_black_piece(board):
    for i, cell in enumerate(board):
        if cell == 'B':
            return i

def generate_moves_for_kill(board,player_to_eat):
    moves = []
    for i, cell in enumerate(board):
        if cell == player_to_eat:
            moves.append(i)
    return moves

def make_kill(board, move, player_to_eat):
    new_board = board.copy()
    if new_board[move] == player_to_eat:
        new_board[move]=''
    return new_board

def generate_moves(board):
    moves = []
    for i, cell in enumerate(board):
        if cell == ' ':
            moves.append(i)
    return moves


def make_move(board, move, player):
    new_board = board.copy()
    new_board[move] = player
    return new_board

def count_black_white(board):
    black = 0
    white = 0
    for i, cell in enumerate(board):
        if cell == 'B':
            black+=1
        elif cell =='W':
            white+=1
    return black,white

def game_over(board):
    black,white=count_black_white(board)
    if black < 3 or white < 3:
        return True
    elif not generate_moves(board):
        return True
    else:
        return False

def first_phase_end(red_placed, white_placed):
    if white_placed ==9 and red_placed ==9:
        return True


def count_mills(board, player):
    mills = [(0,1,2), (3,4,5), (6,7,8), (9,10,11), (12,13,14), (15,16,17), (18,19,20), (21,22,23),
             (0,9,21), (3,10,18), (6,11,15), (1,4,7), (16,19,22), (8,12,17), (5,13,20), (2,14,23)]

    mill_count = 0
    for mill in mills:
        if all(board[pos] == player for pos in mill):
            mill_count += 1
    return mill_count

def opponent(player):
    return 'B' if player == 'W' else 'W'

def minimax_alpha_beta(board, depth, maximizing_player, alpha, beta, player,phase,parent_board,mill_found,red_placed,white_placed):
    if depth == 0 or game_over(board) or first_phase_end(red_placed,white_placed):
        return evalute(board,phase,parent_board)
        
    if mill_found:
        if maximizing_player:
            max_eval = -math.inf
            for move in generate_moves_for_kill(board,opponent(player)):
                parent_board=board.copy()
                new_board =  make_kill(board, move, opponent(player))    
                mill_found = False
                eval = minimax_alpha_beta(new_board, depth - 1, False, alpha, beta, player,phase,parent_board,mill_found,red_placed,white_placed)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval
        else:
            min_eval = math.inf
            for move in generate_moves_for_kill(board,player):
                parent_board=board.copy()
                new_board =  make_kill(board, move, player)    
                mill_found = False
                eval = minimax_alpha_beta(new_board, depth - 1, True, alpha, beta, player,phase,parent_board,mill_found,red_placed,white_placed)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval
    else:
        if maximizing_player:
            max_eval = -math.inf
            for move in generate_moves(board):
                parent_board=board.copy()
                new_board = make_move(board, move, player)
                red_placed+=1
                if check_mill(board,move,player):   
                    mill_found = True
                    eval = minimax_alpha_beta(new_board, depth , True, alpha, beta, player,phase,parent_board,mill_found,red_placed,white_placed)
                else:
                    mill_found = False
                    eval = minimax_alpha_beta(new_board, depth - 1, False, alpha, beta, player,phase,parent_board,mill_found,red_placed,white_placed)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval
        else:
            min_eval = math.inf
            for move in generate_moves(board):
                parent_board=board.copy()
                new_board = make_move(board, move, opponent(player))
                white_placed+=1
                if check_mill(board,move,opponent(player)):   
                    mill_found = True
                    eval = minimax_alpha_beta(new_board, depth, False, alpha, beta, player,phase,parent_board,mill_found,red_placed,white_placed)
                else:
                    mill_found = False
                    eval = minimax_alpha_beta(new_board, depth - 1, True, alpha, beta, player,phase,parent_board,mill_found,red_placed,white_placed)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval



def ai_move(board, depth, player,phase,mil,red_placed,white_placed):
    if mil==False:
        if phase==True:
            global parent_board
            best_move = None
            max_eval = -math.inf
            alpha = -math.inf
            beta = math.inf
            for move in generate_moves(board):
                parent_board=board.copy()
                new_board = make_move(board, move, player)
                red_placed+=1
                if check_mill(board,move,player):   
                    eval = minimax_alpha_beta(new_board, depth , True, alpha, beta, player,phase,parent_board,True,red_placed,white_placed)
                else:
                    eval = minimax_alpha_beta(new_board, depth - 1, False, alpha, beta, player,phase,parent_board,False,red_placed,white_placed)

                if eval > max_eval:
                    max_eval = eval
                    best_move = move
        else:
            best_move =  gen_sec.genetic_algorithm(board, player, depth+1)
    else:
        #intentionally ekta black piece er position return korbe.
        best_move = get_first_black_piece(board)

    return best_move


def ai_move_for_eat(board,depth,player,player_to_eat,phase_number,red_placed,white_placed):
    global parent_board
    best_move = None
    max_eval = -math.inf
    alpha = -math.inf
    beta = math.inf
    if phase_number == 1:
        phase = True
    else:
        phase = False

    for move in generate_moves_for_kill(board,player_to_eat):
        parent_board=board.copy()
        new_board =  make_kill(board, move, player_to_eat)
        eval = minimax_alpha_beta(new_board, depth - 1, False, alpha, beta, player,phase,parent_board,False,red_placed,white_placed)
        if eval > max_eval:
            max_eval = eval
            best_move = move


    return best_move
    