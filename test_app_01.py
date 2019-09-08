import random
from PyQt5 import QtCore, QtGui, QtWidgets
from tinydb import TinyDB, Query
import json



MIN_WIDTH = 750
MIN_HEIGHT = 500
APP_NAME = "Work"
DB_PATH = "./data/db"

class Ui_Dialog(QtWidgets.QWidget):
    def __init__(self, suself, parent=None):
        super(Ui_Dialog, self).__init__(parent)
         
        self.super = suself

        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)
        self.setWindowTitle( APP_NAME )

        lay = QtWidgets.QHBoxLayout(self)
        

 
        
        for letter in "ABCDEFG":
            label = QtWidgets.QLabel(letter, alignment=QtCore.Qt.AlignCenter)
            color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
            label.setStyleSheet("background-color: {}".format(color.name()))
            lay.addWidget(label)

 

    def closeEvent(self,event):
        self.super.on_dialog_close()
        print('closed')






class Main:
    def __init__( self ):

        

        self.set_up_db()



        
        app = QtWidgets.QApplication(sys.argv) 
        self.ui = Ui_Dialog( self )  
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        
        self.update_geometry()
 
        self.ui.show()

        self.set_location_()




        sys.exit(app.exec_()) 



    def set_location_ (self):
        Settings = Query()
        db = self.db


        try:
            tmpdata = db.search((Settings.key == "location")) 
            data = json.loads(tmpdata[0]["data"]) 
            self.ui.setGeometry(data["x"], data["y"], data["w"], data["h"]) 
        except Exception as e: 
            self.set_center()

        


            

    def update_geometry(self):
        self.dialog = self.ui.geometry()
        

    def on_dialog_close (self):
        Settings = Query()
        self.update_geometry()
        
        dialog = self.dialog  
        json_string = json.dumps( { 
            "x": dialog.x(), 
            "y": dialog.y(), 
            "w" : dialog.width(), 
            "h": dialog.height()
            } )


        try:
            tmpdata = self.db.search((Settings.key == "location"))  
            if len(tmpdata) < 1 :
                self.db.insert( { "key" : "location",  "data": json_string }) 
        except : 
            self.db.insert( { "key" : "location",  "data": json_string }) 


        self.db.update({ "data": json_string }, Settings.key.search("location"))



    def set_up_db ( self ):
        try:  
            if not(os.path.exists( DB_PATH ) ):
                os.makedirs(DB_PATH) 
        except  : 
            pass

        self.db = TinyDB(DB_PATH + '/db.json')

        


    def set_center ( self ): 
        screen = self.screen
        dialog = self.dialog

        s_width = screen.width()
        s_height = screen.height()

        w_width = dialog.width()
        w_height = dialog.height()

        x = s_width / 2  - w_width / 2
        y = s_height / 2  - w_height / 2

        x = min( max( x, 0 ), s_width - w_width )
        y = min( max( y, 0 ),s_width - 20 ) 
        self.ui.move(x, y)


if __name__ == "__main__":
    import sys 
    import os

    main = Main()
    



 
