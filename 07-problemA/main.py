# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-05-04 10:45:25
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-05-12 12:26:13

import sys

def extractData(strblood):
	#print("dans extract data : ", strblood, " taille ", len(strblood))
	first = []
	if strblood[0] == "?":
		return ["?", "?"]
	else:
		if len(strblood) == 3:
			first = [strblood[0]+strblood[1], strblood[2]]
			#print("first = ", first)
		elif len(strblood) == 2:
			first = [strblood[0], strblood[1]]
			#print("first = ", first)
		return first
		#return [strblood[0], strblood[1]]

def getChildBlood(pOne, pTwo):
	bloodCorespondance = {	'AA': ['A'],
							'AB': ['AB'],
							'AO': ['A'],
							'BA': ['AB'],
							'BB': ['B'],
							'BO': ['B'],
							'OA': ['A'],
							'OB': ['B'],
							'OO': ['O'],
							'ABA':['A', 'AB'],
							'ABB':['B', 'AB'],
							'ABO':['A', 'B'],
							'ABAB':['A', 'B', 'AB']
							}
	return bloodCorespondance[pOne+pTwo]

#according to the blood type, give possible allele du chromosome de l'enfant
def getAllele(childB):
	bloodCorespondance = {
	'O': [['O', 'O']],
	'A': [['A', 'A'], ['O', 'A'], ['A', 'O']],
	'B': [['B', 'B'], ['O', 'B'], ['B', 'O']],
	'AB': [['A', 'B'], ['B', 'A']]
	}
	return bloodCorespondance[childB]


def getPossibleSecondParent(childB):
	bloodCorespondance = {
	'O': [['O', 'O'], ['O', 'A'], ['A', 'O'], ['O', 'B'], ['B', 'O']],
	'A': [['A', 'A'], ['O', 'A'], ['A', 'O'], ['O', 'B'], ['B', 'O']],
	'B': [['B', 'B'], ['O', 'B'], ['B', 'O'], ['O', 'A'], ['A', 'O']],
	'AB': [['A', 'B'], ['B', 'A']]
	}
	return bloodCorespondance[childB]

def getRhesus(pOne, pTwo):
	rhesusCorespondance = {'++' : ['+'], '+-': ['+', '-'], '-+': ['+', '-'], '--': ['-']}
	return rhesusCorespondance[pOne+pTwo]

def findBloodChild(pOneB, pOneR, pTwoB, pTwoR):
	#print("dans find blood child : ", pOneB, " ", pOneR, " ", pTwoB, " ", pTwoR)
	return [getChildBlood(pOneB, pTwoB), getRhesus(pOneR, pTwoR)]

def cleanResult(res, pBlood):
	c = 0
	for i in res:
		c = len(i)
		if c >1:
			c = i.count('O')
			if c > 1 and pBlood == 'AB':
				#print("impossible")
				raise("impossible")
			i.pop(i.index('O'))
	#print("apres netoyage 1 : ", res, " parent blood : ", pBlood)
	return res

def removeDoublon(res):
	final = []
	for i in res:
		if final.count(i[0]) == 0:
			final.append(i[0])
	#print("AU FINAL DU FINAL : ", final)
	return final

def addRhesus(fres):
	final = []
	for i in fres:
		final.append(i+'+')
		final.append(i+'-')
	#print("avec rhesus :", final)
	return final

