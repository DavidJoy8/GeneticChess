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
		if self.board[start] == "-":
			return False
		if self.board[start] < 91 ^ self.whiteTurn:		#trying to move opponent's piece
			return False
		
		#Piece-specific code:
		if self.board[start] == 'p':
			return True
		elif self.board[start] == 'P':
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
		whiteTurn = !whiteTurn