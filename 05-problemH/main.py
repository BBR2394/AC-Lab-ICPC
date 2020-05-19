# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-05-18 11:31:50
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-05-19 12:33:16

import sys

class Board:
	def __init__(self, size):
		self.board = []
		self.selectedDiagonal = False
		self.size = size
		self.nbMoove = 0
		for i in range(0, size):
			self.board.append([])
			for j in range(0, size):
				self.board[i].append("0")
		#print("le board : ", self.board)
		self.printBoard()

	def printBoard(self):
		print("*========================================*")
		#self.board[0][1] = "X"
		for i in range(0, self.size):
			print("ligne ", self.board[i])
		print("*========================================*")

	def addToken(self, line, col):
		if line > self.size or col > self.size:
			#bon il faudra je je jette une excepption c'est mieux
			return False
		self.board[line-1][col-1] = 'X'

	#count number of piece on each diagonal
	#comme cela on selectionne la diagonale la plus remplie 
	def countDiagional(self):
		diagonalOne = 0
		diagonalTwo = 0
		print("in count diagonal")
		for i in range(0, self.size):
			if self.board[i][i] == 'X':
				diagonalOne += 1
				self.board[i][i] = 'x'
			if self.board[i][self.size-1-i] == 'X':
				diagonalTwo += 1
				self.board[i][self.size-1-i] = 'x'
		if diagonalOne > diagonalTwo:
			#donc la on selectionne la diagonal qui va d'en heut a gauche a en bas a droite
			self.selectedDiagonal = True
		#else:
		#pas besoin d'else, on selectionne par defaut la diagonale qui va d'en haut a droite a en bas a gauche
		print("diagonale un et deux : ", diagonalOne, ", ", diagonalTwo)

	def checkLine(self):
		print("in check line")

		#ici on verifie les ligne spour savoir quel jeton est le plus proche

	def checkDiagonale(self):
		print("check line")
		#ici on verifie dans le diagonale quel jeton est le plus proche
		#mais dans les diagonale non "pricipal"

	#cette fonction parcour la diagonale et c'est de la qu'on appelle checkLine et checkDiagonal
	def findeEmptyCase(self):
		if self.selectedDiagonal == False:
			for i in range(0, self.size):
				if self.board[i][self.size-1-i] == "0":
					print(" la il faut rajouter un jeton")
				else:
					print("la pas besoin")
		if self.selectedDiagonal == True:
			print(" on doit faire l'autre diagonale")



def main():
	print("here is where the magik happend!")
	inputData = []
	for line in sys.stdin:
		print("en premier: ", line)
		inputData.append(line)
	bd = Board(5)
	bd.addToken(1, 2)
	bd.addToken(2, 4)
	bd.addToken(3, 4)
	bd.addToken(5, 1)
	bd.addToken(5, 3)
	bd.countDiagional()
	bd.findeEmptyCase()
	bd.printBoard()
	bdBis = Board(3)
	bdBis.addToken(3, 1)
	bdBis.addToken(1, 2)
	bdBis.addToken(2, 2)
	bdBis.countDiagional()
	bdBis.printBoard()

if __name__=="__main__":
	main()