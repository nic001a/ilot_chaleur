from PyQt5.QtWidgets import QWidget, QApplication

application = QApplication([])

mainWindow = QWidget()

mainWindow.setGeometry(0, 0, 350, 400)
mainWindow.setWindowTitle('Hello World')

mainWindow.show()

application.exec()