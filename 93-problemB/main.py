# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-03-19 14:10:40
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-04-08 11:17:09

import sys

class LinkPoint:
	def __init__(self, x, y):
		print("\x1b[96mLinkPoint created\033[00m")
		self.x = x
		self.y = y
		self.lstLink = []

	# def addConnectedPoint(self, point):
	# 	print("dans linked poitn : ", self.getCoord(), "  ", point.getCoord())
	# 	for i in self.lstLink:
	# 		print("LA : ", i.getCoord())
	# 	print("ICI ", point.getCoord() == (self.x, self.y))
	# 	if point.getCoord() == (self.x, self.y):
	# 		print("c'est le meme")
	# 		return 0

	# 	for i in self.lstLink:
	# 		if i.getCoord() == point.getCoord():
	# 			print("JE BREAK ADDlinked")
	# 			return 0
	# 	self.lstLink.append(point)
	# 	return 1

	def addConnectedPointBis(self, point):
		print("add connected point bis")
		print("je suis le poitn ", self.getCoord(), " j eme lie a ", point.getCoord())
		self.lstLink.append(point)

	def getCoord(self):
		return (self.x, self.y)

	def getLinked(self):
		return self.lstLink

	def getTinierX(self, x=0):
		return None

	def getTinierY(self, y=0):
		return None

	def getBiggerX(self, x=-1):
		return None

	def getBiggerY(self, y=-1):
		return None



class Segment:
	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0

	def __init__(self, x1, y1, x2, y2):
		print("\x1b[46msegment created\033[00m")
		self.x1 = int(x1)
		self.x2 = int(x2)
		self.y1 = int(y1)
		self.y2 = int(y2)

	def getFirst(self):
		return (self.x1, self.y1)

	def getSecond(self):
		return (self.x2, self.y2)

class Graph:
	allPoint = []
	first = None

	def __init__(self):
		print("\x1b[44mgraph created\033[00m")

	def checkIfExisting(self, newPts):
		for i in self.allPoint:
			if i.getCoord() == newPts.getCoord():
				return i
				break
		self.allPoint.append(newPts)
		return newPts

	def addALink(self, x1, y1, x2, y2):
		#ptsOne = LinkPoint(int(x1), int(y1))
		#ptsTwo = LinkPoint(int(x2), int(y2))

		ptsOne = self.checkIfExisting(LinkPoint(int(x1), int(y1)))
		ptsTwo = self.checkIfExisting(LinkPoint(int(x2), int(y2)))

		if self.first == None:
			self.first = ptsOne
		#self.allPoint.append(ptsOne)
		#self.allPoint.append(ptsTwo)

		ptsOne.addConnectedPointBis(ptsTwo)
		ptsTwo.addConnectedPointBis(ptsOne)


	def printAllPoint(self):
		for i in self.allPoint:
			print("\x1b[36mpoint : ", i.getCoord(), " linked point:", end='')
			tmpLinkedPts = i.getLinked()
			for j in tmpLinkedPts:
				print("\033[00m\x1b[38m", j.getCoord(), end='')
			print(".")
		print("\033[00m")

	def goThroughGraph(self):
		print("go through graph")
		tmpPoint = self.first
		tmpPoint


def main():
	print("\x1b[36mHere is where the magik happened !\033[00m")
	inputData = []
	segmentLst = []
	myGraph = Graph()

	for line in sys.stdin:
		if (line[0] == '0'):
			break
		tempLn = line.split(' ')
		#je ne tient pas compte du premier nombre qui correspond au nombre d'entrée (de coordonnée de point)
		if len(tempLn) > 1:
			#print(tempLn)
			#print(tempLn[0])
			#print(tempLn[1])
			#print(tempLn[2])
			#print(tempLn[3])
			myGraph.addALink(tempLn[0], tempLn[1], tempLn[2], tempLn[3])
			#segmentLst.append(Segment(tempLn[0], tempLn[1], tempLn[2], tempLn[3]))
		inputData.append(line)

	myGraph.printAllPoint()
	#createSegmentList
	print("\x1b[35m", inputData, "\033[00m")

	return 0

if __name__=="__main__":       
    main() 