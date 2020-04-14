# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-03-19 14:10:40
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-04-08 18:38:15

import sys
from enum import Enum

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
		print("je suis le poitn ", self.getCoord(), " je me lie a ", point.getCoord())
		self.lstLink.append(point)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getCoord(self):
		return (self.x, self.y)

	def getLinked(self):
		return self.lstLink

	def printLinkedPoint(self):
		print("les point lié au point : ", self.getCoord())
		for i in self.lstLink:
			print("point : ", i.getCoord())

	#c'est mal fait cette fonction car je retourne la valeur du x plus petite
	#alors qu'il faut que je retourne une ref sur le point qui a ce plus petit x parmis les points lié
	# def getTinierX(self, x=0):
	# 	tiny = self.x
	# 	for i in self.lstLink:
	# 		if i.getX() < tiny:
	# 			tiny = i.getX()
	# 	return tiny
	
	#not work
	# def getTinierXExceptPreviousPoint(self, prevPoint):
	# 	tiny = None
	# 	tinyX = self.x
	# 	for i in self.lstLink:
	# 		if i.getX() < tinyX:
	# 			print("le i : ", i.getCoord())
	# 			if i != prevPoint:
	# 				print("tuiny assigné")
	# 				tiny = i
	# 			else :
	# 				print("c'est le point precedent")
	# 	print("et donc celui avec le plus petit x : ", tiny.getCoord(), "de valeur : ", tinyX)
	# 	return tiny

	#...
	def getTinierYExceptPreviousPoint(self, prevPts=None):
		tiny = None
		tinierYTemp = None
		for i in self.lstLink:
			if tinierYTemp == None:
				tinierYTemp = self.getY() +1
			if i.getY() < tinierYTemp:
				print("le Y est plus petit")
				if i != prevPts:
					print(" -> ce n'est pas le pts precedent")
					tiny = i
					tinierYTemp = i.getY()
				else:
					print("c'est le precedent et donc pas le plus petit")
					tinierYTemp = None
		return tiny
			
	def getTinierXExceptPreviousPoint(self, prevPts=None):
		tiny = None
		tinierXTemp = None
		print("c'est le point : ", self.getCoord())
		for i in self.lstLink:
			print("c'est le point i ", i.getCoord(), "et la var tempo ", tinierXTemp)
			if tinierXTemp == None:
				tinierXTemp = i.getX() + 1
				print("->je suis passé dnas le if", i.getCoord(), "  ", tinierXTemp)
			if i.getX() < tinierXTemp:
				print("le X est plus petit")
				if i != prevPts:
					print(" -> ce n'est pas le pts precedent")
					tiny = i
					tinierXTemp = i.getX()
				else:
					print("c'est le precedent et donc pas le plus petit")
					tinierXTemp = None
		print("je sort")
		return tiny

	def getBiggerXExceptPreviousPoint(self, prevPts=None):
		bigger = None
		biggerXTemp = None
		print("\x1b[44mdans get bigger x excpet prev\x1b[0m")
		for i in self.lstLink:
			if biggerXTemp == None:
				biggerXTemp = i.getX() - 1
			if i.getX() > biggerXTemp:
				print("le X est plus grand")
				if i != prevPts:
					print(" -> ce n'est pas le pts precedent : ", i.getCoord())
					bigger = i
					biggerXTemp = i.getX()
				else:
					print(" -> c'est le precedent et donc pas le plus grand")
					biggerXTemp = None
		return bigger
	
	#a tester
	def getBiggerYExceptPreviousPoint(self, prevPts=None):
		Bigger = None
		biggerYTemp = None
		print("\x1b[44mdans get bigger x excpet prev\x1b[0m")
		for i in self.lstLink:
			if biggerYTemp == None:
				biggerYTemp = i.getY() - 1
			if i.getY() > biggerYTemp:
				print("le Y est plus grand")
				if i != prevPts:
					print(" -> ce n'est pas le pts precedent : ", i.getCoord())
					Bigger = i
					biggerYTemp = i.getY()
				else:
					print(" -> c'est le precedent et donc pas le plus grand")
					biggerXTemp = None
		return Bigger


	# def getTinierY(self, y=0):
	# 	tiny = self.y
	# 	for i in self.lstLink:
	# 		if i.getY() < tiny:
	# 			tiny = i.getY()
	# 	return tiny

	# def getBiggerX(self, x=-1):
	# 	big = self.x
	# 	for i in self.lstLink:
	# 		if i.getX() > big:
	# 			big = i.getX()
	# 	return big

	# def getBiggerY(self, y=-1):
	# 	big = self.y
	# 	for i in self.lstLink:
	# 		if i.getY() > big:
	# 			big = i.getY()
	# 	return big

	def getEastPoint(self):
		print("les point lies : ", self.printLinkedPoint())
		res = self.getBiggerXExceptPreviousPoint(None)
		print("le point le plus a l'est du point : ", self.getCoord(), " est le point : ", res.getCoord())
		return res

	def getFirstLinked(self):
		print("dans le get first link : ", self.lstLink[0].getCoord())
		print("la liste lst link : ", self.lstLink)
		return self.lstLink[0]


