from collections import deque
from socket import socket
from threading import Thread, Lock
from demichess import Game

JOIN_EITHER = 81
JOIN_WHITE  = 82
JOIN_BLACK  = 83

class Pool:	#matches up bots and starts games
	white_pool = deque()	#deque means double-ended queue, a FIFO (first in, first out) structure
	black_pool = deque()
	either = None	#there can never be multiple eithers, since they would just be matched up
	mutex = Lock()

	@classmethod
	def enter_pool(cls, conn, color):
		cls.mutex.acquire()		#this prevents several enter_pool s from running at once
		game = None
		if color == "white":
			if len(cls.black_pool) > 0:
				game = Game(conn, cls.black_pool.popLeft())
			elif cls.either != None:
				game = Game(conn, cls.either)
				cls.either = None
			else:
				cls.white_pool.append(conn)
		elif color == "black":
			if len(cls.white_pool) > 0:
				game = Game(cls.white_pool.popLeft(), conn)
			elif cls.either != None:
				game = Game(cls.either, conn)
				cls.either = None
			else:
				cls.black_pool.append(conn)
		else:	#either, so check both pools and either
			if len(cls.white_pool) > 0:
				game = Game(cls.white_pool.popLeft(), conn)
			elif len(cls.black_pool) > 0:
				game = Game(conn, cls.black_pool.popLeft())
			elif cls.either != None:
				game = Game(cls.either, conn)
				cls.either = None
			else:
				cls.either = conn
		if game != None:
			Thread(target=game.run).start()
		cls.mutex.release()

def run_either():
	s = socket()
	s.bind(("", JOIN_EITHER))	#tell it to listen on port JOIN_EITHER
	s.listen()
	print("either port opened")
	while True:
		conn = s.accept()[0]	#accept returns tuple of (conn, ip address), we just want the connection
		Pool.enter_pool(conn, "either")

def run_white():
	s = socket()
	s.bind(("", JOIN_WHITE))	#tell it to listen on port JOIN_EITHER
	s.listen()
	print("white port opened")
	while True:
		conn = s.accept()[0]	#accept returns tuple of (conn, ip address), we just want the connection
		Pool.enter_pool(conn, "white")

def run_black():
	s = socket()
	s.bind(("", JOIN_BLACK))	#tell it to listen on port JOIN_EITHER
	s.listen()
	print("black port opened")
	while True:
		conn = s.accept()[0]	#accept returns tuple of (conn, ip address), we just want the connection
		Pool.enter_pool(conn, "black")

Thread(target=run_either).start()
Thread(target=run_white).start()
Thread(target=run_black).start()