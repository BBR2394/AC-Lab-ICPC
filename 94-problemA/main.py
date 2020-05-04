# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-03-02 15:16:18
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-04-21 11:45:00

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
			print(" livre : ", i.getTitle(), " de ", i.getAuthor())

	def printSorted(self):
		print("la liste au debut : ", self.printAllBook())
		self.listBook.sort()
		print("la liste apres le trie : ", self.printAllBook())

	def manage(self, order, booktocheck):
		print("dans manage jai le livre : ", booktocheck, " a : ", order)
		for i in self.listBook:
			if i.getTitle == booktocheck:
				print("OK")
			else:
				print("KO")


	def addBook(self, title):
		splited = title.split("by")
		print("i am going to add ", splited)
		self.listBook.append(Book(splited[0], splited[1]))


def main():
	allInput = []
	bookOnly = []
	library = Library()
	bookTitle = []

	print("here is where the magik happended")
	for line in sys.stdin:
		print("en premier: ", line)
		allInput.append(line)

	first = True
	second = False

	while len(allInput) > 0:
		if first == True and allInput[0] != "END\n":
			bookOnly.append(allInput[0])
			library.addBook(allInput[0])
			bookTitle.append((allInput[0].split("by")[0]).split('"')[1])
		elif allInput[0] == "END\n":
			first = False
			second = True
		elif second == True and allInput[0] != "END\n":
			print("deuxieme partie ", allInput)
			if allInput[0].find("BORROW"):
				print("dans BORROW ", allInput[0])
				abooktomanage = allInput[0].split('"')[1] 
				print("\x1B[33mle booktocheck =: ", abooktomanage, "\x1B[0m")
				library.manage(Order.BORROW, abooktomanage)
			elif allInput[0].find("RETURN"):
				print("dans RETURN")
				abooktomanage = allInput[0].split('"')[1] 
				print("\x1B[34mle booktocheck =: ", abooktomanage, "\x1B[0m")
				library.manage(Order.RETURN, abooktomanage)
			elif allInput[0].find("SHELVE"):
				print("\x1B[35mSHEEVE")
				library.manage(Order.SHELVE, abooktomanage)
			elif allInput[0].find("END"):
				second = False
		allInput.pop(0)


	print("ici j'ai que les livre d'abord")
	print(bookOnly)
	print(bookTitle)
	print(bookTitle.sort())
	print("A La fin :")
	library.printSorted()


	
if __name__=="__main__":
    main() 