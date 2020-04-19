"""
Ce programe dois résoudre le pb C du sujet 2000 du concour ICPC
Fais dans le cadre du cour Ac Lab du M1-III de la FGES
"""
import math

class Chain:
    """
    La class chain represente les chaines
    """

    def __init__(self, elements):  # del -1 -1
        elements.pop()
        self.nb_maillon = int(elements.pop(0))
        self.chaines_relier = [False for x in range(self.nb_maillon-1)]
        self.maillons = {}
        for element in elements:
            index, lien = element.split(" ")
            if int(index) not in self.maillons:
                self.maillons[int(index)] = [int(lien)]
            else:
                self.maillons[int(index)].append(int(lien))

    def parcour(self):
        for index in self.maillons:
            for lien in self.maillons[index]:
                min_ind = min([index, lien])
                max_ind = max([index, lien])

                for nb in range(min_ind-1, max_ind-1):
                    self.chaines_relier[nb] = True


def read_chains():
    """
    Cette fonction lit le fichier chains.in
    Avec les informations du fichier elle construit les chaines
    qu'elle renvoie dans un tab

    :return: tab de Chaine
    """
    f = open("chains.in", mode='r')
    lignes = f.readlines()
    f.close()
    chains = []
    for ligne in lignes:
        elements = ligne.split("  ")
        if len(elements) > 1:
            chain = Chain(elements)
            chains.append(chain)

    return chains


if __name__ == "__main__":
    chaines = read_chains()

    for chaine in chaines:
        chaine.parcour()

    print("END")
