import sys
sys.path.append("..")

from mainwindow import Window
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    width, height = 800, 600
    app = QApplication(sys.argv)
    window = Window(width, height)
    print ("\n##################################################################\n\t\t\tEQUIPE 01:\n\n>>> Executando Projeto OpenGL... Por favor, aguarde a renderização.\n\n##################################################################")
    window.show()
    sys.exit(app.exec_())