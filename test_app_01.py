import random
from PyQt5 import QtCore, QtGui, QtWidgets
from tinydb import TinyDB, Query
import json



MIN_WIDTH = 750
MIN_HEIGHT = 500
APP_NAME = "Work"
DB_PATH = "./data/db"










#  for drag event component 
class DropComponent(QtWidgets.QLabel): 
    def __init__(self, type, supera, parent=None):
        super(DropComponent, self).__init__(parent)
        self.super = supera 

        color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
        self.setStyleSheet("background-color: {}".format(color.name()))
 
        self.setMinimumSize(10, 10)
        self.setGeometry(QtCore.QRect( 0, 0, 20, 20))

        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):

        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.super( links )
        else:
            event.ignore()



# main widget class 
class Ui_Dialog(QtWidgets.QWidget):
    # constructor that actually reads current this as patent componet this
    def __init__(self, suself, parent=None):
        super(Ui_Dialog, self).__init__(parent)
         
        #  set current comonet super as parent scope/ this
        self.super = suself

        # set the minimum with and height
        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)
        # set widget name
        self.setWindowTitle( APP_NAME )
 

        # create the vertical box to the widget
        lay = QtWidgets.QGridLayout(self) 

        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("top_menu") 
        self.widget.setMaximumSize(QtCore.QSize(16777215, 30))

        self.menuItemsContainer = QtWidgets.QWidget(self.widget)
        self.menuItemsContainer.setObjectName("menu_items")

        
        
        self.menuItems = QtWidgets.QHBoxLayout(self.menuItemsContainer)
        self.menuItems.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.menuItems.setContentsMargins(0, 0, 0, 0)
        self.menuItems.setObjectName("menuItems")
        
        #  button ===================== 01
        self.pushButton01 = QtWidgets.QPushButton(self.menuItemsContainer)
        self.pushButton01.setObjectName("pushButton01")
        self.pushButton01.setMaximumSize(70, 25)
        self.pushButton01.setText("add one ") 
        self.pushButton01.clicked.connect(self.event_clicked_button01) 
        self.menuItems.addWidget(self.pushButton01)
        # ======================================================== end 01
 
        
 
        # setting menu items arrange ===> margin-right auto adjest
        self.qLabel = QtWidgets.QLabel(self.menuItemsContainer)
        self.qLabel.setObjectName("res_event")
        self.menuItems.addWidget(self.qLabel)



 
 
        lay.addWidget( self.widget )


        




        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setObjectName("widget_2")
        self.mainContentTab = QtWidgets.QTabWidget(self.widget_2)

        self.mainContentTab.setObjectName("mainContentTab")
        self.tab01 = QtWidgets.QWidget()
        self.tab01.setObjectName("tab01")
        
        self.inActionTab01 = QtWidgets.QWidget(self.tab01)
        self.inActionTab01.setObjectName("inActionTab01")

        self.inTab01Layout = QtWidgets.QHBoxLayout(self.inActionTab01)
        self.inTab01Layout.setContentsMargins(0, 0, 0, 0)
        self.inTab01Layout.setObjectName("inTab01Layout")


        self.inside_01 = QtWidgets.QWidget(self.inActionTab01)
        self.inside_01.setObjectName("inside_01") 

        self.inTab01Layout.addWidget(self.inside_01)


        self.dropZone = DropComponent( self.inside_01, self.pictureDropped )

        self.inTab01LayoutIn = QtWidgets.QHBoxLayout(self.inside_01)
        self.inTab01LayoutIn.setContentsMargins(0, 0, 0, 0)
        self.inTab01LayoutIn.setObjectName("inTab01LayoutIn")
        
        # self.connect(self.dropZone, QtCore.SIGNAL("dropped"), self.pictureDropped)
        self.inTab01LayoutIn.addWidget(self.dropZone)


        self.inside_02 = QtWidgets.QWidget(self.inActionTab01)
        self.inside_02.setObjectName("inside_02")
        self.inTab01Layout.addWidget(self.inside_02)



        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.inside_02)
        self.plainTextEdit.setObjectName("outputArea") 
        self.plainTextEdit.setPlainText("plainTextEdit") 
        self.plainTextEdit.setReadOnly(True)
        
        



        self.mainContentTab.addTab(self.tab01, "action 1")


        self.tab02 = QtWidgets.QWidget()
        self.tab02.setObjectName("tab02")
        self.mainContentTab.addTab(self.tab02, "action 2")
 
        
        lay.addWidget(self.widget_2 )





        # color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
        # self.menuItemsContainer.setStyleSheet("background-color: {}".format(color.name()))

    def pictureDropped(self, l):
        print(l)

 
    # trigger when window size is changed, updateing all responsive widgets 
    def responsive_init( self, event ) :  

        self.menuItemsContainer.setGeometry(QtCore.QRect(0, 0, self.widget.width(), 31)) 
        self.mainContentTab.setGeometry(QtCore.QRect( 0, 0, self.widget_2.width(), self.widget_2.height()))
        self.inActionTab01.setGeometry(QtCore.QRect( 0, 0,  self.widget_2.width(), self.widget_2.height()  ))
        
        self.inTab01Layout.setGeometry(QtCore.QRect( 0, 0,  self.inActionTab01.width(), self.inActionTab01.height()  ))
        self.plainTextEdit.setGeometry(QtCore.QRect( 0, -1,  self.inside_02.width(), self.inside_02.height()  ))
        



#  system events

    def closeEvent(self,event):
        self.super.on_dialog_close()
        print('closed')

    def resizeEvent(self, event):
        self.responsive_init(event)








    def event_clicked_button01(self):
        print('Button pressed')
        # self.pushButton01.setEnabled(False)

        

class Main:
    def __init__( self ): 
        # set up database 
        self.set_up_db()



        # for widget component 
        app = QtWidgets.QApplication(sys.argv) 
        # assign ui compone to class variable, actual object created and passes this to child class
        self.ui = Ui_Dialog( self )  
        # get system screen to calculate center , etc.
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        
        # class function to get widget location width and height
        self.update_geometry()
    
        #  show the widget
        self.ui.show()

        # update component last widget postion, width and height // initial setup
        self.set_location_()



        # system exit
        sys.exit(app.exec_()) 



    # move widget to last postion 
    def set_location_ (self):
        Settings = Query()
        db = self.db


        try:
            tmpdata = db.search((Settings.key == "location")) 
            data = json.loads(tmpdata[0]["data"]) 
            self.ui.setGeometry(data["x"], data["y"], data["w"], data["h"]) 
        except Exception as e: 
            self.set_center()

        


            
    # set widget location and size details to this object
    def update_geometry(self):
        self.dialog = self.ui.geometry()
        

    # execute when widget trigger a close event > triggered from child componet 
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


    #  preporcessing the db 
    def set_up_db ( self ):
        try:  
            if not(os.path.exists( DB_PATH ) ):
                os.makedirs(DB_PATH) 
        except  : 
            pass

        self.db = TinyDB(DB_PATH + '/db.json')

        
    #  function that position the widget to the center of the screen
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

# main function trigger main class 
if __name__ == "__main__":
    import sys 
    import os

    main = Main()
    



 
