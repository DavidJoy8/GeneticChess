class Game:
	INIT_BOARD = list("kbnrpppp----------------PPPPKBNR")
	
	def __init__(self, white_conn, black_conn, board=None, whiteTurn = True):
		if board == None:
			self.board = Game.INIT_BOARD[:]
		self.white = white_conn
		self.black = black_conn
		self.whiteTurn = whiteTurn
	
	def run(self):
	    # game loop
	    # try assuming both sockets are connected
            try:
                while True:
                    # current player send a move
                    if self.whiteTurn:
                        curr_start, curr_end, curr_promo = self.white.recv().split()
                    else:
                        curr_start, curr_end, curr_promo = self.black.recv().split() 
                    # check if is_legal_move()
                    if self.is_legal_move(curr_start, curr_end):
                        # make the move make_move()
                        is_game_done = self.make_move(curr_start, curr_end, curr_promo)
                        if is_game_done:
                            # ending the game stuff here
                            break
		    # transfer control to the other player
		    self.whiteTurn = not self.whiteTurn
		return
	    except:
	        # one or both socket end their connection
	        # do stuff
	        return
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
		whiteTurn = not whiteTurn
