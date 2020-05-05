class ville():
    def __init__(self, numero):
        self.numero = numero

class map() :
    def __init__(self, nbVille, objectif):
        self.viles = [ville(x) for x in range(nbVille)]
        self.objectif = self.viles[objectif]



if __name__=="__main__":
    print("---------------The Traveling Judges Problem------------------")

    pass
