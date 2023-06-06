import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QLinearGradient, QColor

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Ventana")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout(self)
        
        label1 = QLabel("Valor: ")
        layout.addWidget(label1)
        
        self.textField1 = QLineEdit()
        layout.addWidget(self.textField1)

        label2 = QLabel("Color: ")
        layout.addWidget(label2)

        self.text_field2 = QLineEdit()
        layout.addWidget(self.text_field2)

        self.textField1.setStyleSheet("""
                    QLineEdit{
                        max-width: 200px;
                        margin: 0px;
                        color: #FAFAFA;
                        border-style: solid;
                        border-width: 2px;
                        border-color: transparent transparent #777 #777;
                        padding: 5px;
                        background-color: rgba(0,0,0,0.35);
                    }
                """)
        
        self.text_field2.setStyleSheet("""
                    QLineEdit{
                        max-width: 200px;
                        color: #FAFAFA;
                        margin: 0px;
                        border-style: solid;
                        border-width: 2px;
                        border-color: transparent transparent #777 #777;
                        padding: 5px;
                        background-color: rgba(0,0,0,0.35);
                    }
                """)

        # Crear un degradado lineal
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(255, 255, 255))
        gradient.setColorAt(1, QColor(150, 150, 150))
        

        button = QPushButton("Guardar")
        button.clicked.connect(self.guardar_contenido)
        layout.addWidget(button)

    def guardar_contenido(self):
        
        contenido1 = float(self.textField1.text())
        contenido2 = float(self.text_field2.text())
        print("Contenido 1:", contenido1)
        print("Contenido 2:", contenido2)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