# class Segment:
# 	x1 = 0
# 	x2 = 0
# 	y1 = 0
# 	y2 = 0

# 	def __init__(self, x1, y1, x2, y2):
# 		print("\x1b[46msegment created\033[00m")
# 		self.x1 = int(x1)
# 		self.x2 = int(x2)
# 		self.y1 = int(y1)
# 		self.y2 = int(y2)

# 	def getFirst(self):
# 		return (self.x1, self.y1)

# 	def getSecond(self):
# 		return (self.x2, self.y2)

class Cardinal(Enum):
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3

class Graph:

	def __init__(self):
		print("\x1b[44mgraph created\033[00m")
		self.allPoint = []
		self.origin = None
		self.first = None
		self.second = None
		self.dicoResult = {}
		self.currentDir = Cardinal.EAST

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
		print("\x1b[46m$>dans la méthode print all point\033[00m")
		for i in self.allPoint:
			print("\x1b[36mpoint : ", i.getCoord(), " linked point:", end='')
			tmpLinkedPts = i.getLinked()
			for j in tmpLinkedPts:
				print("\033[00m\x1b[38m", j.getCoord(), end='')
			print(".")
		print("\033[00m")

	def addNumPoint(self, nbPts):
		print("ici le nombre de points qu'il y a :", nbPts)

	def goOnRight(self, currentPts, prevPts):
		print("here i will move to the right")
		#bon il y a une meilleur methode
		nextPts = None
		print("la current dir", self.currentDir)
		if self.currentDir == Cardinal.EAST:
			print("go east")
			nextPts = currentPts.getTinierXExceptPreviousPoint(prevPts)
		if self.currentDir == Cardinal.SOUTH:
			print("go south")
			nextPts = currentPts.getBiggerYExceptPreviousPoint(prevPts)
		if self.currentDir == Cardinal.WEST:
			print("go west")
			nextPts = currentPts.getBiggerXExceptPreviousPoint(prevPts)
		if self.currentDir == Cardinal.NORTH:
			print("go north")
			nextPts = currentPts.getTinierYExceptPreviousPoint(prevPts)
		return nextPts

	def goThroughGraph(self):
		c = 0

		temp = None
		print("go through graph")
		if self.origin == None:
			self.origin = self.allPoint[0]
		#Premiere boucle ou on parcours tous les points
		#for ...
		tmpFirst = self.allPoint[0]
		temp = tmpFirst
		#on change second seulement si il y strictement plus de deux branches
		#car ca veut dire qu'il y a deux chemins possible au moins
		second = tmpFirst.getEastPoint()
		print("le premier point est : ", tmpFirst.getCoord(), " le second le plus a l'est : ", second.getCoord())

		#print("second get tinyer X : ", second.getTinierXExceptPreviousPoint(tmpFirst))
		print("le plus petit y du point : ", second.getCoord(), " avec comme point precedent : ", tmpFirst.getCoord(), " => ", second.getTinierYExceptPreviousPoint(tmpFirst).getCoord())
		print("le plus petit x du point : ", second.getCoord(), " avec comme point precedent : ", tmpFirst.getCoord(), " => ", second.getTinierXExceptPreviousPoint(tmpFirst).getCoord())

		tmpFirst.getEastPoint()
		second.getEastPoint()
		print("le plus grand x du point : ", second.getCoord(), " avec comme point precedent : ", tmpFirst.getCoord(), " => ", second.getBiggerXExceptPreviousPoint(tmpFirst).getCoord())
		#faut faire un if il n'y a qu'un chemin possible

		temp = self.goOnRight(second, tmpFirst)
		print("le prochain point = ", temp.getCoord(), ", le premier etait : ", tmpFirst.getCoord(), "et le second : ", second.getCoord())



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
		else:
			myGraph.addNumPoint(line)

	myGraph.printAllPoint()
	#createSegmentList
	print("\x1b[35m", inputData, "\033[00m")
	myGraph.goThroughGraph()
	return 0

if __name__=="__main__":       
    main() 