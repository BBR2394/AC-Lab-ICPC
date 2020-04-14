# -*- coding: utf-8 -*-
# @Author: Antoine Berthier

"""
PB ACM 1993 B
"""


class Somet:

    def __init__(self, coordonerX, coordonerY, name):
        self.name = name
        self.coordonerY = coordonerY
        self.coordonerX = coordonerX
        self.adj = []

    def __str__(self):
        return "Somet  " + self.name + " : " \
               + "adj:" + str(self.adj)

    def addAdj(self, sommetName):
        self.adj.append(sommetName)


class Graphe:
    """
      Un Objet Graphe est la representation graphique du pb
    """

    def __init__(self, nbSomet):
        self.cycles = []
        self.lSomet = {}
        self.ordre = 0

    def __str__(self):
        message = "Graphe : \n" + "Ordre du Graphe : " + str(self.ordre) + "\n"
        for key in self.lSomet:
            message += str(self.lSomet[key]) + "\n"
        return message

    def gestionSomet(self, x, y, xAdj, yAdj):
        name = str(x) + "_" + str(y)
        nameAdj = str(xAdj) + "_" + str(yAdj)
        if name not in self.lSomet:
            somet = Somet(x, y, name)
            self.lSomet[name] = somet
            self.ordre += 1
        else:
            somet = self.lSomet[name]

        if nameAdj not in self.lSomet:
            sometAdj = Somet(xAdj, yAdj, nameAdj)
            self.lSomet[nameAdj] = sometAdj
            self.ordre += 1
        else:
            sometAdj = self.lSomet[nameAdj]

        somet.addAdj(nameAdj)
        sometAdj.addAdj(name)

    def getSometName(self):
        return [*self.lSomet.keys()]

    def lancerPProfondeur(self, s):
        visited = {x: False for x in self.getSometName()}
        chemin = [s]
        self.parcoursProfondeur(s, visited, None, chemin)
        self.simplificationCycle()
        for cycle in self.cycles:
            print("Cycle :")
            print("len : ", len(cycle))
            for somet in cycle:
                print(somet, end=" ")
            print()
        print()
        self.cycleFinale()

    def parcoursProfondeur(self, s, visited, sp, chemin):
        visited[s] = True
        # print(s)
        for i in self.lSomet[s].adj:
            if not visited[i]:
                chemin.append(i)
                self.parcoursProfondeur(i, visited, s, chemin)
            elif visited[i] and i != sp:
                # print(i)
                # print(chemin[chemin.index(i):chemin.index(s)+1])
                if chemin[chemin.index(i):chemin.index(s) + 1]:
                    # print(chemin[chemin.index(i):chemin.index(s) + 1])
                    self.cycles.append(chemin[chemin.index(i):chemin.index(s) + 1])

    def simplificationCycle(self):
        self.cycles.sort(key=lambda v: len(v))


    def cycleFinale(self):
        newCycles = []
        for cycle in self.cycles:
            sometN2 = cycle[0].split("_")
            sometN1 = cycle[1].split("_")
            newCycle = [sometN2[0] + "_" + sometN2[1]]
            for sometN in cycle[2:len(cycle)]:
                sometN = sometN.split("_")
                if not ((sometN[0] == sometN1[0] and sometN1[0] == sometN2[0]) or (
                        sometN[1] == sometN1[1] and sometN1[1] == sometN2[1])):
                    newCycle.append(sometN1[0] + "_" + sometN1[1])
                sometN2 = sometN1
                sometN1 = sometN
            newCycle.append(sometN1[0] + "_" + sometN1[1])
            newCycles.append(newCycle)
        self.cycles = newCycles


def lectureGraphe():
    """Lis le fichier sample.in et retourn les graphe qui decrit

    :return:
        graphs : Tableaux de Graphe
    """

    f = open("sample.in", mode="r")
    lignes = f.readlines()
    f.close()
    graphes = []
    for x in range(len(lignes)):
        nbSomet = int(lignes.pop(0))
        if nbSomet == 0:
            break
        graphe = Graphe(nbSomet)
        for x in range(nbSomet):
            coordoner = lignes.pop(0).split()
            graphe.gestionSomet(int(coordoner[0]), int(coordoner[1]), int(coordoner[2]), int(coordoner[3]))
        graphes.append(graphe)
    return graphes


if __name__ == "__main__":
    graphs = lectureGraphe()
    for graph in graphs:
        print(graph)
        graph.lancerPProfondeur(graph.getSometName()[0])
        for cycle in graph.cycles:
            print("Cycle :")
            print("len : ", len(cycle))
            for somet in cycle:
                print(somet, end=" ")
            print()
        print()
