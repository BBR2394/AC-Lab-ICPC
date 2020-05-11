import math


class ville():
    def __init__(self, numero):
        self.numero = numero + 1
        self.routes = {}

    def __str__(self):
        routes = ""
        for k in self.routes:
            routes += "Vers la ville : " + str(k + 1) + " a " + str(self.routes[k]) + "\n"

        return "Ville N°: " + str(self.numero) + "\n" + routes


class map():
    def __init__(self, nbVille, objectif):
        self.nbVilles = nbVille
        self.villes = [ville(x) for x in range(nbVille)]
        self.objectif = self.villes[objectif - 1]

    def creation_rout(self, a, b, longeur):
        self.villes[a].routes[b] = longeur
        self.villes[b].routes[a] = longeur

    def position_juge(self, nbJuge, juges_possition):
        self.juge_possition = []
        for x in range(nbJuge):
            self.juge_possition.append(self.villes[int(juges_possition[x]) - 1])

    def __str__(self):
        description = "------------------ MAP --------------- \n"
        description += "Nombre de juge : " + str(len(self.juge_possition)) + "\n"
        description += "Objectif : Ville N " + str(self.objectif.numero) + "\n"
        description += "Nombre de villes : " + str(self.nbVilles) + "\n"
        description += "Villes : \n"
        for ville in self.villes:
            description += str(ville)

        return description

    def parcour_juge(self):
        for j in self.juge_possition:
            self.Dijkstra(j)

    def Dijkstra(self, s):
        dist = [math.inf for x in range(self.nbVilles)]
        dist[s.numero - 1] = 0
        sptSet = [False for x in range(self.nbVilles)]

        for count in range(self.nbVilles):
            u = self.minDistance(dist, sptSet)

            while dist[self.objectif.numero - 1 ] == math.inf:
                if u.numero - 1 in s.routes and\
                        sptSet[s.numero - 1] == False and \
                        dist[s.numero - 1] > dist[u.numero - 1] + s.routes[u.numero - 1]:
                    dist[s.numero - 1] = dist[u.numero - 1] + s.routes[u.numero - 1]
                    s = u

        self.printSolution(dist)

    def minDistance(self, dist, sptSet):
        min = math.inf
        for v in self.villes:
            if dist[v.numero - 1] < min and sptSet[v.numero - 1] == False:
                min = dist[v.numero - 1]
                min_index = v.numero - 1
        return self.villes[min_index]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.nbVilles):
            print(node, "t", dist[node])


def lecteur():
    maps = []
    file = open('judges.in', 'r')
    lignes = file.readlines()
    while lignes:
        if lignes[0] == "\n":
            lignes.pop(0)
        if lignes[0] == "-1":
            break
        nbVille = int(lignes.pop(0))
        ob = int(lignes.pop(0))
        m = map(nbVille, ob)
        nbR = int(lignes.pop(0))
        for r in range(nbR):
            l = lignes.pop(0).split(" ")
            m.creation_rout(int(l[0]) - 1, int(l[1]) - 1, int(l[2]))
        nbJuge = int(lignes.pop(0))
        m.position_juge(nbJuge, lignes.pop(0).split(" "))
        maps.append(m)
    return maps


if __name__ == "__main__":
    print("---------------The Traveling Judges Problem------------------")
    maps = lecteur()
    for m in maps:
        print(m)
        m.parcour_juge()
