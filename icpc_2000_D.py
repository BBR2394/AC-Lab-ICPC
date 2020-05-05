
def AireMinimale(Dimension,coordonnée):
    Aire = 0;
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


    else:

    if Dimension == 4 :


def Distance2point(x1,y1,x2,y2):

    return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));

def AireRectangle(longueur,largeur):

    return longueur*largeur;


class Gift_parsing:


    def __init__(self):
        self.fInput = open('test.txt')
        self.fOutput = open('output.txt', 'w')
        self.results = []
    def sequential_work(self):
        self.getInput()
