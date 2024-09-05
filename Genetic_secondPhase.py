import random
import math
import functions as func
import copy
import random
from collections import Counter
import numpy as np
import cv2

millions = [(0,1,2), (3,4,5), (6,7,8), (9,10,11), (12,13,14), (15,16,17), (18,19,20), (21,22,23),
                      (0,9,21), (3,10,18), (6,11,15), (1,4,7), (16,19,22), (8,12,17), (5,13,20), (2,14,23)]


MILLS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
         (0, 9, 21), (3, 10, 18), (6, 11, 15), (1, 4, 7), (16, 19, 22), (8, 12, 17), (5, 13, 20), (2, 14, 23))

PEACEINMILL = {0: [(1, 2), (9, 21)], 1: [(0, 2), (4, 7)], 2: [(0, 1), (14, 23)], 3: [(4, 5), (10, 18)],
               4: [(3, 5), (1, 7)],
               5: [(13, 20), (3, 4)], 6: [(7, 8), (11, 15)], 7: [(1, 4), (6, 8)], 8: [(6, 7), (12, 17)],
               9: [(0, 21), (10, 11)],
               10: [(9, 11), (3, 18)], 11: [(15, 6), (9, 10)], 12: [(8, 17), (13, 14)], 13: [(12, 14), (5, 20)],
               14: [(2, 23), (12, 13)],
               15: [(16, 17), (11, 6)], 16: [(15, 17), (19, 22)], 17: [(12, 8), (15, 16)], 18: [(3, 10), (19, 20)],
               19: [(18, 20), (16, 22)],
               20: [(13, 5), (18, 19)], 21: [(0, 9), (22, 23)], 22: [(21, 23), (16, 19)], 23: [(2, 14), (21, 22)]}


