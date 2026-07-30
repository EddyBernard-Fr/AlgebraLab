from algebralab.algebra.matrix import Matrix

def choix_matrice(matrices):

    print("\n===== Matrices disponibles =====")
                
    i=0         
    for cle in matrices:
        print(f"{i+1} - {cle}")
        i=i+1
        
    print("0 - Retour")

    numero1 = -1
    while numero1 > len(matrices) or numero1 < 1 :
        if numero1 == 0:
            return "retour"
        else:
            try:
                numero1 = int(input("Numéro de la matrice selectionnée: "))
        
            except ValueError:
                print("Seulement des entiers sont possibles")
                numero1 = int(input("Numéro de la matrice selectionnée: "))
            
    cle1 = list(matrices.keys())[numero1-1]
    return cle1


def objet_matrice(nom, lignes, colonnes, valeurs):

    matrice = Matrix()
    matrice.name = nom
    matrice.lignes = lignes
    matrice.colonnes = colonnes
    matrice.values = valeurs

    return matrice