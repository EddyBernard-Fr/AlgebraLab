import sqlite3
import json
from algebralab.algebra.matrix import Matrix

from algebralab.config import DATABASE_PATH

connexion = sqlite3.connect(DATABASE_PATH)

curseur = connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS matrices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE,
    lignes INTEGER,
    colonnes INTEGER,
    valeurs TEXT
)
""")

connexion.commit()
connexion.close()



def ajouter_matrice(matrice):
    
    connexion = sqlite3.connect(DATABASE_PATH)
    curseur = connexion.cursor()
    
    valeurs_json = json.dumps(matrice.values)
    curseur.execute(
        """
        INSERT INTO matrices
        (nom, lignes, colonnes, valeurs)
        VALUES (?, ?, ?, ?)
        """,
        (
            matrice.name,
            matrice.lignes,
            matrice.colonnes,
            valeurs_json
        )
    )
    connexion.commit()
    connexion.close()


def charger_matrice(nom):

     with sqlite3.connect(DATABASE_PATH) as connexion:

        curseur = connexion.cursor()

        curseur.execute(
            """
            SELECT *
            FROM matrices
            WHERE nom = ?
            """,
            (nom,)
        )

        ligne = curseur.fetchone()

        if ligne is None:
            return None

        matrice = Matrix()

        matrice.name = ligne[1]
        matrice.lignes = ligne[2]
        matrice.colonnes = ligne[3]
        matrice.values = json.loads(ligne[4])

        return matrice

def charger_toute_matrice():

     
     with sqlite3.connect(DATABASE_PATH) as connexion:

        curseur = connexion.cursor()

        curseur.execute(
            """
            SELECT *
            FROM matrices
            """     
        )

        lignes = curseur.fetchall()

        if lignes is None:
            return None

        

        return lignes


def supp_matrice(cle):

    with sqlite3.connect(DATABASE_PATH) as connexion:

        curseur = connexion.cursor()
        
        curseur.execute(
            "DELETE FROM matrices WHERE nom = ?",
            (cle,)
            )
        connexion.commit()


def update_matrice(cle, valeurs):

    with sqlite3.connect(DATABASE_PATH) as connexion:

        curseur = connexion.cursor()
        valeurs_json = json.dumps(valeurs)
        
        curseur.execute(
            "UPDATE matrices SET valeurs = ? WHERE nom = ?",
            (valeurs_json,cle)
            )
        connexion.commit()
