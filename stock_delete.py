# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock_delete.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_stock_delete(object):
    
    def return_true(self):
        self.set_status = 1
    
    def return_false(self):
        self.set_status = 0
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(336, 187)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(336, 187))
        Dialog.setMaximumSize(QtCore.QSize(336, 187))
        Dialog.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.289773 rgba(191, 191, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
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
"")
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setStyleSheet("font-style:palatino linotype;background:white;")
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.textBrowser)
        spacerItem1 = QtWidgets.QSpacerItem(405, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(405, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.buttonBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.retranslateUi(Dialog)
        
        self.set_status = 0
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.return_true)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.rejected.connect(self.return_false)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.buttonBox, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "confirm?"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#aa007f;\">Are You Sure?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#aa007f;\">Once Changes Made Cannot be Undone!!!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_stock_delete()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

