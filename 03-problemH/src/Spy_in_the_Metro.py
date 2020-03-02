class Station:
    def __init__(self, nbStation, trains, horaires,
                stationA, stationAT, stationB, stationBT):
        self.nbStation = nbStation
        self.adj = {stationA: stationAT, stationB: stationBT}
        self.trains = [int(horaires.split()[x]) for x in range(trains)]

    def __str__(self):
        return "Station N : " + str(self.nbStation) \
               + "\nAdj : " + str(self.adj) \
               + "\nHoraire :" + str(self.trains)


class Graphe:
    def __init__(self, ladj, ordre, time):
        # les sommets sont les entiers 0,1,2....
        # Pour chaque sommets i, ladj[i] est la liste
        # des voisins de i
        self.ladj = ladj  # liste adjacence
        self.ordre = ordre
        self.time = time

    def __str__(self):
        message = "Le graphe et d'ordre : " + str(self.ordre) + "\n"
        message += "il a comme liste d'adjacence : " + str([str(station) for station in self.ladj]) + "\n"
        message += "Et comme temps : " + str(self.time)
        return message

    def calcule_horaire(self):
        pass


def lire_graphe():
    f = open("metro.in", mode="r")
    lignes = f.readlines()
    f.close()
    for x in range(len(lignes)):
        nbStation = int(lignes.pop(0))
        heurRDV = int(lignes.pop(0))
        tmpTrajet = lignes.pop(0)
        nbTrain = int(lignes.pop(0))
        heurDepart = lignes.pop(0)
        nbTrainGarN = int(lignes.pop(0))
        heurDepartGarN = lignes.pop(0)

        stationStart = Station(1, nbTrain, heurDepart, None, None, 2, tmpTrajet[0])
        stationEnd = Station(nbStation, nbTrainGarN, heurDepartGarN, nbStation - 1, tmpTrajet[nbStation - 1], None,
                             None)
        ladj = [stationStart]
        for numero in range(1, nbStation - 1):
            ladj.append(
                Station(numero, 0, [], numero - 1, tmpTrajet[nbStation - 1], numero + 1, tmpTrajet[nbStation + 1]))

        ladj.append(stationEnd)
        return Graphe(ladj, nbStation, heurRDV)


if __name__ == "__main__":
    graphe = lire_graphe()
    print(graphe)
