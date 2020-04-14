# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-03-02 15:16:18
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-04-14 12:01:27

#i am not decided yet. do it in C++ or Python ^^

import sys

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

	def __lt__(self, other):
		print("dans la method a surcharger")

	def __le__(self, other):
		print("dans la method a surcharger")

	def __eq__(self, other):
		print("dans la method a surcharger")

	def __ne__(self, other):
		print("dans la method a surcharger")

	def __gt__(self, other):
		print("dans la method a surcharger")

	def __ge__(self, other):
		print("dans la method a surcharger")


class Library:
	def __init__(self):
		print(" a library is created")
		self.listBook = []

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
		print(line)
		allInput.append(line)

	for i in allInput:
		if i != "END\n":
			bookOnly.append(i)
			library.addBook(i)
			bookTitle.append((i.split("by")[0]).split('"')[1])
		else:
			break
	print("ici j'ai que les livre d'abord")
	print(bookOnly)
	print(bookTitle)
	print(bookTitle.sort())


	
if __name__=="__main__":       
    main() 