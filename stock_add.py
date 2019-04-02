# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock_add.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Dialog_stock_add(object):
    def drop_menu(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        #supplier list 
        cursor.execute("SELECT supp_name FROM supplier group by supp_name")
        data = cursor.fetchall()
        for supp_name in data:
            self.comboBox.addItem(supp_name[0])
        db.close()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        #category list
        cursor.execute("SELECT category_name FROM category group by category_name")
        data = cursor.fetchall()
        for category_name in data:
            self.comboBox_2.addItem(category_name[0])
        db.close()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        #brand list
        cursor.execute("SELECT brand_name FROM brand group by brand_name")
        data = cursor.fetchall()
        for brand_name in data:
            self.comboBox_3.addItem(brand_name[0])
        db.close()
    def return_false(self):
        self.returning = (0,'hi')
        #close case 2

    def check_input(self):
        sel_supplier = self.comboBox.currentText()
        sel_category = self.comboBox_2.currentText()
        sel_new_category = self.lineEdit_2.text()
        sel_brand = self.comboBox_3.currentText()
        sel_new_brand = self.lineEdit_3.text()
        sel_item = self.lineEdit_5.text()
        sel_item_desc = self.lineEdit_4.text()
        sel_price = self.lineEdit_6.text()
        sel_quantity = self.lineEdit_7.text()

        

        if(sel_supplier == '--Not Selected--'):
            self.returning = (2,1,'hi')
            
        elif(sel_category == '--Not Selected--' and sel_new_category == ""):
            self.returning = (2,2,'hi')
             
        elif(sel_category != '--Not Selected--' and sel_new_category != ""):
            self.returning = (2,3,'hi')
             
        elif(sel_brand == '--Not Selected--' and sel_new_brand == ""):
            self.returning = (2,4,'hi')
             
        elif(sel_brand != '--Not Selected--' and sel_new_brand != ""):
            self.returning = (2,5,'hi')
             
        elif(sel_item == ""):
            self.returning = (2,6,'hi')
             
        elif(sel_price == "" or not sel_price.isdigit()):
            self.returning = (2,7,'hi')
             
        elif(sel_quantity == "" or not sel_quantity.isdigit()):
            self.returning = (2,8,'hi')
             
            
        elif(not sel_new_category == "" and self.check_category()):
            self.returning = (2,9,'hi')
            
        elif(not sel_new_brand == "" and self.check_brand()):
            self.returning = (2,10,'hi')
            
        elif(not sel_item == "" and self.check_item()):
            self.returning = (2,11,'hi')

        else:
            if(sel_category == '--Not Selected--' and sel_brand == '--Not Selected--'):
                self.returning = (1,1,sel_item,sel_new_category,sel_new_brand,sel_item_desc,sel_price,sel_quantity,sel_supplier,'hi')
            elif(sel_category == '--Not Selected--' and not sel_brand == '--Not Selected--'):
                self.returning = (1,2,sel_item,sel_new_category,sel_brand,sel_item_desc,sel_price,sel_quantity,sel_supplier,'hi')
            elif(not sel_category == '--Not Selected--' and sel_brand == '--Not Selected--'):
                self.returning = (1,3,sel_item,sel_category,sel_new_brand,sel_item_desc,sel_price,sel_quantity,sel_supplier,'hi')
            elif(not sel_category == '--Not Selected--' and not sel_brand == '--Not Selected--'):
                self.returning = (1,4,sel_item,sel_category,sel_brand,sel_item_desc,sel_price,sel_quantity,sel_supplier,'hi')
                
    def check_category(self):
        sel_supplier = self.comboBox.currentText()
        sel_category = self.comboBox_2.currentText()
        sel_new_category = self.lineEdit_2.text()
        sel_brand = self.comboBox_3.currentText()
        sel_new_brand = self.lineEdit_3.text()
        sel_item = self.lineEdit_5.text()
        sel_item_desc = self.lineEdit_4.text()
        sel_price = self.lineEdit_6.text()
        sel_quantity = self.lineEdit_7.text()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        data = cursor.execute("select category_name from category where category_name = %s",sel_new_category)
        db.close()
        return(data)
    
    def check_brand(self):
        sel_supplier = self.comboBox.currentText()
        sel_category = self.comboBox_2.currentText()
        sel_new_category = self.lineEdit_2.text()
        sel_brand = self.comboBox_3.currentText()
        sel_new_brand = self.lineEdit_3.text()
        sel_item = self.lineEdit_5.text()
        sel_item_desc = self.lineEdit_4.text()
        sel_price = self.lineEdit_6.text()
        sel_quantity = self.lineEdit_7.text()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        data = cursor.execute("select brand_name from brand where brand_name = %s",sel_new_brand)
        db.close()
        return(data)
    
    def check_item(self):
        sel_supplier = self.comboBox.currentText()
        sel_category = self.comboBox_2.currentText()
        sel_new_category = self.lineEdit_2.text()
        sel_brand = self.comboBox_3.currentText()
        sel_new_brand = self.lineEdit_3.text()
        sel_item = self.lineEdit_5.text()
        sel_item_desc = self.lineEdit_4.text()
        sel_price = self.lineEdit_6.text()
        sel_quantity = self.lineEdit_7.text()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        data = cursor.execute("select item_name from items where item_name = %s",sel_item)
        db.close()
        return(data)

    def add_item(self):
        sel_supplier = self.comboBox.currentText()
        sel_category = self.comboBox_2.currentText()
        sel_new_category = self.lineEdit_2.text()
        sel_brand = self.comboBox_3.currentText()
        sel_new_brand = self.lineEdit_3.text()
        sel_item = self.lineEdit_5.text()
        sel_item_desc = self.lineEdit_4.text()
        sel_price = self.lineEdit_6.text()
        sel_quantity = self.lineEdit_7.text()
        
        if(sel_category == '--Not Selected--'):
            req_category = sel_new_category
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("insert into category(category_name) values (%s)",self.lineEdit_2.text())
            db.commit()
            db.close()
        else:
            req_category = sel_category
        if(sel_brand == '--Not Selected--'):
            req_brand = sel_new_brand
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("insert into brand(brand_name) values (%s)",self.lineEdit_3.text())
            db.commit()
            db.close()
        else:
            req_brand = sel_brand
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("select category_id from category where category_name = %s",req_category)
        data = cursor.fetchone()
        req_category_id = data[0]
        db.close()
        
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("select brand_id from brand where brand_name = '"+req_brand+"'")
        data = cursor.fetchone()
        req_brand_id =  data[0]
        db.close()

        
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("insert into items (item_category_id,item_brand_id,item_name,item_desc,item_price) values (%s, %s, %s ,%s,%s)",(req_category_id,req_brand_id,sel_item,sel_item_desc,sel_price))
        db.commit()
        db.close()
                       
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("select item_id from items where item_name = %s ",sel_item)
        data = cursor.fetchone()
        req_item_id = data[0]
        db.close()

        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("select supp_id from supplier where supp_name = %s ",sel_supplier)
        data = cursor.fetchone()
        req_supp_id = data[0]
        db.close()
        
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("insert into stock (stock_item_id,stock_quantity,stock_sup_id) values (%s, %s, %s)",(req_item_id,sel_quantity,req_supp_id))
        db.commit()
        db.close()
        
    def reset_all(self):
        self.lineEdit_2.setFocus()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)

    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(689, 398)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(689, 398))
        Dialog.setMaximumSize(QtCore.QSize(689, 398))
        Dialog.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.289773 rgba(191, 191, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QDialog{\n"
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
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(226, 20))
        self.lineEdit_4.setStyleSheet("background:white;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 7, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 12, 1, 1, 3)
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(226, 20))
        self.lineEdit_6.setStyleSheet("background:white;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 9, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 11, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 10, 1, 1, 3)
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(226, 20))
        self.lineEdit_7.setStyleSheet("background:white;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 9, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 8, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(226, 20))
        self.lineEdit_5.setStyleSheet("background:white;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 7, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 1, 1, 3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(226, 20))
        self.lineEdit_3.setStyleSheet("background:white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 3, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setMinimumSize(QtCore.QSize(226, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 1, 1, 3)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(226, 20))
        self.lineEdit_2.setStyleSheet("background:white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 1, 1, 3)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(226, 20))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 4, 13, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 0, 1, 1, 3)
        spacerItem9 = QtWidgets.QSpacerItem(28, 377, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 0, 0, 13, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 28))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 11, 2, 1, 1)

        self.comboBox.setFocus()
        self.returning = (0,'hi')
        self.display_msg = QtWidgets.QMessageBox(Dialog)
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)
        self.drop_menu()
        self.pushButton_3.clicked.connect(self.reset_all)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.check_input)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.rejected.connect(self.return_false)
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox, self.pushButton_3)
        Dialog.setTabOrder(self.pushButton_3, self.comboBox_2)
        Dialog.setTabOrder(self.comboBox_2, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.comboBox_3)
        Dialog.setTabOrder(self.comboBox_3, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.lineEdit_5)
        Dialog.setTabOrder(self.lineEdit_5, self.lineEdit_4)
        Dialog.setTabOrder(self.lineEdit_4, self.lineEdit_6)
        Dialog.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        Dialog.setTabOrder(self.lineEdit_7, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.comboBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add New Item"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Item Description"))
        self.lineEdit_6.setPlaceholderText(_translate("Dialog", "Item Price"))
        self.lineEdit_7.setPlaceholderText(_translate("Dialog", "Item Quantity in Units"))
        self.label_6.setText(_translate("Dialog", "Price & Quantity"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "Item Name"))
        self.label_3.setText(_translate("Dialog", "Item Name"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "New Brand"))
        self.label_5.setText(_translate("Dialog", "Brand"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "New Category"))
        self.label_4.setText(_translate("Dialog", "Category"))
        self.label.setText(_translate("Dialog", "Supplier Name"))
        self.pushButton_3.setText(_translate("Dialog", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_stock_add()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

