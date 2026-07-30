import json
from algebralab.database.database import ajouter_matrice, supp_matrice, charger_toute_matrice, update_matrice
from algebralab.manager.utils import objet_matrice, choix_matrice


class MatrixManager:

    def __init__(self):
        self.matrices_dict = {}

    def ajouter_matrice_dict(self, matrice):
        self.matrices_dict[matrice.name] = matrice

    def save_matrice_bdd(self, matrice):
        ajouter_matrice(matrice)


    def recuperer_matrice(self, nom):

        return self.matrices_dict.get(nom)
    
    def get_matrices(self):

        return self.matrices_dict.values()

    def supprimer_matrice_bdd(self, nom):

        if nom in self.matrices_dict:
            del self.matrices_dict[nom]

        supp_matrice(nom)
    
    def charger_matrices(self):

        all_matrix = charger_toute_matrice()

        if all_matrix is None:
            return

        for ligne in all_matrix:

            matrice = objet_matrice(
                ligne[1],
                ligne[2],
                ligne[3],
                json.loads(ligne[4])
            )

            self.matrices_dict[matrice.name] = matrice
                  

def modifier(matrices):
   

    while True:

        cle = choix_matrice(matrices)
        if cle != "retour":
        
            matrices[cle].values = []
        
            for i in range(matrices[cle].lignes):
                ligne = []

                for j in range(matrices[cle].colonnes):

                    while True:

                        try:
                            valeur = float(input(f"Valeur [{i}][{j}] : "))
                            break

                        except ValueError:
                            print("Veuillez entrer un nombre valide.")
                           
                       
                    ligne.append(valeur)

                matrices[cle].values.append(ligne)
                
    
            print(matrices[cle])

            update_matrice(cle, matrices[cle].values)

            print("Matrice sauvegardée !")
            
        else:
            break
  
  
       
        
        
def afficher_matrice(matrices):


    while True:

        cle = choix_matrice(matrices)
        if cle != "retour":
            print(matrices[cle]) 
        else:
            break
