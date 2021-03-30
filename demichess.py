class Game:
	INIT_BOARD = list("kbnrpppp----------------PPPPKBNR")
	
	def __init__(self, white_conn, black_conn, board=None, whiteTurn = True):
		if board == None:
			self.board = Game.INIT_BOARD[:]
		self.white = white_conn
		self.black = black_conn
		self.whiteTurn = whiteTurn
	
	def run(self):
		pass
	
	def is_legal_move(self, start, end):
		if start == end:
			return False
		if self.board[start] == "-":
			return False
		if self.board[start] < 91 ^ self.whiteTurn:		#trying to move opponent's piece
			return False
		if self.board[end] > 91 ^ self.whiteTurn:		#trying to take own piece
			return False
		
		#Piece-specific code:
		if self.board[start] == 'p':
			sx = start % 4
			sy = start // 4
			ex = end % 4
			ey = end // 4
			if (ey - sy) < 1: #trying to move up 
				return False
			if sy == 1: #Pawn in original position
				if ey - sy > 2: #moving more than two lines down
					return False
			else:
				if (ey - sy) != 1: #trying to move more than one down from non-starting position
					return False
			if (ex-sx) == 0: #move striaght down
				if self.board[end] != '-':
					return False
			elif (ex-sx) == 1 or (ex-sx) == -1: #taking diagonally
			    if self.board[end] == '-':
			        return False
			else: #moving too far to a side (not just one diagonal)
			    return False
			return True 
                
			return True
		elif self.board[start] == 'P':
			sx = start % 4
			sy = start // 4
			ex = end % 4
			ey = end // 4
			if (ey - sy) > -1: #trying to move down  
			    return False
			if sy == 6: #Pawn in original position
			    if ey - sy < -2: #moving more than two lines up
			        return False
			else:
			    if (ey - sy) != 1: #trying to move more than one up from non-starting position
			        return False
			if (ex-sx) == 0: #move striaght up
			    if self.board[end] != '-':
			        return False
			elif (ex-sx) == 1 or (ex-sx) == -1: #taking diagonally
			    if self.board[end] == '-':
			        return False
			else: #moving too far to a side (not just one diagonal)
			    return False
			return True 
		elif self.board[start] == 'B' or self.board[start] == 'b':
			return True
		elif self.board[start] == 'N' or self.board[start] == 'n':
			return True
		elif self.board[start] == 'R' or self.board[start] == 'r':
			return True
		elif self.board[start] == 'Q' or self.board[start] == 'q':
			return True
		elif self.board[start] == 'K' or self.board[start] == 'k':
			return True

	def make_move(self, start, end, promotion_choice):	#actually perform the move.  Assume it is legal.  Promotion choice will be a legal piece and the right color
		#code here
		whiteTurn = not whiteTurn
