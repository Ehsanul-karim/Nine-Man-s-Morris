import math

WHITE = 'W'
BLACK = 'B'

def evaluate_board(board, player):
    score = 0
    player_pieces = 0
    opponent_pieces = 0
    for piece in board:
        if piece == player:
            player_pieces += 1
        elif piece != ' ':
            opponent_pieces += 1
    score += (player_pieces - opponent_pieces)

    player_mills = count_mills(board, player)
    opponent_mills = count_mills(board, opponent(player))
    score += (player_mills - opponent_mills)
    print(score)
    return score

def count_mills(board, player):
    mills = [(0,1,2), (3,4,5), (6,7,8), (9,10,11), (12,13,14), (15,16,17), (18,19,20), (21,22,23),
             (0,9,21), (3,10,18), (6,11,15), (1,4,7), (16,19,22), (8,12,17), (5,13,20), (2,14,23)]

    mill_count = 0
    for mill in mills:
        if all(board[pos] == player for pos in mill):
            mill_count += 1
    return mill_count

def opponent(player):
    return BLACK if player == WHITE else WHITE

def minimax_alpha_beta(board, depth, maximizing_player, alpha, beta, player):
    print("Minimax")
    if depth == 0 or game_over(board):
        return evaluate_board(board, player)

    if maximizing_player:
        max_eval = -math.inf
        for move in generate_moves(board):
            new_board = make_move(board, move, player)
            eval = minimax_alpha_beta(new_board, depth - 1, False, alpha, beta, player)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for move in generate_moves(board):
            new_board = make_move(board, move, opponent(player))
            eval = minimax_alpha_beta(new_board, depth - 1, True, alpha, beta, player)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

def generate_moves(board):
    moves = []
    for i, cell in enumerate(board):
        if cell == ' ':
            moves.append(i)
    return moves

def make_move(board, move, player):
    new_board = list(board)
    new_board[move] = player
    return new_board

def game_over(board):
    white_count = board.count(WHITE)
    black_count = board.count(BLACK)
    if white_count < 3 or black_count < 3:
        return True
    elif not generate_moves(board):
        return True
    else:
        return False

def ai_move(board, depth, player):
    best_move = None
    max_eval = -math.inf
    alpha = -math.inf
    beta = math.inf

    for move in generate_moves(board):
        new_board = make_move(board, move, player)
        eval = minimax_alpha_beta(new_board, depth - 1, False, alpha, beta, player)
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move
