import sys
import os
from algebralab.manager.matrix_manager import MatrixManager
from algebralab.gui.main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from algebralab.config import ICON_PATH

manager = MatrixManager()

manager.charger_matrices()

def resource_path(relative_path):

    if hasattr(sys, "_MEIPASS"):
        return os.path.join(
            sys._MEIPASS,
            relative_path
        )

    return os.path.join(
        os.path.abspath("."),
        relative_path
    )
 

app = QApplication(sys.argv)

fenetre = MainWindow(manager)
fenetre.showMaximized()

fenetre.setWindowIcon(
    QIcon(resource_path(ICON_PATH))
)

fenetre.show()

app.exec()