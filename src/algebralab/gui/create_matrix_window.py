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
    QTableWidgetItem
)

from PySide6.QtCore import Qt
from algebralab.manager.utils import *
from algebralab.manager.matrix_manager import *



class CreateMatrixPage(QWidget):

    def __init__(self, manager, main_window):
        super().__init__()

        # Paramètres de la fenêtre
        
        self.name = ""
        self.lignes = 0
        self.colonnes = 0
        self.manager = manager
        self.main_window = main_window

        # Widget central
       

        # Widgets
        self.nom_label = QLabel("Nom :")
        self.nom_input = QLineEdit()
        self.lignes_label = QLabel("Lignes :")
        self.lignes_input = QSpinBox()
        self.colonnes_label = QLabel("Colonnes :")
        self.colonnes_input = QSpinBox()
        self.bouton_creer = QPushButton("Créer grille") 
        
        self.lignes_input.setMinimum(1)
        self.colonnes_input.setMinimum(1)

        self.lignes_input.setValue(3)
        self.colonnes_input.setValue(3)
        self.bouton_creer.setFixedHeight(40)
        self.nom_input.setMinimumWidth(150)
        self.table = QTableWidget()
        self.bouton_save = None
        self.parenthese_gauche = QLabel("(")
        self.parenthese_droite = QLabel(")")

        self.parenthese_gauche.setAlignment(Qt.AlignCenter)
        self.parenthese_droite.setAlignment(Qt.AlignCenter)

        self.parenthese_gauche.hide()
        self.parenthese_droite.hide()
        self.table.hide()

       

        # Layout
        self.layout = QVBoxLayout()
        self.layout.setSpacing(15)

        self.form_layout = QGridLayout()
        self.form_layout.setColumnMinimumWidth(0, 80)
        self.form_layout.setColumnStretch(0, 0)
        self.form_layout.setColumnStretch(1, 1)

        self.form_layout.addWidget(self.nom_label, 0, 0)
        self.form_layout.addWidget(self.nom_input,0,1,alignment=Qt.AlignLeft)

        self.form_layout.addWidget(self.lignes_label, 1, 0)
        self.form_layout.addWidget(self.lignes_input, 1, 1, alignment=Qt.AlignLeft)


        self.form_layout.addWidget(self.colonnes_label, 2, 0)
        self.form_layout.addWidget(self.colonnes_input, 2, 1, alignment=Qt.AlignLeft)

        self.layout.addLayout(self.form_layout)

        self.bouton_layout = QHBoxLayout()

        self.bouton_layout.addStretch()
        self.bouton_layout.addWidget(self.bouton_creer)
        self.bouton_layout.addStretch()

        self.layout.addLayout(self.bouton_layout)


        self.table_layout = QHBoxLayout()
        
        self.table_layout.addStretch()
        self.table_layout.addWidget(self.parenthese_gauche, alignment=Qt.AlignVCenter)
        self.table_layout.addWidget(self.table, alignment=Qt.AlignVCenter)
        self.table_layout.addWidget(self.parenthese_droite, alignment=Qt.AlignVCenter)
        self.table_layout.addStretch()


        self.layout.addLayout(self.table_layout)

        self.save_layout = QHBoxLayout()

        self.bouton_save = QPushButton("Sauvegarder")  
        self.bouton_save.hide()

        self.save_layout.addStretch()
        self.save_layout.addWidget(self.bouton_save)
        self.save_layout.addStretch()
        
        self.layout.addLayout(self.save_layout)
        self.layout.addStretch()
        self.setLayout(self.layout)
        

        # Connexions
        self.bouton_creer.clicked.connect(self.creer_grille)
        self.bouton_save.clicked.connect(self.sauvegarder_grille)
        

    def sauvegarder_grille(self):

        nom = self.nom_input.text()

        lignes = self.lignes_input.value()
        colonnes = self.colonnes_input.value()

        valeurs = []

        for i in range(lignes):

            ligne = []

            for j in range(colonnes):

                item = self.table.item(i, j)

                if item is None:
                    ligne.append(0)

                else:
                    ligne.append(float(item.text()))

            valeurs.append(ligne)

        print(nom)
        print(valeurs)
        matrice = objet_matrice(nom, lignes, colonnes, valeurs)
        self.manager.ajouter_matrice_dict(matrice)
        self.manager.save_matrice_bdd(matrice)



    def creer_grille(self):
        nom = self.nom_input.text()
        lignes = self.lignes_input.value()
        colonnes = self.colonnes_input.value()

        self.table.setRowCount(lignes)
        self.table.setColumnCount(colonnes)
        self.table.setShowGrid(False)
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.table.setFixedSize(
            colonnes * 50,
            lignes * 50
        )

        taille_parenthese = self.table.height()

        for p in [self.parenthese_gauche, self.parenthese_droite]:
            p.setStyleSheet(
             f"font-size: {taille_parenthese}px;"
            )
            p.setFixedHeight(taille_parenthese)
            p.setAlignment(Qt.AlignCenter)

        decalage = -(lignes * 15)
        self.parenthese_gauche.setContentsMargins(0, decalage, 0, 0)
        self.parenthese_droite.setContentsMargins(0, decalage, 0, 0)

        for i in range(lignes):
            for j in range(colonnes):
                item = QTableWidgetItem("0")
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(i,j,item)
        
        for i in range(colonnes):
            self.table.setColumnWidth(i, 48)

        for i in range(lignes):
            self.table.setRowHeight(i, 48)
        
        self.parenthese_gauche.show()
        self.table.show()
        self.parenthese_droite.show()
        self.bouton_save.setFixedHeight(40)
        self.bouton_save.show()


        
 
    


        

         
