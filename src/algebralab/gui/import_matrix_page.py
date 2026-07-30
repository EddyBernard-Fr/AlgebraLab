from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QApplication,
    QTableWidget,
    QSpinBox,
    QLineEdit,
    QLabel,
    QHBoxLayout,
    QGridLayout,
    QFileDialog,  
    QMessageBox
)


from algebralab.manager.utils import *
from algebralab.manager.matrix_manager import *
import os

        

         
class ImportMatrixPage(QWidget):

    def __init__(self, manager, main_window):
        super().__init__()

        self.manager = manager
        self.main_window = main_window
        self.layout = QVBoxLayout()

        self.form_layout = QVBoxLayout()

        

        self.bouton_layout = QHBoxLayout()

        self.label = QLabel("Importer une matrice:")

        self.bouton_import = QPushButton("Importer")

        self.bouton_layout.addWidget(self.label)
        self.bouton_layout.addWidget(self.bouton_import)
        self.bouton_layout.addStretch()
        
        
        self.form_layout.addLayout(self.bouton_layout)

        self.layout.addLayout(self.form_layout)


        self.layout.addStretch()
        self.setLayout(self.layout)

        self.bouton_import.clicked.connect(self.import_matrix)

    def charger_liste(self):

        self.liste.clear()

        for matrice in self.manager.get_matrices():

            self.liste.addItem(
                matrice.name
            )

    def supprimer(self):

        item = self.liste.currentItem()

        if item is None:
            return

        nom = item.text()

        self.manager.supprimer_matrice_bdd(nom)

        self.charger_liste()

    def import_matrix(self):
        
        fichier, _ = QFileDialog.getOpenFileName(
            self,
            "Choisir un fichier",
            "",
            "Fichiers texte (*.txt)"
        )

        if fichier:
            with open(fichier, "r") as f:
                lignes = f.readlines()

            valeurs = []

            for ligne in lignes:
                ligne = ligne.strip()

                if "," in ligne:
                    elements = ligne.split(",")
                else:
                    elements = ligne.split()

                valeurs.append(
                    [float(x) for x in elements]
                )

            nom = os.path.splitext(
                os.path.basename(fichier)
            )[0]

            lignes = len(valeurs)
            colonnes = len(valeurs[0])

            for ligne in valeurs:

                if len(ligne) != colonnes:
                    QMessageBox.warning(
                        self,
                        "Erreur d'import",
                        "Toutes les lignes doivent avoir le même nombre de colonnes."
                    )
                    return

            matrice = objet_matrice(
                nom,
                lignes,
                colonnes,
                valeurs
            )
            self.manager.ajouter_matrice_dict(matrice)
            self.manager.save_matrice_bdd(matrice)

            
            