# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-03-02 15:32:07
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-03-19 10:02:38

import sys

Nmax = 5

class Storage:
	keyword = ""
	weight = 0

	def __init__(self, kw, wght):
		#print("New storage with keyword : ", kw, " and weight : ", wght)
		self.weight = wght
		self.keyword = kw

	def __eq__(self, other):
		if self.keyword == other:
			return True
		else :
			return False

	def getWeight(self):
		return self.weight

	def getKeyword(self):
		return self.keyword

	def getInformation(self):
		formatString = "kw : ", self.keyword, " and weight : ", self.weight
		return formatString

class Query:
	keywordToFindLst = []
	
	def __init__(self, maxKw, keywordLst):
		#print("query manager create")
		currentWeight = maxKw
		for i in keywordLst:
			#print("querymanager add : ", i, " and weighth : ", currentWeight)
			self.keywordToFindLst.append(Storage(currentWeight, i))
			currentWeight -= 1


# This object take everything about the pages storage
class SearchEngine:
	keyword = []
	maxKW = 0
	#storageList est une liste de liste d'objet Storage
	storageList = []
	dicoFromLastQuery = {}

	def __init__(self, maxKeyWord):
		#lstKeyword = lstKeyword[:]
		self.maxKW = maxKeyWord

	def printStorage(self):
		print("au debut de storage : ", len(self.storageList))
		for i in range(len(self.storageList)): #for i in range(len(lst))
			print("la page : ", i)
			for j in self.storageList[i]:
				print("un element : ", j.getInformation())

	def addPage(self, keywordLst):
		currentWeight = Nmax
		# print("here i am going to create and add a new page")
		tempStorageList = []
		for i in keywordLst:
			# print("i = ", i)
			# print("current poid ", currentWeight)
			tempElem = Storage(i, currentWeight)
			# print("tempElem kw : ", tempElem.getKeyword(), " and poids : ", tempElem.getWeight())
			tempStorageList.append(tempElem)
			currentWeight -= 1
		self.storageList.append(tempStorageList)

	def getKey(self, item):
		return item[1]

	def orderDictionary(self, dico):
		# print("in orderDictionary")
		tpls_dico = list(dico.items())
		tpls_sorted = sorted(tpls_dico, key=self.getKey, reverse=True)
		return tpls_sorted

	#by sending a query, the ouptu is the pages result for this query
	#aQuery juste la liste des mots
	def find(self, aQuery):
		resPerPages = {}
		for i in range(len(self.storageList)):
			resPerPages[i] = 0
		# print("dico resultats = ", resPerPages)
		# print("here i will find the pages for the query")
		currentWeight = self.maxKW
		for q in aQuery:
			for i in range(len(self.storageList)):
				for j in self.storageList[i]:
					if j == q:
						resPerPages[i] += currentWeight * j.getWeight()
						# print(j.getKeyword() , " et ", q, "  sont egaux et donne en poids ", resPerPages[i])
			currentWeight = self.maxKW - 1

		resSorted = self.orderDictionary(resPerPages)
		dicoFromLastQuery = resSorted
		#print("le dico en tuples : ", resSorted)
		return resSorted

def storeInputData(inputDt, searchEngn):
	allInput = []
	aLine = []
	queryInput = []
	#print("here i'll get the input data")
	for i in inputDt:
		#print(i, end="")
		aLine = i.split()
		if aLine[0] == 'P':
			# print("c'est une page ", aLine)
			allInput.append(aLine)
			aLine.pop(0)
			searchEngn.addPage(aLine)
		elif aLine[0] == 'Q':
			# print("c'est une requete ", aLine)
			allInput.append(aLine)
			aLine.pop(0)
			queryInput.append(aLine)
	# print("allInput : ", allInput)
	# print("query input only : ", queryInput)
	return queryInput

def printResult(result):
	# print("les Resultats !")
	for i in range(len(result)):
		print("Q" + str(i+1), end=" : ")
		for j in result[i]:
			if j[1] != 0:
				print("P" + str(j[0]+1), end=" ")
		print(end="\n")


def main():
    # print("Here is where the magik happened 98D")
    inputData = []
    dicoList = []
    se = SearchEngine(Nmax)
    for line in sys.stdin:
    	#print("une ligne ", end=" : ")
    	#print(line, end="")
    	if (line[0] == 'E'):
    		break
    	inputData.append(line)
    # print(inputData)
    queryList = storeInputData(inputData, se)
    # se.printStorage()
    for i in queryList:
    	dicoList.append(se.find(i))

    # print("dico list : ", dicoList)

    printResult(dicoList)
    return 0
    # queryOne = Query(Nmax, ['Smalltalk', 'computers'])
    # queryTwo = Query(Nmax, ['Smalltalk', 'programming'])
    # queryThree = Query(Nmax, ['computers'])
    # se.addPage(['Smalltalk', 'programming', 'computers'])
    #se.printStorage()
    # se.addPage(['COBOL', 'programming'])
    #se.addPage(['COBOL', 'programming'])
    # se.addPage(['COBOL', 'computers'])
    # se.printStorage()
    # se.find(['Smalltalk', 'computers'])
    #qManager = QueryManager()
    #qManager.addQuery(queryOne)


main()
# print(sys.argv)
#print(sys.stdin.read(1))

# if __name__=="__main__":       
#     main() 