# AlgebraLab

## Highlights

- Desktop application developed with Python and PySide6
- Matrix creation, editing, and storage
- SQLite database integration
- Matrix addition and multiplication
- Modular application architecture
- Windows executable generated with PyInstaller

AlgebraLab is a desktop application developed in Python for creating, storing, and manipulating matrices through a graphical user interface.

The main objective of this project is to provide a simple and intuitive interface for working with matrices without requiring direct interaction with the terminal.

## Overview

The application allows users to create, import, store, retrieve, and manipulate matrices through an intuitive graphical interface.

This project mainly focuses on:

- GUI development using PySide6
- Software architecture and modular design
- User interaction and event handling
- SQLite database integration
- Separation between the graphical interface, business logic, and data access layer

## Features

AlgebraLab currently supports:

- Creating matrices from the graphical interface
- Importing matrices from files
- Storing matrices in a local SQLite database
- Displaying stored matrices
- Editing matrices
- Deleting matrices
- Matrix addition
- Matrix multiplication

## Screenshots

![AlgebraLab main window](assets/screenshots/main-window.png)

## Technologies

- Python
- PyQt
- PySide6
- SQLite
- NumPy
- PyInstaller

## Project Structure

```text
AlgebraLab/
├── assets/
├── data/
├── src/algebralab/
├── tests/
├── AlgebraLab.spec
├── README.md
└── requirements.txt
```

- `gui/` – Graphical user interface components and application windows.
- `manager/` – Communication layer between the GUI and the application logic.
- `algebra/` – Matrix operations implementation.
- `database/` – SQLite database access layer.
- `config.py` – Centralized application configuration.
- `assets/` – Icons and graphical resources.
- `data/` – Local SQLite database.

## Download

The latest Windows executable is available on the project's
[Releases](../../releases/latest) page.

Windows SmartScreen may display a warning because the executable is not digitally signed.

Select **More info**, then **Run anyway**.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/EddyBernard-Fr/AlgebraLab.git
cd AlgebraLab
```

### 2. Create a virtual environment

**Windows**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

## Running from the Source Code

From the project root directory, under PowerShell:

```powershell
$env:PYTHONPATH="src"
python -m algebralab.main
```

Under Linux or macOS:

```bash
PYTHONPATH=src python -m algebralab.main
```

## Building the Windows Executable

PyInstaller is used to generate a standalone Windows executable.

Install PyInstaller if necessary:

```bash
python -m pip install pyinstaller
```

Then build the application from the project root:

```bash
pyinstaller --clean AlgebraLab.spec
```

The executable is generated in:

```text
dist/AlgebraLab.exe
```

The `build/` and `dist/` directories are automatically generated and are not tracked by Git.

## Database

Matrices are stored locally in a SQLite database.

No external database server is required.

When running the packaged executable, AlgebraLab stores user data in:

```text
%LOCALAPPDATA%\AlgebraLab
```

When running the project from the source code, the development database is located in the project's `data/` directory.

## Educational Objectives

This project was mainly developed to deepen my understanding of:

- Desktop GUI development in Python
- Event-driven programming
- Modular software architecture
- SQLite database management
- Executable generation with PyInstaller

## Future Improvements

Possible future enhancements include:

- Additional matrix operations
- Improved input validation
- Automated testing
- Better error handling
- Automated executable generation
- Continuous delivery through GitHub Releases

## Author

**Eddy Bernard**

PhD in Mathematics & Theoretical Chemistry

GitHub: https://github.com/EddyBernard-Fr

This repository is part of my scientific computing portfolio.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.