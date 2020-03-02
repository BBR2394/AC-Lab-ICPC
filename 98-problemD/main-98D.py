# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-03-02 15:32:07
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-03-02 15:46:14



import sys

#def getInputInList():


def main():
    print("Here is where the magik happened 98D")

main()

print(sys.argv)
inputData = []

for line in sys.stdin:
	print("une ligne ", end=" : ")
	print(line, end="")
	inputData.append(line)

print(inputData)

#print(sys.stdin.read(1))
