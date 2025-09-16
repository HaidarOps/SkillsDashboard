# Objective - To build a dashboard which monitors skills that i have learnt
# LO:
#  - Build a dashboard
#  - Allow the user to add skills
#  - Display skills and different Objective



import sys

from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog, QLabel,QGridLayout)
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QIcon,  QPixmap

class  Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        # self.edit = QLineEdit("Write your name here... ")
        # self.button = QPushButton("Show greetings")
        self.icon_label = QLabel()
        self.icon_label.setPixmap(QPixmap("./assets/book.png"))
        self.icon_label.setFixedSize(64, 64)
        self.icon_label.setScaledContents(True)
        self.label_quote = QLabel("There are a thousand paths up the mountain...")
        self.grid_layout = QGridLayout()


        # changing the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.icon_label, alignment = Qt.AlignCenter)
        layout.addWidget(self.label_quote)
        layout.setSpacing(50)
        layout.addWidgetQGridLayout())
        # layout.addWidget(self.edit)
        # layout.addWidget(self.button)


        self.setLayout(layout)
        # self.button.clicked.connect(self.greetings)

        self.setWindowIcon(QIcon("./assets/book.png"))

    def greetings(self):
        print(f"Hello {self.edit.text()}")




#This will skip everything inside if the file is not directly called and not import
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())

