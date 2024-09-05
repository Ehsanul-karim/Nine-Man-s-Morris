# Possible mills on the board
import math

mills = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11),
    (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
    (0, 9, 21), (3, 10, 18), (6, 11, 15), (1, 4, 7),
    (16, 19, 22), (8, 12, 17), (5, 13, 20), (2, 14, 23)
]

# Adjacency list for the board positions
adjacency_list = {
    0: [1, 9], 1: [0, 2, 4], 2: [1, 14],
    3: [4, 10], 4: [1, 3, 5, 7], 5: [4, 13],
    6: [7, 11], 7: [4, 6, 8], 8: [7, 12],
    9: [0, 10, 21], 10: [3, 9, 11, 18], 11: [6, 10, 15],
    12: [8, 13, 17], 13: [5, 12, 14, 20], 14: [2, 13, 23],
    15: [11, 16], 16: [15, 17, 19], 17: [12, 16],
    18: [10, 19], 19: [16, 18, 20, 22], 20: [13, 19],
    21: [9, 22], 22: [19, 21, 23], 23: [14, 22]
}

def is_mill(board, pos, player):
    for mill in mills:
        if pos in mill and all(board[p] == player for p in mill):
            return True
    return False

def get_possible_moves(board, player):
    moves = []
    for i in range(24):
        if board[i] == player:
            for adj in adjacency_list[i]:
                if board[adj] == '-':
                    new_board = board[:]
                    new_board[i] = '-'
                    new_board[adj] = player
                    moves.append(new_board)
    return moves

def evaluate_board(board):
    # Count the number of pieces for each player
    player_pieces = board.count('X')
    opponent_pieces = board.count('O')

    # Evaluate the number of mills each player has
    player_mills = sum(1 for mill in mills if all(board[pos] == 'X' for pos in mill))
    opponent_mills = sum(1 for mill in mills if all(board[pos] == 'O' for pos in mill))

    # Evaluate the number of possible mills each player can form
    player_potential_mills = sum(1 for mill in mills if any(board[pos] == '-' for pos in mill) and sum(board[pos] == 'X' for pos in mill) == 2)
    opponent_potential_mills = sum(1 for mill in mills if any(board[pos] == '-' for pos in mill) and sum(board[pos] == 'O' for pos in mill) == 2)

    # Evaluate strategic positioning based on adjacency
    player_positions = sum(1 for pos in range(24) if board[pos] == 'X' and any(board[adj] == 'X' for adj in adjacency_list[pos]))
    opponent_positions = sum(1 for pos in range(24) if board[pos] == 'O' and any(board[adj] == 'O' for adj in adjacency_list[pos]))

    # Combine evaluations into a single score
    score = (
        10 * (player_pieces - opponent_pieces) +
        15 * (player_mills - opponent_mills) +
        5 * (player_potential_mills - opponent_potential_mills) +
        3 * (player_positions - opponent_positions)
    )
    
    return score

def minimax(board, depth, is_maximizing_player, alpha, beta):
    if depth == 0:
        return evaluate_board(board)

    if is_maximizing_player:
        max_eval = -math.inf
        for move in get_possible_moves(board,'B' ):
            eval = minimax(move, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_possible_moves(board, 'W'):
            eval = minimax(move, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
    



def ai_move(board, depth, player):
    best_move = None
    max_eval = -math.inf
    alpha = -math.inf
    beta = math.inf
    for move in get_possible_moves(board,player):
        eval = minimax(move, depth - 1, False, alpha, beta)
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move