import os
import shutil
import sys
from pathlib import Path


APP_NAME = "AlgebraLab"


def resource_path(relative_path: str) -> Path:
    """Chemin d'une ressource incluse par PyInstaller."""

    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parents[2]

    return base_path / relative_path


def get_user_data_dir() -> Path:
    """Dossier permanent et modifiable de l'application."""

    if sys.platform == "win32":
        base_dir = Path(
            os.getenv("LOCALAPPDATA", Path.home() / "AppData" / "Local")
        )
    else:
        base_dir = Path.home() / ".local" / "share"

    app_dir = base_dir / APP_NAME
    app_dir.mkdir(parents=True, exist_ok=True)

    return app_dir


def get_database_path() -> Path:
    """Retourne la base utilisateur, en la créant au premier lancement."""

    user_database = get_user_data_dir() / "algebralab.db"

    if not user_database.exists():
        bundled_database = resource_path("data/algebralab.db")

        if not bundled_database.exists():
            raise FileNotFoundError(
                f"Base initiale introuvable : {bundled_database}"
            )

        shutil.copy2(bundled_database, user_database)

    return user_database


if getattr(sys, "frozen", False):
    DATABASE_PATH = get_database_path()
else:
    DATABASE_PATH = resource_path("data/algebralab.db")

ICON_PATH = resource_path("assets/matrice.ico")