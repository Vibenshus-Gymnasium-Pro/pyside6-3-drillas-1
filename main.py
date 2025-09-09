from __future__ import annotations

from PySide6.QtCore import Qt, QPoint, QRect, QSize, Property, Slot
from PySide6.QtGui import QPainter, QPen, QIcon
from PySide6.QtWidgets import QWidget

TOM = '-'
KRYDS = 'X'

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile("tictactoeUI.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # size n pos, x, y, w, h
        self.setGeometry(300, 170, 550, 600)

        # set window title
        self.setWindowTitle("1073139323 - TicTacToe")

        # set window icon (currently unused)
        self.setWindowIcon(QIcon("img-2025-09-09-12-26-47.png"))

        self.setCentralWidget(self.ui.centralwidget)

        # access the gridLayout from the loaded ui
        self.buttons = {}
        for row in range(self.ui.gridLayout.rowCount()):
            for col in range(self.ui.gridLayout.columnCount()):
                item = self.ui.gridLayout.itemAtPosition(row, col)
                if item:
                    container = item.widget()
                    button = container.findChild(QPushButton)
                    if button:
                        self.buttons[(row, col)] = button
                        button.clicked.connect(
                            lambda checked=False, r=row, c=col: self.on_button_clicked(r, c)
                        )

    def on_button_clicked(self, row, col):
        print(f"Button at ({row}, {col}) pressed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
