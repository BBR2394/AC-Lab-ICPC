# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-05-04 10:45:25
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-05-04 11:50:01

import sys

def extractData(strblood):
	if strblood[0] == "?":
		return ["?", "?"]
	else:
		return [strblood[0], strblood[1]]

def getAllBlood(inputBlood):
	parentOneBlood = ""
	parentOneRhesus = ""
	parentTwoBlood = ""
	parentTwoRhesus = ""
	childBlood = ""
	childRhesus = ""
	listBlood = inputBlood.split(" ")
	print("la liste : ", listBlood)
	res = extractData(listBlood[0])
	parentOneBlood = res[0]
	parentOneRhesus = res[1]
	res = extractData(listBlood[1])
	parentTwoBlood = res[0]
	parentTwoRhesus = res[1]
	res = extractData(listBlood[2])
	childBlood = res[0]
	childRhesus = res[1]
	print("les données : ", parentOneBlood, " ", parentOneRhesus, " ", parentTwoBlood, " ", parentTwoRhesus, " ", childBlood, " ", childRhesus)

def main():
	allInput = []
	print("here is where the magik happen")
	for line in sys.stdin:
		print("en premier: ", line, end="")
		allInput.append(line)
	print("\n")

	getAllBlood(allInput[0])

if __name__=="__main__":
	main() 