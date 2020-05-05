
def AireMinimale(Dimension,coordonnée):
    liste_coordonnée =[];
    fichier = open("test.txt", "r");

    for ligne in fichier:
        a = ligne.replace(",", "")
        b = a.split()
        for i in range(len(b)):
            c = b[i]
            d = ma_liste.append(c)
    print(d);

    if Dimension ==3 :
        return False

    else:
        if Dimension == 4 :


def Distance2point(p1,p2):

    return ()

def AireRectangle(longueur,largeur):

    return longueur*largeur;


class Gift_parsing:


    def __init__(self):
        self.fInput = open('test.txt')
        self.fOutput = open('output.txt', 'w')
        self.results = []
    def sequential_work(self):
        self.getInput()
