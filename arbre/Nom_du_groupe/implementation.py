class Binary_nodes:
    def __init__(self, valeur: float, fils_gauche, fils_droit, id):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit
        self.id = id

    def check_for_children(self):
        if self.fils_gauche == None and self.fils_droit == None:
            return "empty"
        elif self.fils_gauche == None or self.fils_droit == None:
            if self.fils_gauche == None:
                return "gauche"
            else:
                return "droit"
        else:
            return False




class Binary_tree:
    def __init__(self, racine: Binary_nodes):
        self.racine = racine
    
    def add_node(self, ajout:Binary_nodes):        
        current_node = self.racine
        if ajout.valeur > current_node.valeur:
            match current_node.check_for_children():
                case "empty":
                    current_node.fils_droit = ajout
                case "gauche":
                    current_node = current_node.fils_droit
                case "droit":
                    current_node.fils_droit = ajout
                case False:
                    current_node = current_node.fils_droit
                case _:
                    print("erreur interne 2")

        elif ajout.valeur < current_node.valeur:
            match current_node.check_for_children():
                case "empty":
                    current_node.fils_gauche = ajout
                case "gauche":
                    current_node.fils_gauche = ajout
                case "droit":
                    current_node = current_node.fils_gauche
                case False:
                    current_node = current_node.fils_gauche
                case _:
                    print("erreur interne 3")

        else:
            print("Erreur: la valeur sprecifiée est la racine")

    def remove_node(self, valeur: Binary_nodes):
        arbre1 = Binary_tree(valeur.fils_droit)
        arbre2 = Binary_tree(valeur.fils_gauche) # La fonction detruit la valeur et crée deux arbres avec les deux enfant
        del valeur
        return arbre1, arbre2
    
    def hauteur(self):
        pass
    
    def search(self, clef: Binary_nodes.valeur):
        index = None
        current_node = self.racine
        while index == None:
            if clef < current_node.valeur:
                if current_node.check_for_children() == "gauche":
                    current_node = current_node.fils_gauche
                else:
                    index = current_node.id
            elif clef > current_node.valeur:
                if current_node.check_for_children() == "droit":
                    current_node = current_node.fils_droit
                else:
                    index = current_node.id
            else:
                index = self.racine.id
        
    
    def afficher(self):
        print("Arbre")
    
    def number_of_nodes(self):
        pass