import numpy as np
from algebralab.manager.utils import choix_matrice, objet_matrice
from algebralab.database.database import ajouter_matrice


def addition_matrice(matrices):

    cle = [0 , 0]
    Matrice = [0, 0]
    for i in range(2):

        while True:

            cle[i] = choix_matrice(matrices)
            if cle[i] != "retour":
                print(matrices[cle[i]])
                Matrice[i] = np.array(matrices[cle[i]].values)
                break
            else:
                break
    

    R = Matrice[0] + Matrice[1]

    if hasattr(R, "tolist"):
        valeurs = R.tolist()


    matrices[f"{cle[0]} + {cle[1]}"] = objet_matrice(f"{cle[0]} + {cle[1]}", matrices[cle[0]].lignes, matrices[cle[0]].colonnes, valeurs)
    print(matrices[f"{cle[0]} + {cle[1]}"])
    
    
    ajouter_matrice(matrices[f"{cle[0]} + {cle[1]}"])

def multiplication_matrice(matrices):

    cle = [0 , 0]
    Matrice = [0, 0]
    for i in range(2):

        while True:

            cle[i] = choix_matrice(matrices)
            if cle[i] != "retour":
                print(matrices[cle[i]])
                Matrice[i] = np.array(matrices[cle[i]].values)
                break
            else:
                break
    

    R = np.dot(Matrice[0],Matrice[1])
    

    if hasattr(R, "tolist"):
        valeurs = R.tolist()


    matrices[f"{cle[0]} x {cle[1]}"] = objet_matrice(f"{cle[0]} x {cle[1]}", matrices[cle[0]].lignes, matrices[cle[1]].colonnes, valeurs)
    print(matrices[f"{cle[0]} x {cle[1]}"])
    
    
    ajouter_matrice(matrices[f"{cle[0]} x {cle[1]}"])