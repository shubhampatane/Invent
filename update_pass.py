# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_pass.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_update_pass(object):
    def accepted(self):
        sel_user = self.comboBox.currentText()
        old_pass = self.lineEdit.text()
        new_pass = self.lineEdit_2.text()
        conf_pass = self.lineEdit_3.text()

        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        cursor.execute("SELECT user_name,user_pass FROM user_info where user_name = %s", sel_user)
        data = cursor.fetchall()
        db.close()
        for user_password in data:
            req_password = data[0][1]
        if (not req_password == old_pass):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Incorrect Password')
            self.display_msg.show()
            # self.lineEdit.setText("")
        elif new_pass == "":
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('New Password cannot be blank')
            self.display_msg.show()
        elif conf_pass =="":
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Confirmation Password cannot be blank')
            self.display_msg.show()
        elif(not new_pass  == conf_pass and not new_pass == ""):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Password dose not Match')
            self.display_msg.show()
            # self.lineEdit_2.setText("")
            # self.lineEdit_3.setText("")
        else:
            db = pymysql.connect("localhost", "root", "", "ims")
            cursor = db.cursor()
            cursor.execute("UPDATE user_info SET user_pass = %s where user_name = %s", (new_pass, sel_user))
            db.commit()
            db.close()
            self.display_msg.setWindowTitle('Information')
            self.display_msg.setText('Password updated SUCCESSFULLY')
            self.display_msg.show()

    def rejected(self):
        a=12
    def dropmenu(self):
        self.comboBox.addItem("customer")
        self.comboBox.addItem("supplier")
        self.comboBox.addItem("orders")
        self.comboBox.addItem("pricing")
        self.comboBox.addItem("billing")
        self.comboBox.addItem("stocks")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(635, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(635, 438))
        Dialog.setMaximumSize(QtCore.QSize(635, 438))
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
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(130, 380, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 90, 351, 22))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(152, 150, 321, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(152, 210, 321, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(152, 270, 321, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.dropmenu()
        self.display_msg = QtWidgets.QMessageBox(Dialog)
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.rejected.connect(self.rejected)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Old Password"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "New Password"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Confirm New Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_update_pass()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

