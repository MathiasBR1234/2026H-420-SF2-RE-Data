class Arbre:
    def __init__(self, coeur, enfants=None):
        self.coeur = coeur
        if enfants == None:
            self.enfants = []
        else:
            enfants_ = []
            for enfant in range(len(enfants)):
                enfants_.append((enfants[enfant]).coeur)
            self.enfants = enfants_

    def ajouter_enfant(self, donnees: list):
        for donnee in donnees:
            self.enfants.append(donnee)


class Noeud(Arbre):
    def __init__(self, coeur, enfants=None):
        super().__init__(coeur, enfants)

    def ajouter_enfant(self, donnees: list):
        for donnee in donnees:
            self.enfants.append(donnee)

    def __str__(self):
        return f"Le Noeud {self.coeur} a comme enfant {self.enfants}"


g = Noeud(5)
f = Noeud(4)
e = Noeud(7)
d = Noeud(6)
c = Noeud(3, [d, e])
b = Noeud(2, [f, g])
a = Arbre(Noeud(1, [b, c]))
