import random
from PyQt5 import QtCore, QtGui, QtWidgets
from tinydb import TinyDB, Query
import json
import ntpath
import threading
import subprocess




MIN_WIDTH = 750
MIN_HEIGHT = 500
APP_NAME = "Work"
DB_PATH = "./data/db"






#  class tab one
class Tab02(QtWidgets.QWidget):
    def __init__(self, type, parent=None):
        super(Tab02, self).__init__(parent)
        

        color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
        self.setStyleSheet("background-color: {}".format(color.name()))


 
        self.setObjectName("tab02")


 



    def responsive_init (self, super, event):
        test = 0





# file list and dir operations
class ListDirFiles () :
    def __init__( self, input ):
        
        self.fulllist = []
        self.input  = input
        self.listFiles() 
        
    def getFiles (self):
        try: 
            if isinstance( self.fulllist , list):
                return self.fulllist
            else:
                return []   
        except:
            pass

        return []


    def folderExist (self, path ) :
        try:
            return os.path.exists( path )
        except:
            return False

    def fileExist (self, path ) :
        try:
            return os.path.isfile( path )
        except:
            return False

    def listAllFiles ( self, file):
        tmplist = []
        try:

            if self.folderExist( file ):
                for root, dirs, files in os.walk( file ):
                    for file in files:
                        tmplist.append( os.path.join(root, file)  )

        except : 
            pass

        return tmplist

    def listFiles (self ):
        try:
            input  = self.input

            if os.path.isdir( input ):   
                if self.folderExist( input ): 
                    listifles = self.listAllFiles( input )
                    if len(listifles) > 0 :
                        self.fulllist.extend( listifles ) 

            elif os.path.isfile( input):  
                if self.fileExist( input ):
                    self.fulllist.append( input ) 
            else:  
                print( input + " is a special file (socket, FIFO, device file)" )
               


        except Exception as e: 
            pass 


