import sys
from PyQt5.QtWidgets import QApplication, QWidget, QApplication, QWidget, QLineEdit, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QPalette, QLinearGradient, QColor

# Crear una aplicación de PyQt
app = QApplication(sys.argv)

# Crear una ventana principal
window = QWidget()
window.setWindowTitle("Mi Ventana")
window.setGeometry(100, 100, 400, 300)  # Establecer la posición y el tamaño de la ventana



# Crear un degradado lineal
gradient = QLinearGradient(0, 0, window.width(), window.height())
gradient.setColorAt(0, QColor(255, 255, 255))
gradient.setColorAt(1, QColor(150, 150, 150))

# Crear una paleta de colores y asignar el degradado como fondo
palette = window.palette()
palette.setBrush(QPalette.Window, gradient)
window.setPalette(palette)

# Crear un layout vertical
layout = QVBoxLayout(window)

# Crear un campo de texto centrado horizontalmente
text_field = QLineEdit()
#text_field.setAlignment(Qt.AlignCenter)  # Centrar el texto horizontalmente

text_field.setStyleSheet("""
    QLineEdit {
        width: 100px;
        border-style: solid;
        border-width: 2px;
        border-color: transparent transparent #777 transparent;
        border-radius: 10px 10px 0px 0px;
        padding: 5px;
        background-color: transparent;
    }
""")

layout.addWidget(text_field)

# Configurar la política de tamaño del campo de texto
text_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

window.setLayout(layout)

# Mostrar la ventana
window.show()

# Iniciar el bucle de eventos de la aplicación
sys.exit(app.exec_())