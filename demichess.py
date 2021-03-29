class Game:
	INIT_BOARD = list("kbnrpppp----------------PPPPKBNR")
	
	def __init__(self, white_conn, black_conn, board=None):
		if board == None:
			self.board = Game.INIT_BOARD[:]
	
	def run(self):
		pass
	
	def is_legal_move(self, start, end):
		if self.board[start] == "-":
			return False
		elif self.board[start] == 'p':
			return False
		elif self.board[start] == 'P':
			return False
		elif self.board[start] == 'B' or self.board[start] == 'b':
			return False
		elif self.board[start] == 'N' or self.board[start] == 'n':
			return False
		elif self.board[start] == 'R' or self.board[start] == 'r':
			return False
		elif self.board[start] == 'Q' or self.board[start] == 'q':
			return False
		elif self.board[start] == 'K' or self.board[start] == 'k':
			return False