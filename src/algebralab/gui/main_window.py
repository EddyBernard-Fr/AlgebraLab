from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QApplication
)

from algebralab.gui.create_matrix_window import *
from algebralab.gui.delete_matrix_page import *
from algebralab.gui.import_matrix_page import *
from algebralab.gui.accueil_page import *


class MainWindow(QMainWindow):

    def __init__(self, manager):
        super().__init__()

        # Paramètres de la fenêtre
        self.setWindowTitle("AlgebraLab")
        
        self.manager = manager

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        # Widgets
        
        self.menu = QHBoxLayout()
        self.bouton_accueil = QPushButton("Matrix Calculator")
        
        # menu fixe
        
        self.menu.addWidget(self.bouton_accueil)
        self.layout.addLayout(self.menu)

        # zone qui change

        self.page = QWidget()
        self.layout.addWidget(self.page)
        self.page_accueil()


        self.bouton_accueil.clicked.connect(
            self.page_accueil
        )
   

    def changer_page(self, nouvelle_page):

        self.layout.removeWidget(self.page)

        self.page.deleteLater()

        self.page = nouvelle_page

        self.layout.addWidget(self.page)

    def page_creation_matrice(self):

        page = CreateMatrixPage(
            self.manager,
            self
        )

        self.changer_page(page)
    
    def page_import_matrice(self):

        page = ImportMatrixPage(self.manager, self)

        self.changer_page(page)

    
    def page_accueil(self):

        page = AccueilPage(self.manager, self)

        self.changer_page(page)