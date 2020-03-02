class Station:
    def __init__(self, nbStation, trains, horaires,
                 stationA, stationAT, stationB, stationBT):
        self.nbStation = nbStation
        self.adj = {stationA: stationAT, stationB: stationBT}
<<<<<<< HEAD
        if type(trains) is dict :
            self.trains = trains
        else:
            self.trains = [int(horaires.split()[x]) for x in range(trains)]
=======
        self.trains = [int(horaires.split()[x]) for x in range(trains)]
>>>>>>> 03-PBH

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

<<<<<<< HEAD
    def calcule_horaires(self):
        self.calcule_D_F()
        self.calcule_F_D()

    def calcule_D_F(self):
        station = self.ladj[1]
        stationA = self.ladj[0]
        station.trains[2] = [int(h) + int(station.adj[0]) for h in stationA.trains]
        for x in range(2, len(self.ladj) - 1):
            station = self.ladj[x]
            stationA = self.ladj[x - 1]
            station.trains[x + 1] = [int(h) + int(station.adj[x - 1]) for h in stationA.trains[x]]

    def calcule_F_D(self):
        station = self.ladj[self.ordre - 2]
        stationB = self.ladj[self.ordre - 1]
        station.trains[self.ordre - 3] = [int(h) + int(station.adj[self.ordre - 1]) for h in stationB.trains]
        for x in range(self.ordre - 2, 1, - 1):
            station = self.ladj[x]
            stationA = self.ladj[x - 1]
            station.trains[x - 1] = [int(h) + int(station.adj[x + 1]) for h in stationA.trains[x]]
=======
    def calcule_horaire(self):
        pass
>>>>>>> 03-PBH


def lire_graphe():
    f = open("metro.in", mode="r")
    lignes = f.readlines()
    f.close()
    for x in range(len(lignes)):
        nbStation = int(lignes.pop(0))
        heurRDV = int(lignes.pop(0))
        tmpTrajet = lignes.pop(0).split()
        nbTrain = int(lignes.pop(0))
        heurDepart = lignes.pop(0)
        nbTrainGarN = int(lignes.pop(0))
        heurDepartGarN = lignes.pop(0)

        stationStart = Station(0, nbTrain, heurDepart, None, None, 2, tmpTrajet[0])
        stationEnd = Station(nbStation - 1, nbTrainGarN, heurDepartGarN, nbStation - 2, tmpTrajet[nbStation - 2], None,
                             None)
        ladj = [stationStart]
        for numero in range(1, nbStation - 1):
            ladj.append(
                Station(numero, {}, None, numero - 1, tmpTrajet[numero - 1], numero + 1, tmpTrajet[numero]))

        ladj.append(stationEnd)
        return Graphe(ladj, nbStation, heurRDV)


if __name__ == "__main__":
    graphe = lire_graphe()
    graphe.calcule_horaires()
    print(graphe)