def genetic_algorithm(board, current_player,depths):
    POPULATION_SIZE = 10
    GENE_SIZE = 10
    GENERATIONS = 10
    MUTATION_RATE = 0.1

    Memory = {}
    
    class GameState:
        def __init__(self, board, current_player):
            self.board = board
            self.current_player = current_player
            self.opponent_player = 'B' if current_player == 'W' else 'W'

        def apply_move(self, move):
            temporary_board = copy.deepcopy(self.board)
            new_state = GameState(temporary_board, self.current_player) 
            from_pos, to_pos = move
            new_state.board[to_pos] = new_state.board[from_pos]
            new_state.board[from_pos] = ' '
            return new_state
  
        def make_kill(self,move):
            temporary_board = copy.deepcopy(self.board)
            new_state = GameState(temporary_board, self.current_player) 
            new_state.board[move]=' '
            return new_state



        def get_legal_moves(self,playerr):
            moves = []
            for i in range(24):
                if self.board[i] == playerr:
                    for neighbor in self.get_empty_neighboring_cells(i):
                        moves.append((i, neighbor))
            return moves

        def get_neighbors(self, pos):
            neighbors = {
                0: [1, 9], 1: [0, 2, 4], 2: [1, 14], 3: [4, 10], 4: [1, 3, 5, 7],
                5: [4, 13], 6: [7, 11], 7: [4, 6, 8], 8: [7, 12], 9: [0, 10, 21],
                10: [3, 9, 11, 18], 11: [6, 10, 15], 12: [8, 13, 17], 13: [5, 12, 14, 20],
                14: [2, 13, 23], 15: [11, 16], 16: [15, 17, 19], 17: [12, 16], 18: [10, 19],
                19: [16, 18, 20, 22], 20: [13, 19], 21: [9, 22], 22: [19, 21, 23], 23: [14, 22]
            }
            return neighbors[pos]
        

        def get_empty_neighboring_cells(self, pos):
            neighbors = {
                0: [1, 9], 1: [0, 2, 4], 2: [1, 14], 3: [4, 10], 4: [1, 3, 5, 7],
                5: [4, 13], 6: [7, 11], 7: [4, 6, 8], 8: [7, 12], 9: [0, 10, 21],
                10: [3, 9, 11, 18], 11: [6, 10, 15], 12: [8, 13, 17], 13: [5, 12, 14, 20],
                14: [2, 13, 23], 15: [11, 16], 16: [15, 17, 19], 17: [12, 16], 18: [10, 19],
                19: [16, 18, 20, 22], 20: [13, 19], 21: [9, 22], 22: [19, 21, 23], 23: [14, 22]
            }
            li = []
            for i in neighbors[pos]:
                if self.board[i] == ' ':
                    li.append(i) 
            return li
        
        def get_all_current_player_positions(self):
            li = []
            for i in range(24):
                if self.board[i] == self.current_player:
                    li.append(i)
            return li
        
        def generate_moves_for_kill(self,player_to_eat):
            li = []
            for i in range(24):
                if self.board[i] == player_to_eat:
                    li.append(i)
            return li

        def evaluate(self, parent_state, phase):
            # print(self.board)
            result = 10 * func.closedMorris(parent_state.board, self.board) + \
                    8 * func.differceInNumberOfMills(self.board) + \
                    4 * func.differenceInClosedPeaces(self.board) + \
                    2 * func.differceInPieces(self.board) + \
                    6 * func.differenceInDoubleMorrises(self.board) + \
                    20 * func.winningConfiguration(self.board)
            return result
        
        def check_mill(self,move,player):
            # print(self.board)
            old_position, current_position = move
            for mill in millions:
                if current_position in mill:
                    pos1, pos2, pos3 = mill
                    if self.board[pos1] == self.board[pos2] == self.board[pos3] == player:
                        return True
            return False

    class Chromosome:
        def __init__(self, moves=None, mf = None):
            if moves is not None:
                self.moves = moves
            else:
                if mf.sum() < 0:
                    mini = mf.min() - 1
                    mf = mf - mini 
                    if mf.sum() == 0:
                        mf = mf + 1
                print(mf)    
                self.moves = random.choices(all_legall_movess, k=GENE_SIZE, weights=mf)
        
        def fitness(self):
            score = 0
            for move in self.moves:
                score+=Memory[move]
            return score

    def count_black_white(state_board):
        black = 0
        white = 0
        for i, cell in enumerate(state_board):
            if cell == 'B':
                black+=1
            elif cell =='W':
                white+=1
        return black,white

    def game_over(new_state,player):
        black,white=count_black_white(new_state.board)
        if black < 3 or white < 3:
            return True
        elif new_state.get_legal_moves(player):
            return False
        else:
            return True
        

    def opponent(player):
        return 'B' if player == 'W' else 'W'
    

    def minimax_alpha_beta(new_state, depth, maximizing_player, alpha, beta, player,phase,parent_state,mill_found):

        if depth == 0 or game_over(new_state,player):
            return new_state.evaluate(parent_state, phase)
            
        if mill_found:
            if maximizing_player:
                max_eval = -math.inf
                for move in new_state.generate_moves_for_kill(opponent(player)):
                    newest_board =  new_state.make_kill(move)
                    mill_found = False
                    eval = minimax_alpha_beta(newest_board, depth - 1, False, alpha, beta, player,phase,new_state,mill_found)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta cutoff
                return max_eval
            else:
                min_eval = math.inf
                for move in new_state.generate_moves_for_kill(player):
                    newest_board =  new_state.make_kill(move) 
                    mill_found = False
                    eval = minimax_alpha_beta(newest_board, depth - 1, False, alpha, beta, player,phase,new_state,mill_found)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha cutoff
                return min_eval
        else:
            if maximizing_player:
                max_eval = -math.inf
                for move in new_state.get_legal_moves(player):
                    newestboard = new_state.apply_move(move)
                    if newestboard.check_mill(move,player):
                        mill_found = True
                        eval = minimax_alpha_beta(newestboard, depth , True, alpha, beta, player,phase,new_state,mill_found)
                    else:
                        mill_found = False
                        eval = minimax_alpha_beta(newestboard, depth - 1, False, alpha, beta, player,phase,new_state,mill_found)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta cutoff
                return max_eval
            
            else:
                min_eval = math.inf
                for move in new_state.get_legal_moves(opponent(player)):
                    newestboard = new_state.apply_move(move)
                    if newestboard.check_mill(move,opponent(player)):
                        mill_found = True
                        eval = minimax_alpha_beta(newestboard, depth , False, alpha, beta, player,phase,new_state,mill_found)
                    else:
                        mill_found = False
                        eval = minimax_alpha_beta(newestboard, depth - 1, True, alpha, beta, player,phase,new_state,mill_found)
                    # print(depth, eval)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha cutoff
                return min_eval
    

    def crossover(parent1, parent2):
        #uniform crossover
        li= []
        li2 = []
        for i in range(GENE_SIZE):
            num = random.random()
            if(num>0.5):
                li.append(parent1.moves[i])
                li2.append(parent2.moves[i])
            else:
                li.append(parent2.moves[i])
                li2.append(parent1.moves[i])

        child1 = Chromosome(moves=li)
        child2 = Chromosome(moves=li2)
        return child1, child2

    def mutate(chromosome):
        i = random.randint(0, GENE_SIZE-1)
        if random.random() < MUTATION_RATE:
            chromosome.moves[i] = random_move()

    def random_move():
        all_avail_pos = GameState(board, current_player).get_all_current_player_positions()
        while True:
            from_pos = random.choice(all_avail_pos)
            empty_neighbours = GameState(board, current_player).get_empty_neighboring_cells(from_pos)
            if empty_neighbours:
                to_pos = random.choice(empty_neighbours)
                break
            else:
                all_avail_pos.remove(from_pos)
        return (from_pos, to_pos)
    
    
    def most_frequent_tuple(tuples_list):
        counter = Counter(tuples_list)
        most_common_tuple, count = counter.most_common(1)[0]
        return most_common_tuple

    def all_legal_moves():
        legal_moves = []
        all_avail_pos = GameState(board, current_player).get_all_current_player_positions()
        for from_pos in all_avail_pos:
            empty_neighbours = GameState(board, current_player).get_empty_neighboring_cells(from_pos)
            for to_pos in empty_neighbours:
                tup = (from_pos, to_pos)
                legal_moves.append(tup)
        return legal_moves
    
    def find_score_of_legal_moves(li):
        for move in li:
            parentt_state = GameState(board, current_player)
            temporary_board = copy.deepcopy(board)
            new_state = GameState(temporary_board, current_player).apply_move(move)
            alpha = -math.inf
            beta = math.inf
            #need change
            if new_state.check_mill(move,current_player):
                eval = minimax_alpha_beta(new_state, depths , True, alpha, beta, current_player,False,parentt_state,True)
                # print("mill with :", move)
            else:
                # print("none with :", move)
                eval = minimax_alpha_beta(new_state, depths - 1, False, alpha, beta, current_player,False,parentt_state,False)
            # print(eval)
            Memory[move] = None
            Memory[move] = eval
        

    all_legall_movess = all_legal_moves()
    find_score_of_legal_moves(all_legall_movess)   
    move_fitnesses = []
    for i in Memory:
        move_fitnesses.append(Memory[i])
    
    move_fitnesses = np.array(move_fitnesses, dtype=np.float32)
    
    population = [Chromosome(mf = move_fitnesses) for _ in range(POPULATION_SIZE)]
    # print(Memory)

    for generation in range(GENERATIONS):

        new_population = []

        c_f_list = []
        for c in population:
            c_f_list.append(c.fitness())

        c_f_list = np.array(c_f_list, dtype=np.float32)

        # print(generation)
        # for c in population:
        #     print(c.moves)
        #     print(c.fitness())

        while len(new_population) < POPULATION_SIZE:
            if c_f_list.sum() < 0:
                mini = c_f_list.min() - 1
                c_f_list = c_f_list - mini
                if c_f_list.sum() == 0:
                    c_f_list = c_f_list + 1
            parent1, parent2 = random.choices(population, k=2, weights=c_f_list)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

    best_strategy = max(population, key=lambda chromosome: chromosome.fitness())

    best_move_that_appear_most = most_frequent_tuple(best_strategy.moves)
    return best_move_that_appear_most
    # return 5

#board = ['W', 'B', 'B', 'W', 'B', 'B', 'B', 'W', ' ', 'W', 'W', 'B', 'W', 'W', 'B', ' ', ' ', ' ', 'B', ' ', 'W', 'B', 'W', ' ']
# board= ['B','B','B','B','W',' ','B','W','W','B','W','W','W',' ','B',' ',' ',' ','W',' ',' ',' ','B',' ']
# # board= ['B','B','B','W','W','B','W','W','B','B','W','W','B',' ',' ','B','W',' ','W',' ',' ',' ',' ',' ']
# # board=['B', 'B', 'B', 'W', 'W', 'B', 'W', 'W', 'B', 'B', 'W', 'W', 'B', ' ', ' ', 'B', ' ', ' ', 'W', 'W', ' ', ' ', ' ', ' ']
#best_move = genetic_algorithm(board, 'B', 3)
#print("Best move:", best_move)