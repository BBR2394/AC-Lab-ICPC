# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-03-02 15:16:18
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-05-18 10:49:13

#i am not decided yet. do it in C++ or Python ^^

import sys
from enum import Enum

class Order(Enum):
	BORROW = 1
	RETURN = 2
	SHELVE = 3

class Book:
	def __init__(self, name, authors):
		self.title = name
		self.authors = authors
		self.isBorrowed = False

	def getAuthor(self):
		return self.authors

	def getTitle(self):
		return self.title

	def borrowed(self):
		self.isBorrowed = True

	def back(self):
		self.isBorrowed = False

	def getIsBorrowed(self):
		return self.isBorrowed

	def setStatus(self, order):
		print("dans set status : ", self.getIsBorrowed(), " ", order )
		if order == Order.BORROW:
			self.borrowed()
		if order == Order.RETURN:
			self.back()
		print("dans set status : ", self.getIsBorrowed(), " ", order )

		#self < other
	def __lt__(self, other):
		print("dans la method a surcharger")
		if self.getAuthor() < other.getAuthor():
			return True
		else:
			return False
		#self <= other
	def __le__(self, other):
		print("dans la method a surcharger")
		if self.getAuthor() < other.getAuthor():
			return True
		elif self.getAuthor() == other.getAuthor():
			if self.getTitle() <= other.getTitle():
				return True
			else:
				return False
		else:
			return False
		#self == other
	def __eq__(self, other):
		print("dans la method a surcharger")
		#self != other
	def __ne__(self, other):
		print("dans la method a surcharger")
		# self > other
	def __gt__(self, other):
		print("dans la method a surcharger")
		if self.getAuthor() > other.getAuthor():
			return True
		else:
			return False
		# self >= other
	def __ge__(self, other):
		print("dans la method a surcharger")
		if self.getAuthor() >= other.getAuthor():
			return True
		elif self.getAuthor() == other.getAuthor():
			if self.getTitle() >= other.getTitle():
				return True
			else:
				return False
		else:
			return False


class Library:
	def __init__(self):
		print(" a library is created")
		self.listBook = []

	def printAllBook(self):
		for i in self.listBook:
			print(" livre : ", i.getTitle(), " de ", i.getAuthor(), " is borrowed : ", i.getIsBorrowed())

	def printSorted(self):
		print("la liste au debut : ", self.printAllBook())
		self.listBook.sort()
		print("la liste apres le trie : ", self.printAllBook())

	def removeBorrowedBook(self):
		temp = []
		for i in self.listBook:
			print("get Is borrowed : ", i.getIsBorrowed())
			if i.getIsBorrowed() == False:
				temp.append(i)
			else:
				print("I REMOVED A BOOK", i.getTitle())
		print(("temp a la fin :"))
		self.listBook.clear()
		self.listBook = temp
		for j in temp:
			print(j.getTitle())

	def sortTheListBook(self):
		self.removeBorrowedBook()
		self.listBook.sort()

	def manage(self, order, booktocheck):
		print("dans manage jai le livre : ", booktocheck, " a : ", order)
		for i in self.listBook:
			x = booktocheck.find(i.getTitle())
			if i.getTitle() == booktocheck:
				print("OK")
				i.setStatus(order)
				return 
			else:
				print("KO : ", i.getTitle(), " ", booktocheck, " ", i.getIsBorrowed(), " ", x)

	def addBook(self, title):
		splited = title.split("by")
		print("i am going to add ", splited)
		bookname = splited[0].split('"')
		print(" book name ", bookname)
		self.listBook.append(Book(bookname[1], splited[1]))

	def printResult(self):
		i = len(self.listBook)
		c = 0
		print("taille de la liste : ", len(self.listBook))
		if i > 1:
			while c+1 < i:
				print("Put ", self.listBook[c+1].getTitle(), " after ", self.listBook[c].getTitle())
				c += 1
		print("END")

def main():
	allInput = []
	# bookOnly = []
	library = Library()
	# bookTitle = []

	print("here is where the magik happended")
	for line in sys.stdin:
		print("en premier: ", line)
		allInput.append(line)

	first = True
	second = False

	while len(allInput) > 0:
		if first == True and allInput[0] != "END\n":
			#la on recupere la liste des livre
			# bookOnly.append(allInput[0])
			library.addBook(allInput[0])
			# bookTitle.append((allInput[0].split("by")[0]).split('"')[1])
		elif allInput[0] == "END\n":
			#je passe des entrée des livres aux entrées des emprunts
			first = False
			library.printAllBook()
			second = True
		elif second == True and allInput[0] != "END\n":
			print("deuxieme partie ", allInput)
			if allInput[0].find("BORROW") == 0:
				print("dans BORROW !", allInput[0])
				abooktomanage = allInput[0].split('"')[1] 
				print("\x1B[33mle booktocheck =: ", abooktomanage, "\x1B[0m")
				library.manage(Order.BORROW, abooktomanage)
			elif allInput[0].find("RETURN") == 0:
				print("dans RETURN")
				abooktomanage = allInput[0].split('"')[1] 
				print("\x1B[34mle booktocheck =: ", abooktomanage, "\x1B[0m")
				library.manage(Order.RETURN, abooktomanage)
			elif allInput[0].find("SHELVE") == 0:
				print("\x1B[35mSHEEVE")
				library.manage(Order.SHELVE, abooktomanage)
			elif allInput[0].find("END") == 0:
				second = False
		allInput.pop(0)


	# print("ici j'ai que les livre d'abord")
	# print(bookOnly)
	# print(bookTitle)
	# bookTitle.sort()
	# print(bookTitle)
	library.printAllBook()
	print("A La fin :")
	library.sortTheListBook()
	print("\x1B[0m", end="")
	library.printResult()


	
if __name__=="__main__":
    main() 