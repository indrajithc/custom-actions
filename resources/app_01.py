# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_01.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(759, 575)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 50, 631, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 651, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hboxlayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.hboxlayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.mainContentTab = QtWidgets.QTabWidget(self.widget_2)
        self.mainContentTab.setGeometry(QtCore.QRect(-4, -1, 641, 361))
        self.mainContentTab.setObjectName("mainContentTab")
        self.tab01 = QtWidgets.QWidget()
        self.tab01.setObjectName("tab01")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab01)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 631, 331))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget_3.setEnabled(True)
        self.widget_3.setMinimumSize(QtCore.QSize(50, 0))
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setEnabled(True)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 629, 329))
        self.widget_4.setMinimumSize(QtCore.QSize(50, 0))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout.addWidget(self.widget_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab01)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 631, 331))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_5 = QtWidgets.QWidget(self.horizontalLayoutWidget_3)
        self.widget_5.setEnabled(True)
        self.widget_5.setMinimumSize(QtCore.QSize(50, 0))
        self.widget_5.setObjectName("widget_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_5)
        self.plainTextEdit.setGeometry(QtCore.QRect(160, 60, 104, 70))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.mainContentTab.addTab(self.tab01, "")
        self.tab02 = QtWidgets.QWidget()
        self.tab02.setObjectName("tab02")
        self.mainContentTab.addTab(self.tab02, "")
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        self.mainContentTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "dfsdf sdf sdf\n"
"sd\n"
"f \n"
"sdf\n"
"sdf\n"
"sdf\n"
"sd\n"
"fs\n"
"dfsdf \n"
""))
        self.mainContentTab.setTabText(self.mainContentTab.indexOf(self.tab01), _translate("Dialog", "Tab 1"))
        self.mainContentTab.setTabText(self.mainContentTab.indexOf(self.tab02), _translate("Dialog", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
