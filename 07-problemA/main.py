# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-05-04 10:45:25
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-05-11 11:36:18

import sys

def extractData(strblood):
	print("dans extract data : ", strblood, " taille ", len(strblood))
	first = []
	if strblood[0] == "?":
		return ["?", "?"]
	else:
		if len(strblood) == 3:
			first = [strblood[0]+strblood[1], strblood[2]]
			print("first = ", first)
		elif len(strblood) == 2:
			first = [strblood[0], strblood[1]]
			print("first = ", first)
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

def getPossibleSecondParent(childB):
	bloodCorespondance = {
	'O': [['O', 'O']],
	'A': [['A', 'A'], ['O', 'A'], ['A', 'O']],
	'B': [['B', 'B'], ['O', 'B'], ['B', 'O']],
	'AB': [['A', 'B'], ['B', 'A']]
	}

def getRhesus(pOne, pTwo):
	rhesusCorespondance = {'++' : ['+'], '+-': ['+', '-'], '-+': ['+', '-'], '--': ['-']}
	return rhesusCorespondance[pOne+pTwo]

def findBloodChild(pOneB, pOneR, pTwoB, pTwoR):
	print("dans find blood child : ", pOneB, " ", pOneR, " ", pTwoB, " ", pTwoR)
	return [getChildBlood(pOneB, pTwoB), getRhesus(pOneR, pTwoR)]

def findParentBlood(pOneB, pOneR, pTwoB, pTwoR, childBlood, childRhesus):
	print("$>dans findParentBlood : ", pOneB, " ", pOneR, " ", pTwoB, " ", pTwoR)
	return []

def checkEnd(lst):
	if lst[0] == 'E':
		if lst[1] == 'N':
			if lst[2] == 'D':
				return True
	else :
		return False

def getAllPossible(lst):
	print("get all possible ")
	finalRes = []
	for i in lst[0]:
		for j in lst[1]:
			finalRes.append(i+j)
	print("a la fin de get all possible : ", finalRes)

def getAllBlood(inputBlood):
	parentOneBlood = ""
	parentOneRhesus = ""
	parentTwoBlood = ""
	parentTwoRhesus = ""
	childBlood = ""
	childRhesus = ""

	listBlood = inputBlood.split(" ")
	print("la liste : ", listBlood)
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
		print("le resultat est : ", firstResult)
		secondResult = getAllPossible(firstResult)
		print("finally : ", secondResult)
	if parentOneBlood == '?' or parentTwoBlood == '?':
		print("la je dois cherche le parent ...")
		findParentBlood(parentOneBlood, parentOneRhesus, parentTwoBlood, parentTwoRhesus, childBlood, childRhesus)
	return True

def main():
	allInput = []
	print("here is where the magik happen")
	for line in sys.stdin:
		print("en all input: ", line, end="")
		allInput.append(line)
	print("\n")
	ret = True
	i = 0
	while ret:
		ret = getAllBlood(allInput[i])
		i += 1

if __name__=="__main__":
	main() 