#en fait pour le parent je me suis compliqué la vie pour rien car en fait le second parent peut etre de tout les groupe sangunin et ce 
#independament de l'enfant, le seul cas ou il y a des exceptions c'est sir l'un des parents est AB, ou la l'enfant et forcement A ou B et jamais O
#mais aussi seulement si l'enfant est O, et le premier parent A ou B ou O, le second peut etre tout sauf AB
#finde the blood possible for the second parent
def findParentBlood(pOneB, pOneR, pTwoB, pTwoR, childBlood, childRhesus):
	res = []
	finalRes = []
	#print("$>dans findParentBlood : ", pOneB, " ", pOneR, " ", pTwoB, " ", pTwoR, " ", childBlood, " ", childRhesus)
	#print("la ppopssibilité du deuxieme parent : ", getPossibleSecondParent(childBlood))
	childPossibility = getPossibleSecondParent(childBlood)
	try:
		if pOneB == '?':
			#parentAllele = getPossibleSecondParent(pTwoB)
			#print("parent Two allele : ", parentAllele)
			for i in childPossibility:
				#print("$>i:", i)
				if i.count(pTwoB):
					i.pop(i.index(pTwoB))
			#print("new possible parent : ", childPossibility)
			res = cleanResult(childPossibility, pTwoB)
		else:
			#parentAllele = getPossibleSecondParent(pOneB)
			#print("parent One allele : ", parentAllele)
			for i in childPossibility:
				#print("$>i:", i)
				if i.count(pOneB):
					i.pop(i.index(pOneB))
			#print("new possible parent : ", childPossibility)
			res = cleanResult(childPossibility, pOneB)
		finalRes = removeDoublon(res)
		finalRes = addRhesus(finalRes)
	except: 
		#print("excepption retourné")
		return ["IMPOSSIBLE"]
	return finalRes

def checkEnd(lst):
	if lst[0] == 'E':
		if lst[1] == 'N':
			if lst[2] == 'D':
				return True
	else :
		return False

def getAllPossible(lst):
	#print("get all possible ")
	finalRes = []
	for i in lst[0]:
		for j in lst[1]:
			finalRes.append(i+j)
	#print("a la fin de get all possible : ", finalRes)
	return finalRes

def printCorectlyResults(casenb, finalRes, parentOneBlood, parentOneRhesus, parentTwoBlood, parentTwoRhesus, childBlood, childRhesus):
	if childBlood == '?':
		print("Case ", casenb, ":", parentOneBlood, parentOneRhesus, " ", parentTwoBlood, parentTwoRhesus, "{", end="")
		for i in finalRes:
			print(i, ',', end="")
		print("}")
	else:
		if parentOneBlood == "?":
			print("Case ", casenb, ":", finalRes,  " ", parentTwoBlood, parentTwoRhesus, " ", childBlood, childRhesus)
		else:
			print("Case ", casenb, ":", parentOneBlood, parentOneRhesus, " ", finalRes, " ", childBlood, childRhesus)


def getAllBlood(inputBlood, nb):
	parentOneBlood = ""
	parentOneRhesus = ""
	parentTwoBlood = ""
	parentTwoRhesus = ""
	childBlood = ""
	childRhesus = ""
	#print("input blood, ", inputBlood)
	inputBlood = inputBlood.replace('\n', ' ')
	#print("input blood, ", inputBlood)
	listBlood = inputBlood.split(" ")
	#print("la liste : ", listBlood)
	if checkEnd(listBlood):
		return False
	res = extractData(listBlood[0])
	parentOneBlood = res[0]
	parentOneRhesus = res[1]

	res = extractData(listBlood[1])
	parentTwoBlood = res[0]
	parentTwoRhesus = res[1]

	res = extractData(listBlood[2])
	childBlood = res[0]
	childRhesus = res[1]

	if childBlood == '?':
		#print("pour recherche l'enfant")
		firstResult = findBloodChild(parentOneBlood, parentOneRhesus, parentTwoBlood, parentTwoRhesus)
		#print("le resultat est : ", firstResult)
		secondResult = getAllPossible(firstResult)
		#print("finally : ", secondResult)
	if parentOneBlood == '?' or parentTwoBlood == '?':
		#print("pour recherche le parent")
		#print("la je dois cherche le parent ...")
		secondResult = findParentBlood(parentOneBlood, parentOneRhesus, parentTwoBlood, parentTwoRhesus, childBlood, childRhesus)
	#print("a la fin")
	#print(secondResult)
	secondResult.sort()
	#print(secondResult)
	printCorectlyResults(nb, secondResult, parentOneBlood, parentOneRhesus, parentTwoBlood, parentTwoRhesus, childBlood, childRhesus)
	return True

def main():
	allInput = []
	#print("here is where the magik happen")
	for line in sys.stdin:
		#print("en all input: ", line, end="")
		allInput.append(line)
	#print("\n")
	ret = True
	i = 0
	while ret:
		ret = getAllBlood(allInput[i], i)
		i += 1

if __name__=="__main__":
	main() 