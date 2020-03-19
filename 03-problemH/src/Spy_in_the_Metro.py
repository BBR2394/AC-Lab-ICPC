import math

"""
Les Station sont les somets du Graphe
"""


class Station:
    def __init__(self, nbStation, trains, horaires,
                 stationA, stationAT, stationB, stationBT):
        self.nbStation = nbStation
        self.adj = {stationA: stationAT, stationB: stationBT}
        if type(trains) is dict:
            self.trains = trains
        else:
            self.trains = [int(horaires.split()[x]) for x in range(trains)]
        self.horaireTerminus = None

    def __str__(self):
        message = "Station N : " + str(self.nbStation) \
                  + "\nAdj : " + str(self.adj) \
                  + "\nHoraire :" + str(self.trains)
        if self.horaireTerminus:
            message += "\nHoraire Terminus :" + str(self.horaireTerminus)
        return message

    def prochainTrain(self, horaire):
        minDelai = math.inf
        nbKey = 0
        cKey = 0
        if type(self.trains) is dict:
            for key in self.trains:
                cKey += 1
                for x in range(len(self.trains[key])):
                    if self.trains[key][x] >= horaire and abs(self.trains[key][x] - horaire) <= minDelai:
                        minDelai = horaire - self.trains[key][x]
                        nbKey = key - 2 if cKey == 1 else key + 2
        else :
            for x in range(len(self.horaireTerminus)):
                if abs(self.horaireTerminus[x] - horaire) < minDelai:
                    minDelai = abs(self.horaireTerminus[x] - horaire)
                    nbKey = self.nbStation - 1
        return nbKey, minDelai


"""
Class Graphe  qui pertmet de remrensenter  la ligne de metro
Cette classe contiendra les methode pour calculer le resulta
"""


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
        message += "il a comme liste d'adjacence : \n"
        for station in self.ladj:
            message += str(station) + "\n\n"
        message += "Et comme temps : " + str(self.time)
        return message

    def calcule_horaires(self):
        self.calcule_D_F()
        self.calcule_F_D()

    """
    Methode qui calculer les horaire des trains dans le sens Debut -> Fin 
    """

    def calcule_D_F(self):
        station = self.ladj[1]
        stationA = self.ladj[0]
        station.trains[2] = [int(h) + int(station.adj[0]) for h in stationA.trains]
        for x in range(2, len(self.ladj) - 1):
            station = self.ladj[x]
            stationA = self.ladj[x - 1]
            station.trains[x + 1] = [int(h) + int(station.adj[x - 1]) for h in stationA.trains[x]]

        x = len(self.ladj) - 1
        station = self.ladj[x]
        stationA = self.ladj[x - 1]
        station.horaireTerminus = [int(h) + int(station.adj[x - 1]) for h in stationA.trains[x]]

    """
    Methode qui calculer les horaire des trains dans le sens Fin -> Debut 
    """

    def calcule_F_D(self):
        station = self.ladj[self.ordre - 2]
        stationB = self.ladj[self.ordre - 1]
        station.trains[self.ordre - 3] = [int(h) + int(station.adj[self.ordre - 1]) for h in stationB.trains]
        for x in range(self.ordre - 3, 0, - 1):
            station = self.ladj[x]
            stationB = self.ladj[x + 1]
            station.trains[x - 1] = [int(h) + int(station.adj[x + 1]) for h in stationB.trains[x]]


"""
Function qui transforme le fichier metro.io en Graphe Non Orianter

:return: Graphe
"""


def lire_graphe():
    f = open("metro.in", mode="r")
    lignes = f.readlines()
    f.close()
    graphes = []
    cas = 0
    for x in range(0, len(lignes), 7):
        cas += 1
        nbStation = int(lignes.pop(0))
        if nbStation == 0:
            break
        try:
            heurRDV = int(lignes.pop(0))
            tmpTrajet = lignes.pop(0).split()
            nbTrain = int(lignes.pop(0))
            heurDepart = lignes.pop(0)
            nbTrainGarN = int(lignes.pop(0))
            heurDepartGarN = lignes.pop(0)

            """
            On calcule dabord les stations 0 et N 
            """
            stationStart = Station(0, nbTrain, heurDepart, None, None, 2, tmpTrajet[0])
            stationEnd = Station(nbStation - 1, nbTrainGarN, heurDepartGarN, nbStation - 2, tmpTrajet[nbStation - 2],
                                 None,
                                 None)
            ladj = [stationStart]
            """
            On calcule les stations de 1 a N-1 
            """
            for numero in range(1, nbStation - 1):
                ladj.append(
                    Station(numero, {}, None, numero - 1, tmpTrajet[numero - 1], numero + 1, tmpTrajet[numero]))
            ladj.append(stationEnd)
        except:
            graphes.append(None)
            pass
        else:
            graphes.append(Graphe(ladj, nbStation, heurRDV))

    return graphes


def parcour(graphe):
    delaiFinal = 0
    heureCourante = graphe.time
    station = graphe.ladj[graphe.ordre - 1]
    minDelai = math.inf
    for x in range(len(station.horaireTerminus)):
        if abs(station.horaireTerminus[x] - graphe.time) < minDelai:
            minDelai = abs(station.horaireTerminus[x] - graphe.time)

    delaiFinal += minDelai
    heureCourante -= delaiFinal + int(station.adj[station.nbStation - 1])
    station = graphe.ladj[station.nbStation - 1]

    while station.nbStation != 0:
        nextStation, nextdelai = station.prochainTrain(heureCourante)
        delaiFinal += nextdelai
        heureCourante -= delaiFinal + int(station.adj[nextStation])
        station = graphe.ladj[nextStation]

    for x in range(len(station.trains)):
        if abs(station.trains[x] - graphe.time) < minDelai:
            minDelai = abs(station.trains[x] - graphe.time)

    delaiFinal += minDelai

    return delaiFinal


if __name__ == "__main__":
    graphes = lire_graphe()
    nbGraphes = 0
    for graphe in graphes:
        nbGraphes += 1
        if graphe:
            try:
                graphe.calcule_horaires()
            except:
                print("Case Number " + str(nbGraphes) + " : impossible")
            else:
                print("Case Number " + str(nbGraphes) + " : " + str(parcour(graphe)))
        else:
            print("Case Number " + str(nbGraphes) + " : impossible")
