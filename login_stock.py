# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Dialog_stock_login(object):
    
    def user_authenticate(self):
        sel_user_name = self.lineEdit.text()
        sel_password  = self.lineEdit_2.text()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("SELECT user_name,user_pass FROM user_info where user_id = 7")
        data = cursor.fetchall()
        for user_name in data:
            req_user_name = data[0][0]
        for user_password in data:
            req_password = data[0][1]
        if(req_user_name == sel_user_name and req_password == sel_password):
            self.returning = 1
        else:
            self.returning = 2
        db.close()
        
    def return_false(self):
        self.returning = 0
        #close case 
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(449, 318)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(449, 318))
        Dialog.setMaximumSize(QtCore.QSize(449, 318))
        Dialog.setStyleSheet("QPushButton {\n"
"    width: 150%;\n"
"height:20px;\n"
"    padding: 3%;\n"
"    background:#25D366;\n"
"    border-bottom: 2px solid #30C29E;\n"
"    border-top-style: none;\n"
"    border-right-style: none;\n"
"    border-left-style: none;    \n"
"    color: #fff;\n"
" border-radius: 10px;\n"
"font-size:20px;\n"
"color:purple;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: darkgreen;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size:18px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"QDialog{\n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.289773 rgba(191, 191, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(150, 20))
        self.label_2.setMaximumSize(QtCore.QSize(150, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 3)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(150, 20))
        self.label.setMaximumSize(QtCore.QSize(150, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 1, 1, 3)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 8, 1, 1, 4)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.user_authenticate)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.rejected.connect(self.return_false)
        self.display_msg = QtWidgets.QMessageBox(Dialog)
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)
        self.returning = 0

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.lineEdit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stock Login"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label.setText(_translate("Dialog", "Stock User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_stock_login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

