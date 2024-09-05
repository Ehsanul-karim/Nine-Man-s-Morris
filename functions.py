POSDICT = {0: (0, 0), 1: (0, 3), 2: (0, 6), 3: (1, 1), 4: (1, 3), 5: (1, 5), 6: (2, 2), 7: (2, 3), 8: (2, 4),
		   9: (3, 0), 10: (3, 1), 11: (3, 2), 12: (3, 4), 13: (3, 5), 14: (3, 6), 15: (4, 2), 16: (4, 3), 17: (4, 4),
		   18: (5, 1), 19: (5, 3), 20: (5, 5), 21: (6, 0), 22: (6, 3), 23: (6, 6)}

ADJDICT = {0: (1, 9), 1: (0, 2, 4), 2: (1, 14), 3: (4, 10), 4: (1, 3, 5, 7), 5: (4, 13), 6: (7, 11),
		   7: (4, 6, 8), 8: (7, 12), 9: (0, 21, 10), 10: (3, 8, 11, 18), 11: (6, 10, 15), 12: (8, 13, 17),
		   13: (5, 12, 14, 20), 14: (2, 13, 23), 15: (11, 16), 16: (15, 17, 19), 17: (12, 16),
		   18: (10, 19), 19: (16, 18, 20, 22), 20: (13, 19), 21: (9, 22), 22: (19, 21, 23), 23: (14, 22)}

MILLS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
		 (0, 9, 21), (3, 10, 18), (6, 11, 15), (1, 4, 7), (16, 19, 22), (8, 12, 17), (5, 13, 20), (2, 14, 23))

TREECONFIG = \
	((9, 0, 1, 2, 21), (9, 21, 22, 0, 23), (1, 2, 14, 0, 23), (22, 23, 14, 21, 2), (10, 3, 4, 5, 18), (4, 5, 13, 3, 20),
	 (10, 18, 19, 3, 20), (19, 20, 13, 18, 5), (11, 6, 7, 15, 8), (7, 8, 12, 6, 17), (11, 15, 16, 6, 17),
	 (16, 17, 12, 15, 8), (0, 1, 4, 7, 2), (2, 1, 4, 0, 7), (21, 22, 19, 16, 23), (23, 22, 19, 16, 21),
	 (0, 9, 10, 11, 21),
	 (21, 9, 10, 11, 0), (2, 13, 14, 12, 23), (13, 14, 23, 12, 2), (3, 4, 7, 5, 1), (3, 4, 1, 7, 5), (4, 5, 7, 3, 1),
	 (5, 4, 1, 7, 3), (22, 19, 18, 20, 16), (18, 19, 16, 22, 20), (20, 19, 22, 16, 18), (20, 19, 16, 18, 22),
	 (3, 10, 11, 9, 18), (3, 9, 10, 11, 18), (18, 10, 11, 9, 3), (18, 10, 9, 11, 3), (5, 12, 13, 14, 20),
	 (5, 13, 14, 12, 20),
	 (20, 13, 14, 12, 5), (20, 13, 12, 5, 14), (6, 7, 4, 1, 8), (8, 7, 4, 1, 6), (6, 11, 10, 9, 15), (15, 11, 10, 6, 9),
	 (15, 16, 19, 17, 22), (16, 17, 19, 15, 22), (17, 12, 13, 8, 14), (8, 12, 13, 14, 17))

MILLS2 = (
	(23, 22, 21, 9, 0), (21, 22, 23, 14, 2), (21, 9, 0, 1, 2), (0, 1, 2, 14, 23), (20, 19, 18, 10, 3),
	(18, 19, 20, 13, 5),
	(18, 10, 3, 4, 5), (20, 13, 5, 4, 3), (17, 16, 15, 11, 6), (15, 16, 17, 12, 8), (15, 11, 6, 7, 8),
	(6, 7, 8, 12, 17),
	(0, 1, 2, 4, 7), (21, 22, 23, 19, 16), (0, 9, 21, 10, 11), (2, 14, 23, 12, 13), (1, 4, 7, 3, 5), (3, 10, 18, 9, 11),
	(5, 13, 20, 12, 14), (16, 19, 22, 18, 20), (6, 7, 8, 4, 1), (6, 11, 15, 9, 10), (15, 16, 17, 19, 22),
	(8, 12, 17, 13, 14))

PEACEINMILL = {0: [(1, 2), (9, 21)], 1: [(0, 2), (4, 7)], 2: [(0, 1), (14, 23)], 3: [(4, 5), (10, 18)],
			   4: [(3, 5), (1, 7)],
			   5: [(13, 20), (3, 4)], 6: [(7, 8), (11, 15)], 7: [(1, 4), (6, 8)], 8: [(6, 7), (12, 17)],
			   9: [(0, 21), (10, 11)],
			   10: [(9, 11), (3, 18)], 11: [(15, 6), (9, 10)], 12: [(8, 17), (13, 14)], 13: [(12, 14), (5, 20)],
			   14: [(2, 23), (12, 13)],
			   15: [(16, 17), (11, 6)], 16: [(15, 17), (19, 22)], 17: [(12, 8), (15, 16)], 18: [(3, 10), (19, 20)],
			   19: [(18, 20), (16, 22)],
			   20: [(13, 5), (18, 19)], 21: [(0, 9), (22, 23)], 22: [(21, 23), (16, 19)], 23: [(2, 14), (21, 22)]}

