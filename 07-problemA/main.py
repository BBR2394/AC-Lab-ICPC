# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-05-04 10:45:25
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-05-12 12:28:28

import sys

def extractData(strblood):
	first = []
	if strblood[0] == "?":
		return ["?", "?"]
	else:
		if len(strblood) == 3:
			first = [strblood[0]+strblood[1], strblood[2]]
		elif len(strblood) == 2:
			first = [strblood[0], strblood[1]]
		return first

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
	return [getChildBlood(pOneB, pTwoB), getRhesus(pOneR, pTwoR)]

def cleanResult(res, pBlood):
	c = 0
	for i in res:
		c = len(i)
		if c >1:
			c = i.count('O')
			if c > 1 and pBlood == 'AB':
				raise("impossible")
			i.pop(i.index('O'))
	return res

def removeDoublon(res):
	final = []
	for i in res:
		if final.count(i[0]) == 0:
			final.append(i[0])
	return final

def addRhesus(fres):
	final = []
	for i in fres:
		final.append(i+'+')
		final.append(i+'-')
	return final

#en fait pour le parent je me suis compliqué la vie pour rien car en fait le second parent peut etre de tout les groupe sangunin et ce 
#independament de l'enfant, le seul cas ou il y a des exceptions c'est sir l'un des parents est AB, ou la l'enfant et forcement A ou B et jamais O
#mais aussi seulement si l'enfant est O, et le premier parent A ou B ou O, le second peut etre tout sauf AB
#finde the blood possible for the second parent
def findParentBlood(pOneB, pOneR, pTwoB, pTwoR, childBlood, childRhesus):
	res = []
	finalRes = []
	childPossibility = getPossibleSecondParent(childBlood)
	try:
		if pOneB == '?':
			for i in childPossibility:
				if i.count(pTwoB):
					i.pop(i.index(pTwoB))
			res = cleanResult(childPossibility, pTwoB)
		else:
			for i in childPossibility:
				if i.count(pOneB):
					i.pop(i.index(pOneB))
			res = cleanResult(childPossibility, pOneB)
		finalRes = removeDoublon(res)
		finalRes = addRhesus(finalRes)
	except: 
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
	finalRes = []
	for i in lst[0]:
		for j in lst[1]:
			finalRes.append(i+j)
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
	inputBlood = inputBlood.replace('\n', ' ')
	listBlood = inputBlood.split(" ")

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
		firstResult = findBloodChild(parentOneBlood, parentOneRhesus, parentTwoBlood, parentTwoRhesus)
		secondResult = getAllPossible(firstResult)
	if parentOneBlood == '?' or parentTwoBlood == '?':
		secondResult = findParentBlood(parentOneBlood, parentOneRhesus, parentTwoBlood, parentTwoRhesus, childBlood, childRhesus)
	secondResult.sort()
	printCorectlyResults(nb, secondResult, parentOneBlood, parentOneRhesus, parentTwoBlood, parentTwoRhesus, childBlood, childRhesus)
	return True

def main():
	allInput = []
	for line in sys.stdin:
		allInput.append(line)
	ret = True
	i = 0
	while ret:
		ret = getAllBlood(allInput[i], i)
		i += 1

if __name__=="__main__":
	main() 