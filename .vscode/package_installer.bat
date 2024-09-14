@echo off

IF EXIST ".venv\Scripts\activate" (
    call .venv\Scripts\activate

    :: formatting and helper modules
    pip install coloredlogs

    :: math modules
    pip install matplotlib
    pip install numpy
    pip install xlwings
    pip install pandas
    pip install openpyxl
    pip install scipy

    :: computer vision and image modules
    pip install opencv-python
    pip install psd-tools
    pip install imutils

    :: documentation generation
    pip install mkdocs
    pip install mkdocstrings
    pip install mkdocstrings-crystal
    pip install mkdocstrings-python
    pip install mkdocs-print-site-plugin
    pip install mkdocs-autorefs
    pip install mkdocs-admonition
    pip install mkdocs-material

    :: extra
    pip install pyinstaller

) ELSE (
    echo .venv does not exist
)
EXIT /b