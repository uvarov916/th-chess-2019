import re

class condition:
	def __init__(self, fen):
		self.board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], 
			['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
			[None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None],
			[None, None, None, None, None, None, None, None],
			['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
			['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
		self.ActiveColor = 'w'
		self.CastlingAvailability = 'KQkq'
		self.EnPassant = '-'
		self.HalfMove = 0
		self.FullMove = 0
		self.init_board(fen)

	def get_fen(self):
		states = ''
		count = 0
		for i in range(len(self.board)):    
			count = 0        
			for j in range(len(self.board[i])):
				if self.board[i][j] == None:
					count += 1
				else:
					if count > 0:
						states += str(count)
						count = 0
					states += self.board[i][j]
			if count > 0:
				states += str(count)
			if i < 7:
				states += '/'	
		#states += ' ' + self.ActiveColor + ' ' + self.CastlingAvailability + ' ' + self.EnPassant + ' ' + int(self.HalfMove) + ' ' + int(self.FullMove)
		return states

	def init_board(self, fen):

		state = fen.split(' ')
		states = state[0].split('/')
		for row in range(8):
			column = list(states[row])
			j = -1
			for grid in column:
				if (grid >='A' and grid <= 'Z') or (grid >='a' and grid <= 'z'):
					self.board[row][j] = grid
					j += 1
				else:
					for i in range(int(grid)):
						self.board[row][j] = None
						j += 1
		self.ActiveColor = state[1]
		self.CastlingAvailability = state[2]
		self.EnPassant = state[3]
		self.HalfMove = state[4]
		self.FullMove = state[5]
		return self.board

	def print_board(self):
		for i in range(len(self.board)):       
			for j in range(len(self.board[i])):
				print(self.board[i][j], end = ' ')
			print()
		print(step1.ActiveColor)
		print(step1.EnPassant)
		print(step1.CastlingAvailability)
		print(step1.HalfMove)
		print(step1.FullMove)

step1 = condition('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b K-kq e3 1 1')
step1.print_board()
