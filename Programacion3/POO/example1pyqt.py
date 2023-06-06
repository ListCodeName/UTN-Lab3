"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

app = QApplication(sys.argv)

# Crear una ventana principal
window = QWidget()
window.setWindowTitle("Mi Ventana")
window.setGeometry(100, 100, 400, 300)

# Crear un layout vertical
layout = QVBoxLayout(window)

# Crear elementos de ejemplo
label1 = QLabel("Etiqueta 1")
label2 = QLabel("Etiqueta 2")
button1 = QPushButton("Botón 1")
button2 = QPushButton("Botón 2")

# Agregar los elementos al layout
layout.addWidget(label1)
layout.addWidget(label2)

# Crear un layout horizontal para los botones
button_layout = QHBoxLayout()
button_layout.addWidget(button1)
button_layout.addWidget(button2)

# Agregar el layout horizontal al layout vertical
layout.addLayout(button_layout)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())


"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QButtonGroup

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Ventana")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout(self)

        # Crear un grupo de botones
        button_group = QButtonGroup()

        # Crear los RadioButtons y agregarlos al layout y al grupo
        square_button = QRadioButton("Cuadrado")
        layout.addWidget(square_button)
        button_group.addButton(square_button)

        circle_button = QRadioButton("Círculo")
        layout.addWidget(circle_button)
        button_group.addButton(circle_button)

        # Conectar la señal de cambio de selección
        square_button.clicked.connect(lambda : self.mostrar_seleccion(square_button))
        circle_button.clicked.connect(lambda : self.mostrar_seleccion(circle_button))

        #button_group.buttonClicked.connect(self.mostrar_seleccion())

    def mostrar_seleccion(self, button):
        print("Opción seleccionada:", button.text())

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QDialog, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt

class ShapeDialog(QDialog):
    def __init__(self, shape):
        super().__init__()
        self.setWindowTitle("Figura")
        self.setGeometry(200, 200, 200, 200)
        self.shape = shape

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(Qt.black, 2)
        painter.setPen(pen)

        if self.shape == "Cuadrado":
            brush = QBrush(Qt.red)
            painter.setBrush(brush)
            painter.drawRect(50, 50, 100, 100)
        elif self.shape == "Círculo":
            brush = QBrush(Qt.blue)
            painter.setBrush(brush)
            painter.drawEllipse(50, 50, 100, 100)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Ventana")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout(self)

        # Crear un grupo de botones
        button_group = QButtonGroup()

        # Crear los RadioButtons y agregarlos al layout y al grupo
        square_button = QRadioButton("Cuadrado")
        layout.addWidget(square_button)
        button_group.addButton(square_button)

        circle_button = QRadioButton("Círculo")
        layout.addWidget(circle_button)
        button_group.addButton(circle_button)

        # Conectar la señal de cambio de selección de los RadioButtons individuales
        square_button.clicked.connect(lambda: self.mostrar_seleccion(square_button))
        circle_button.clicked.connect(lambda: self.mostrar_seleccion(circle_button))

    def mostrar_seleccion(self, button):
        shape = button.text()

        shape_dialog = ShapeDialog(shape)
        shape_dialog.exec_()

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