#  class tab one
class Tab01(QtWidgets.QWidget):
    def __init__(self, type, parent=None):
        super(Tab01, self).__init__(parent)
         

        self.files_list = []

        self.setObjectName("tab01")
 
        self.inActionTab01 = QtWidgets.QWidget(self)
        self.inActionTab01.setObjectName("inActionTab01")

        self.inTab01Layout = QtWidgets.QHBoxLayout(self.inActionTab01)
        self.inTab01Layout.setContentsMargins(5, 5, 5, 5)
        self.inTab01Layout.setObjectName("inTab01Layout")


        self.inside_01 = QtWidgets.QWidget(self.inActionTab01)
        self.inside_01.setObjectName("inside_01") 

        self.inTab01Layout.addWidget(self.inside_01)


        self.dropZone = DropComponent( self.inside_01, self.pictureDropped )

        self.inTab01LayoutIn = QtWidgets.QVBoxLayout(self.inside_01)
        self.inTab01LayoutIn.setContentsMargins(0, 0, 0, 0)
        self.inTab01LayoutIn.setObjectName("inTab01LayoutIn") 
        self.inTab01LayoutIn.addWidget(self.dropZone)



        self.inside_011 = QtWidgets.QWidget(self.inActionTab01)
        self.inside_011.setObjectName("tab1_shred_div")  
        self.inside_011.setMaximumSize(QtCore.QSize(16777215, 25)) 
        self.inTab01LayoutIn.addWidget(self.inside_011)


        self.buttonConta = QtWidgets.QHBoxLayout(self.inside_011)
        self.buttonConta.setContentsMargins(0, 0, 0, 0)
        self.buttonConta.setObjectName("buttonConta")   
        # self.inside_02.addWidget(self.buttonConta)

                
        #  button ===================== 01
        self.pushButton01 = QtWidgets.QPushButton(self.inside_011)
        self.pushButton01.setObjectName("pushButton01") 
        self.pushButton01.setMaximumSize(70, 25)
        self.pushButton01.setText(" clear ") 
        self.pushButton01.clicked.connect(self.event_clicked_button01)  
        self.buttonConta.addWidget(self.pushButton01)
        # ======================================================== end 01
        
        #  button ===================== 02
        self.pushButton02 = QtWidgets.QPushButton(self.inside_011)
        self.pushButton02.setObjectName("pushButton02") 
        self.pushButton02.setMaximumSize(70, 25)
        self.pushButton02.setText(" full path ") 
        self.pushButton02.clicked.connect(self.event_clicked_button02)  
        self.buttonConta.addWidget(self.pushButton02)
        # ======================================================== end 02
 
        #  button ===================== 03
        self.pushButton03 = QtWidgets.QPushButton(self.inside_011)
        self.pushButton03.setObjectName("pushButton03") 
        self.pushButton03.setMaximumSize(70, 25)
        self.pushButton03.setText(" file name ") 
        self.pushButton03.clicked.connect(self.event_clicked_button03)  
        self.buttonConta.addWidget(self.pushButton03)
        # ======================================================== end 03
  
        #  button ===================== 04
        self.pushButton04 = QtWidgets.QPushButton(self.inside_011)
        self.pushButton04.setObjectName("pushButton04") 
        self.pushButton04.setMaximumSize(70, 25)
        self.pushButton04.setText(" is exist ") 
        self.pushButton04.clicked.connect(self.event_clicked_button04)  
        self.buttonConta.addWidget(self.pushButton04)
        # ======================================================== end 04
 
        
 
   
 
        
 
        # setting menu items arrange ===> margin-right auto adjest
        self.qLabel = QtWidgets.QLabel(self.inside_011)
        self.qLabel.setObjectName("res_event")
        self.buttonConta.addWidget(self.qLabel)





        self.inside_02 = QtWidgets.QWidget(self.inActionTab01)
        self.inside_02.setObjectName("inside_02")
        self.inTab01Layout.addWidget(self.inside_02)









        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.inside_02)
        self.plainTextEdit.setObjectName("outputArea") 
        self.plainTextEdit.setPlainText("") 
        self.plainTextEdit.setReadOnly(True)

        self.inTab02LayoutIn = QtWidgets.QVBoxLayout(self.inside_02)
        self.inTab02LayoutIn.setContentsMargins(0, 0, 0, 0)
        self.inTab02LayoutIn.setObjectName("inTab02LayoutIn") 



        self.inside_021 = QtWidgets.QWidget(self.inActionTab01)
        self.inside_021.setObjectName("tab2_shred_div")  
        self.inside_021.setMaximumSize(QtCore.QSize(16777215, 30)) 

        self.inTab02LayoutIn.addWidget(self.inside_021)

        self.inTab02LayoutIn.addWidget(self.plainTextEdit)

        self.buttonContb = QtWidgets.QHBoxLayout(self.inside_021)
        self.buttonContb.setContentsMargins(0, 0, 0, 0)
        self.buttonContb.setObjectName("buttonContb")   
        # self.inside_02.addWidget(self.buttonContb)

                 
        #  checkbox ===================== 01
        self.checkBox01 = QtWidgets.QCheckBox( self.inside_021) 
        self.checkBox01.setObjectName("pushButton11") 
        self.checkBox01.setMaximumSize(70, 25)
        self.checkBox01.setText(" Start ")  
        self.checkBox01.stateChanged.connect(self.event_clicked_checkbox11)
        self.buttonContb.addWidget(self.checkBox01)
        # ======================================================== end 01



        # setting menu items arrange ===> margin-right auto adjest
        self.qLabel2 = QtWidgets.QLabel(self.inside_021)
        self.qLabel2.setObjectName("res_event")
        self.buttonContb.addWidget(self.qLabel2)




    def thread_function(self, name):
        vto = self.files_list 
        listDirFiles = ListDirFiles("") 
        for each in vto:
            if listDirFiles.fileExist( each ):
                if self.checkBox01.isChecked(): 
                    # os.system("xfce4-terminal -e ' shred -vuz * \""+ each +"\"'")
                    
                    
                    vero = subprocess.run(["shred", "-vuz",  each], capture_output=True)
                    print(vero)
                    print("file processed - [" + each + "]")

        print ( " process exited ")
        self.exitFilter()




    def event_clicked_checkbox11(self, state):  
        if state == QtCore.Qt.Checked:
            x = threading.Thread(target=self.thread_function, args=( True,)) 
            x.start()
        else:
            print('Unchecked')
            # self.checkBox01.setChecked( True)
 

    def event_clicked_button04(self):  
       self.exitFilter()

    def event_clicked_button03(self):  
        vto = self.files_list 
        new_v = []
        for each in vto:
            new_v.append( ntpath.basename( each ))
        self.updateOutput(new_v )

    def event_clicked_button02(self):  
        self.updateOutput( self.files_list )

    def event_clicked_button01(self):
        self.files_list = []            
        self.updateOutput( [] )
    


    def exitFilter ( self ):
        vto = self.files_list 
        listDirFiles = ListDirFiles("")
        new_v = []
        for each in vto:
            if listDirFiles.fileExist( each ):
                new_v.append(  each  )
        self.files_list = new_v
        self.updateOutput(new_v )


    def updateOutput ( self, files_list ) : 
        self.plainTextEdit.setPlainText("")
        for index, each in  enumerate(files_list) : 
            self.plainTextEdit.setPlainText( self.plainTextEdit.toPlainText() + "\n" + "[" + str( index + 1 ) + "]" + each ) 



    def pictureDropped(self, l):
        print(l)
        for each in l :
            listDirFiles = ListDirFiles( each ) 
            for eachIn in listDirFiles.getFiles() :
                if not( eachIn in self.files_list): 
                    self.files_list.append( eachIn )
            
        self.updateOutput( self.files_list )
 



    def responsive_init (self, super, event):
        self.inActionTab01.setGeometry(QtCore.QRect( 0, 0,  self.width(), self.height()  ))
        
        self.inTab01Layout.setGeometry(QtCore.QRect( 0, 0,  self.inActionTab01.width(), self.inActionTab01.height()  ))
        self.plainTextEdit.setGeometry(QtCore.QRect( 0, -1,  self.inside_02.width(), self.inside_02.height()  ))
        
        self.buttonConta.setGeometry(QtCore.QRect( 0, -1,  self.inside_011.width(), self.inside_011.height()  ))
        self.buttonContb.setGeometry(QtCore.QRect( 0, -1,  self.inside_021.width(), self.inside_021.height()  ))
        
        self.inside_02.setMaximumSize(self.width() /2 , self.height())
 
#  for drag event component 
class DropComponent(QtWidgets.QLabel): 
    def __init__(self, type, supera, parent=None):
        super(DropComponent, self).__init__(parent)
        self.super = supera 

        color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
        self.setStyleSheet("background-color: {}".format(color.name()))
  

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


        self.tab01 = Tab01( self )  
        self.mainContentTab.addTab(self.tab01, "action 1")




        self.tab02 = Tab02( self )  
        self.mainContentTab.addTab(self.tab02, "action 2")






 
        
        lay.addWidget(self.widget_2 )





        # color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
        # self.menuItemsContainer.setStyleSheet("background-color: {}".format(color.name()))




    # trigger when window size is changed, updateing all responsive widgets 
    def responsive_init( self, event ) :  

        self.menuItemsContainer.setGeometry(QtCore.QRect(0, 0, self.widget.width(), 31)) 
        self.mainContentTab.setGeometry(QtCore.QRect( 0, 0, self.widget_2.width(), self.widget_2.height()))


        try:
            self.tab01.responsive_init( self, event )
            self.tab02.responsive_init( self, event )
        except Exception as e:
            print( e )
            pass



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
    



 
