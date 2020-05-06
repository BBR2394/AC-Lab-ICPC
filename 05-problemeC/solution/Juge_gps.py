class ville():
    def __init__(self, numero):
        self.numero = numero
        self.routes = {}


class map():
    def __init__(self, nbVille, objectif):
        self.viles = [ville(x) for x in range(nbVille)]
        self.objectif = self.viles[objectif]

    def creation_rout(self, a, b, longeur):
        self.viles[a].routes[b] = longeur
        self.viles[b].routes[a] = longeur

    def position_juge(self, nbJuge,juges_possition):
        self.juge_possition = [ville[int(juges_possition[x])-1] for x in range(nbJuge)]

    def __str__(self):
        return "Salut"


def lecteur():
    file = open('judges.in', 'r')
    lignes = file.readlines()
    while lignes:
        nbVille = int(lignes.pop(0))
        ob = int(lignes.pop(0))
        m = map(nbVille, ob)
        nbR = int(lignes.pop(0))
        for r in range(nbR):
            l = lignes.pop(0).split(" ")
            m.creation_rout(int(l[0]) - 1, int(l[1]) - 1, int(l[2]))
        nbJuge = int(lignes.pop(0))
        m.position_juge(nbJuge,lignes.pop(0).split(" "))
        print(m)



if __name__ == "__main__":
    print("---------------The Traveling Judges Problem------------------")
    lecteur()
    pass