EMPTYCELL = ' '

def getNumberOf2PeacesConfig(board, player):
	number = 0
	for trio in MILLS:
		if board[trio[0]] == board[trio[1]] == player and board[trio[2]] == EMPTYCELL:
			number += 1
		if board[trio[1]] == board[trio[2]] == player and board[trio[0]] == EMPTYCELL:
			number += 1
	return number


def getNumberOf3PeaceConfig(board, player):
	number = 0
	for var in TREECONFIG:
		if board[var[0]] == board[var[1]] == board[var[2]] == player and board[
			var[3]] == EMPTYCELL and board[var[4]] == EMPTYCELL:
			number += 1
	return number


def getNumberOfPlayerDoubleMills(board, player):
	number = 0
	for var in MILLS2:
		if board[var[0]] == board[var[1]] == board[var[2]] == board[var[3]] == board[
			var[4]] == player:
			number += 1
	return number


def getNumberOfPlayerMills(board, player):
	numberOfMills = 0
	for trio in MILLS:
		if board[trio[0]] == board[trio[1]] == board[trio[2]] == player:
			numberOfMills += 1
	return numberOfMills


def getNumberOfPlayerPieces(board, player):
	number = 0
	for position in board:
		if position == player:
			number += 1
	return number


def getNumberOfPlayerClosedPeaces(board, player):
	number = 0
	for key, value in ADJDICT.items():
		temp = 0
		if board[key] == player:
			for adj in value:
				if board[adj] == EMPTYCELL:
					temp = 1
					break
			if temp == 0: 
				number += 1
	return number


def allPlayerPiecesClosed(board, player):
	for key, value in ADJDICT.items():
		if board[key] == player:
			for adj in value:
				if board[adj] == EMPTYCELL:
					return False
	return True


def differenceIn3PeacesConfig(board):
	black = getNumberOf3PeaceConfig(board, 'B')
	white = getNumberOf3PeaceConfig(board, 'W')
	return black - white


def differenceInDoubleMorrises(board):
	black = getNumberOfPlayerDoubleMills(board, 'B')
	white = getNumberOfPlayerDoubleMills(board, 'W')
	return black - white


def differenceIn2PeacesConfig(board):
	black = getNumberOf2PeacesConfig(board, 'B')
	white = getNumberOf2PeacesConfig(board, 'W')
	return black - white


def differenceInClosedPeaces(board):
	black = getNumberOfPlayerClosedPeaces(board, 'B')
	white = getNumberOfPlayerClosedPeaces(board, 'W')
	return black - white


def differceInNumberOfMills(board):
	black = getNumberOfPlayerMills(board, 'B')
	white = getNumberOfPlayerMills(board, 'W')
	return black - white


def differceInPieces(board):
	black = getNumberOfPlayerPieces(board, 'B')
	white = getNumberOfPlayerPieces(board, 'W')
	return black - white


def winningConfiguration(board):
	if allPlayerPiecesClosed(board, 'W') or getNumberOfPlayerPieces(board, 'W') < 3:
		return 1
	if allPlayerPiecesClosed(board, 'B') or getNumberOfPlayerPieces(board, 'B') < 3:
		return -1
	return 0


def getListOfAllPlayerMills(board, player):
	list = []
	for trio in MILLS:
		if board[trio[0]] == board[trio[1]] == board[trio[2]] == player:
			list.append(trio)
	return list

def millHasBeenMadeInLastTurn(parent_board,board, player):
	parent_mills = getListOfAllPlayerMills(parent_board, player)
	current_mills = getListOfAllPlayerMills(board, player)
	for mill in current_mills:
		if mill not in parent_mills:
			return True
	return False

def closedMorris(parent_board,board):
	if millHasBeenMadeInLastTurn(parent_board,board, 'W'):
		return -1
	
	if millHasBeenMadeInLastTurn(parent_board,board, 'B'):
		return 1
	else:
		return 0


def pieceInMill(board, index_peace):
	for par in PEACEINMILL[index_peace]:
		if board[par[0]] == board[par[1]] == board[index_peace]:
			return True
	return False


def getAllPositionsOfPlayer(board, player):
	positions = []
	for i in range(24):
		if board[i] == player:
			positions.append(i)
	return positions


def getAllEmptyPositionsOnBoard(board):
	pos = []
	for i in range(24):
		if board[i] == EMPTYCELL:
			pos.append(i)
	return pos


