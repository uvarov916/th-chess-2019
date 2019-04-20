import re
import json
class Board:
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
		states += ' ' + self.ActiveColor + ' ' + self.CastlingAvailability + ' ' + self.EnPassant + ' ' + str(self.HalfMove) + ' ' + str(self.FullMove)
		return states

	def init_board(self, fen):

		state = fen.split(' ')
		states = state[0].split('/')
		for row in range(8):
			column = list(states[row])
			j = 0
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


	#def translate(coordinate)
	def apply_changes(self, changes):
		if self.ActiveColor == 'b' :
			self.FullMove = str(int(self.FullMove) + 1)
		if len(changes) == 2 :
			# Ход на пустую клетку
			if self.board[changes[0][0]][changes[0][1]] == None or self.board[changes[1][0]][changes[1][1]] == None :
				temp = self.board[changes[0][0]][changes[0][1]]
				self.board[changes[0][0]][changes[0][1]] = self.board[changes[1][0]][changes[1][1]]
				self.board[changes[1][0]][changes[1][1]] = temp
				self.HalfMove = str(int(self.HalfMove) + 1)
				if self.board[changes[0][0]][changes[0][1]] == 'P' or self.board[changes[0][0]][changes[0][1]] == 'p' or self.board[changes[1][0]][changes[1][1]] == 'P' or self.board[changes[1][0]][changes[1][1]] == 'p' :
					self.HalfMove = '0'
					#peshka na prohode
					if abs(changes[0][0] - changes[1][0]) == 2 : 
						polosa = 8 - (changes[0][0] + changes[1][0])//2
						print('eto polosa ' , polosa)
						self.EnPassant = str(chr(ord('a') + changes[0][1]))+ str(polosa)


			# Съедаем
			else :
				isFirstBlack = self.board[changes[0][0]][changes[0][1]].islower()
				self.HalfMove = '0'

				# съели первого
				if isFirstBlack and self.ActiveColor == 'w' or not isFirstBlack and self.ActiveColor == 'b' :
					self.board[changes[0][0]][changes[0][1]] = self.board[changes[1][0]][changes[1][1]]
					self.board[changes[1][0]][changes[1][1]] = None
				# съели второго
				else:
					self.board[changes[1][0]][changes[1][1]] = self.board[changes[0][0]][changes[0][1]]
					self.board[changes[0][0]][changes[0][1]] = None

		if len(changes) == 4:	
			
			self.HalfMove = '0'
			if self.ActiveColor == 'w' and self.CastlingAvailability == 'KQkq' : self.CastlingAvailability = 'kq'	
			if self.ActiveColor == 'w' and self.CastlingAvailability == 'KQ' : self.CastlingAvailability = '-'

			if self.ActiveColor == 'b' and self.CastlingAvailability == 'KQkq' : self.CastlingAvailability = 'KQ'
			if self.ActiveColor == 'b' and self.CastlingAvailability == 'kq' : self.CastlingAvailability = '-'

			tmp = self.board[changes[0][0]][changes[0][1]]
			self.board[changes[0][0]][changes[0][1]] = self.board[changes[2][0]][changes[2][1]]
			self.board[changes[2][0]][changes[2][1]] = tmp
			tmp = self.board[changes[1][0]][changes[1][1]]
			self.board[changes[1][0]][changes[1][1]] = self.board[changes[3][0]][changes[3][1]]
			self.board[changes[3][0]][changes[3][1]] = tmp

		if self.ActiveColor == 'w' :
			self.ActiveColor = 'b'
		else :
			self.ActiveColor = 'w'
			
				 
def swap (a, b) :
	tmp = a
	a = b
	b = tmp

# step1 = condition('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b K-kq e3 1 1')
# step1.print_board()
