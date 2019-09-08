import random
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_Dialog, self).__init__(parent)
         

        self.setMinimumSize(750, 500)
        lay = QtWidgets.QHBoxLayout(self)
        

 
        
        for letter in "ABCDEFG":
            label = QtWidgets.QLabel(letter, alignment=QtCore.Qt.AlignCenter)
            color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
            label.setStyleSheet("background-color: {}".format(color.name()))
            lay.addWidget(label)



if __name__ == "__main__":
    import sys 

    app = QtWidgets.QApplication(sys.argv) 
    ui = Ui_Dialog() 
    ui.resize(719, 478)
    ui.show()
    sys.exit(app.exec_()) 



 
