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
    
)

from algebralab.manager.utils import *
from algebralab.manager.matrix_manager import *

        

         
class DeleteMatrixPage(QWidget):

    def __init__(self, manager, main_window):
        super().__init__()

        self.manager = manager
        self.main_window = main_window
        self.layout = QVBoxLayout()

        self.label = QLabel("Choisir une matrice à supprimer")

        self.liste = QListWidget()

        self.bouton_supprimer = QPushButton("Supprimer")


        self.layout.addWidget(self.label)
        self.layout.addWidget(self.liste)
        self.layout.addWidget(self.bouton_supprimer)

        self.setLayout(self.layout)


        self.charger_liste()


        self.bouton_supprimer.clicked.connect(
            self.supprimer
        )

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