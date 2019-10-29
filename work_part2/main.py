import sys
sys.path.append("..")

from mainwindow import Window
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    width, height = 1000, 1000
    app = QApplication(sys.argv)
    window = Window(width, height)
    print ("Main")
    window.show()
    sys.exit(app.exec_())