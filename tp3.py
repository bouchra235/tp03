class ObjetSac: 
    def __init__(self, poids, valeur, indice): 
        self.indice = indice         
        self.poids = poids 
        self.valeur = valeur
        self.rapport = valeur // poids 
  #Fonction pour la comparaison entre deux ObjetSac
  #On compare le rapport calculé pour les trier
    def __lt__(self, other): 
        return self.rapport < other.rapport 
  
def getValeurMax(poids, valeurs, capacite): 
        tableauTrie = [] 
        for i in range(len(poids)): 
            tableauTrie.append(ObjetSac(poids[i], valeurs[i], i)) 
  
        #Trier les éléments du sac par leur rapport
        tableauTrie.sort(reverse = True) 
  
        compteurValeur = 0
        for objet in tableauTrie: 
            poidsCourant = int(objet.poids) 
            valeurCourante = int(objet.valeur) 
            if capacite - poidsCourant >= 0: 
                #on ajoute l'objet dans le sac
                #On soustrait la capacité
                capacite -= poidsCourant 
                compteurValeur += valeurCourante
                #On ajoute la valeur dans le sac 
            else: 
                fraction = capacite / poidsCourant 
                compteurValeur += valeurCourante * fraction 
                capacite = int(capacite - (poidsCourant * fraction)) 
                break
        return compteurValeur 
poids = [1,5,3,2,4] 
valeurs = [10,50,20,30,60] 
capacite = 11
valeurMax = getValeurMax(poids, valeurs, capacite) 
print("Valeur maxi dans le sac à dos =", valeurMax)
