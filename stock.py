# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

from adv_search import Ui_Dialog_adv_search
from stock_add import Ui_Dialog_stock_add
from stock_delete import Ui_Dialog_stock_delete

class Ui_Stock(object):

    def regular_search(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        tel = self.lineEdit.text()
        cursor.execute("SELECT * FROM available_stock where item_name = %s or supp_name = %s or brand_name = %s or category_name = %s or item_id = %s",(tel,tel,tel,tel,tel))
        data = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row_number = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()

    def advance_search(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_adv_search()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        req_tupple = ui.returning
        #return tupple from search dialog aand pu condition in delete dialog by retuirning some value
        if(req_tupple[0] == 1):
            db=pymysql.connect("localhost","root","","ims")
            cursor=db.cursor()
            cursor.execute("select * from available_stock where category_name = %s and brand_name = %s",(req_tupple[2],req_tupple[3]))
            data=cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_no =self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_no)
                for column_no,data in enumerate(row_data):
                    self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
            db.close()
        elif(req_tupple[0] == 2):
            db=pymysql.connect("localhost","root","","ims")
            cursor=db.cursor()
            cursor.execute("select * from available_stock where item_name = %s and category_name = %s and brand_name = %s",(req_tupple[1],req_tupple[2],req_tupple[3]))
            data=cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_no =self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_no)
                for column_no,data in enumerate(row_data):
                    self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
            db.close()
        elif(req_tupple[0] == 3):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Please selcet a Brand or Category')
            self.display_msg.show()

    def update_quantity(self):
        selected_col = 1
        selected_row = self.tableWidget.currentItem().row()
        selected_item_id = self.tableWidget.item(selected_row,selected_col).text()
        updated_quantity = self.lineEdit_2.text()

        if(self.lineEdit_2.text() == "" or not updated_quantity.isdigit() or selected_item_id == 'None'):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Please Enter valid Quantity')
            self.display_msg.show()
        else:
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("UPDATE stock SET stock_quantity = %s where stock_item_id=%s",(updated_quantity,selected_item_id))
            db.commit()
            db.close()

            self.display_msg.setWindowTitle('Information')
            self.display_msg.setText('Quantity Updated')
            self.display_msg.show()

            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM available_stock where item_id = %s",selected_item_id)
            data = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_number = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            db.close()

    def add_item(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_stock_add()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        req_tupple = ui.returning
        #print(req_tupple)
        if(req_tupple[0] == 2):
            #error
            if(req_tupple[1] == 1):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Select Supplier Name')
                self.display_msg.show()
            elif(req_tupple[1]==2):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Select Category or Enter New if not Exists')
                self.display_msg.show()
            elif(req_tupple[1]==3):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Select EITHER Existing Category or New Category')
                self.display_msg.show()
            elif(req_tupple[1]==4):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Select Brand or Enter New if not Exists')
                self.display_msg.show()
            elif(req_tupple[1]==5):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Select EITHER Existing Brand or New Brand')
                self.display_msg.show()
            elif(req_tupple[1]==6):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Enter valid Item Name')
                self.display_msg.show()
            elif(req_tupple[1]==7):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Enter valid Price')
                self.display_msg.show()
            elif(req_tupple[1]==8):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Enter valid Quantity')
                self.display_msg.show()
            elif(req_tupple[1]==9):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Category name already Exists')
                self.display_msg.show()
            elif(req_tupple[1]==10):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Brand name already Exists')
                self.display_msg.show()
            elif(req_tupple[1]==11):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Item already Exist')
                self.display_msg.show()
                  
        if(req_tupple[0] == 1):
            #item added
            req_item = str(req_tupple[2])
            req_category = str(req_tupple[3])
            req_brand = str(req_tupple[4])
            req_item_desc = str(req_tupple[5])
            req_price = int(req_tupple[6])
            req_quantity = int(req_tupple[7])
            req_supplier= str(req_tupple[8])
            if(req_tupple[1] == 1):
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into category (category_name) values (%s)",req_category)
                db.commit()
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into brand (brand_name) values (%s)",req_brand)
                db.commit()
                db.close()


                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select category_id from category where category_name = %s",req_category)
                data = cursor.fetchone()
                req_category_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select brand_id from brand where brand_name = %s",req_brand)
                data = cursor.fetchone()
                req_brand_id =  data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select supp_id from supplier where supp_name = %s ",req_supplier)
                data = cursor.fetchone()
                req_supp_id = data[0]
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into items (item_category_id,item_brand_id,item_name,item_desc,item_price) values (%s, %s, %s ,%s,%s)",(req_category_id,req_brand_id,req_item,req_item_desc,req_price))        
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select item_id from items where item_name = %s ",req_item)
                data = cursor.fetchone()
                req_item_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into stock (stock_item_id,stock_quantity,stock_sup_id) values (%s, %s, %s)",(req_item_id,req_quantity,req_supp_id))
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select * from available_stock where item_id = %s",req_item_id)
                data=cursor.fetchall()
                self.tableWidget.setRowCount(0)
                for row_data in data:
                    row_no = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_no)
                    for column_no,data in enumerate(row_data):
                        self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
                db.close()
                self.display_msg.setWindowTitle('Information')
                self.display_msg.setText('Item Added Successfully')
                self.display_msg.show()

            elif(req_tupple[1] == 2):
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into category (category_name) values (%s)",req_category)
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select category_id from category where category_name = %s",req_category)
                data = cursor.fetchone()
                req_category_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select brand_id from brand where brand_name = %s",req_brand)
                data = cursor.fetchone()
                req_brand_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select supp_id from supplier where supp_name = %s ",req_supplier)
                data = cursor.fetchone()
                req_supp_id = data[0]
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into items (item_category_id,item_brand_id,item_name,item_desc,item_price) values (%s, %s, %s ,%s,%s)",(req_category_id,req_brand_id,req_item,req_item_desc,req_price))        
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select item_id from items where item_name = %s ",req_item)
                data = cursor.fetchone()
                req_item_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into stock (stock_item_id,stock_quantity,stock_sup_id) values (%s, %s, %s)",(req_item_id,req_quantity,req_supp_id))
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select * from available_stock where item_id = %s",req_item_id)
                data=cursor.fetchall()
                self.tableWidget.setRowCount(0)
                for row_data in data:
                    row_no = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_no)
                    for column_no,data in enumerate(row_data):
                        self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
                db.close()
                self.display_msg.setWindowTitle('Information')
                self.display_msg.setText('Item Added Successfully')
                self.display_msg.show()
                
                
            elif(req_tupple[1] == 3):
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into brand (brand_name) values (%s)",req_brand)
                db.commit()
                db.close()


                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select category_id from category where category_name = %s",req_category)
                data = cursor.fetchone()
                req_category_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select brand_id from brand where brand_name = %s",req_brand)
                data = cursor.fetchone()
                req_brand_id =  data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select supp_id from supplier where supp_name = %s ",req_supplier)
                data = cursor.fetchone()
                req_supp_id = data[0]
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into items (item_category_id,item_brand_id,item_name,item_desc,item_price) values (%s, %s, %s ,%s,%s)",(req_category_id,req_brand_id,req_item,req_item_desc,req_price))        
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select item_id from items where item_name = %s ",req_item)
                data = cursor.fetchone()
                req_item_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into stock (stock_item_id,stock_quantity,stock_sup_id) values (%s, %s, %s)",(req_item_id,req_quantity,req_supp_id))
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select * from available_stock where item_id = %s",req_item_id)
                data=cursor.fetchall()
                self.tableWidget.setRowCount(0)
                for row_data in data:
                    row_no = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_no)
                    for column_no,data in enumerate(row_data):
                        self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
                db.close()
                self.display_msg.setWindowTitle('Information')
                self.display_msg.setText('Item Added Successfully')
                self.display_msg.show()

            elif(req_tupple[1] == 4):
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select category_id from category where category_name = %s",req_category)
                data = cursor.fetchone()
                req_category_id = data[0]
                #print(req_category_id)
                #print(type(req_category_id))
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select brand_id from brand where brand_name = %s",req_brand)
                data = cursor.fetchone()
                req_brand_id =  data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select supp_id from supplier where supp_name = %s ",req_supplier)
                data = cursor.fetchone()
                req_supp_id = data[0]
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into items (item_category_id,item_brand_id,item_name,item_desc,item_price) values (%s, %s, %s ,%s,%s)",(req_category_id,req_brand_id,req_item,req_item_desc,req_price))        
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select item_id from items where item_name = %s ",req_item)
                data = cursor.fetchone()
                req_item_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into stock (stock_item_id,stock_quantity,stock_sup_id) values (%s, %s, %s)",(req_item_id,req_quantity,req_supp_id))
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select * from available_stock where item_id = %s",req_item_id)
                data=cursor.fetchall()
                self.tableWidget.setRowCount(0)
                for row_data in data:
                    row_no = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_no)
                    for column_no,data in enumerate(row_data):
                        self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
                db.close()
                self.display_msg.setWindowTitle('Information')
                self.display_msg.setText('Item Added Successfully')
                self.display_msg.show()
                
                

    def delete_item(self):
        selected_col = 1
        selected_row = self.tableWidget.currentItem().row()
        selected_item_id = self.tableWidget.item(selected_row,selected_col).text()
        selected_col = 3
        selected_category = self.tableWidget.item(selected_row,selected_col).text()
        selected_col = 4
        selected_brand = self.tableWidget.item(selected_row,selected_col).text()
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_stock_delete()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        got_status = ui.set_status
        if(got_status==1):
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("delete from stock where stock_item_id = %s",selected_item_id)
            db.commit()
            db.close()
            
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("delete from items where item_id = %s",selected_item_id)
            db.commit()
            db.close()

            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            print("selected catid",selected_category)
            cursor.execute("select count(%s) as c_count from available_stock where category_name = %s",(selected_category,selected_category))
            data_c = cursor.fetchone()
            print(data_c[0])
            db.close()

            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("select count(%s) from available_stock where brand_name = %s",(selected_brand,selected_brand))
            data_b = cursor.fetchone()
            print(data_b[0])
            db.close()

            if(data_c[0] == 0):
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("delete from category where category_name = %s",selected_category)
                db.commit()
                db.close()
                
            if(data_b[0] == 0):
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("delete from brand where brand_name = %s",selected_brand)
                db.commit()
                db.close()
            
            self.display_msg.setWindowTitle('Information')
            self.display_msg.setText('Delete Successfull')
            self.display_msg.show()
            self.initial_stock()

    def refresh_table(self):
        self.initial_stock()
        #self.lineEdit.clear()
        #self.lineEdit.clear()

    def initial_stock(self):
        db=pymysql.connect("localhost","root","","ims")
        cursor=db.cursor()
        query = "SELECT * from available_stock"
        try:
            cursor.execute(query)
            data=cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_no =self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_no)
                for column_no,data in enumerate(row_data):
                    self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
            db.commit()
        except:
            db.rollback()
        db.close()

    def setupUi(self, Stock):
        Stock.setObjectName("Stock")
        Stock.resize(1014, 794)
        Stock.setStyleSheet("QMainWindow{\n"
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
"")
        Stock.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Stock)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 6, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(950, 550))
        self.tableWidget.setMaximumSize(QtCore.QSize(580, 16777215))
        font = QtGui.QFont()
        font.setFamily("palatino linotype")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("font: 11pt \"palatino linotype\";\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(500)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(48)
        self.gridLayout.addWidget(self.tableWidget, 5, 2, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 7, 6, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 2, 1, 5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setStyleSheet("font-size:18px;font:bold;font-style:palatino linotype;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 4, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 5)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet("font-size:18px;font:bold;font-style:palatino linotype;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font-size:18px;font:bold;font-style:palatino linotype;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("font-size:18px;font:bold;font-style:palatino linotype;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("font-size:18px;font:bold;font-style:palatino linotype;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 6, 2, 1, 5)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("QLabel{\n"
"font-size:28px;\n"
"font-family:\"palatino linotype\";\n"
"font-weight: bold;\n"
"\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 5)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("font-size:18px;font:bold;font-style:palatino linotype;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 4, 1, 1)
        Stock.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Stock)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 21))
        self.menubar.setObjectName("menubar")
        Stock.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Stock)
        self.statusbar.setObjectName("statusbar")
        Stock.setStatusBar(self.statusbar)
        
        self.pushButton_4.setFocus()
        self.pushButton.clicked.connect(self.regular_search)
        self.pushButton_2.clicked.connect(self.delete_item)
        self.pushButton_3.clicked.connect(self.add_item)
        self.initial_stock()
        self.pushButton_4.clicked.connect(self.advance_search)
        self.pushButton_5.clicked.connect(self.refresh_table)
        self.pushButton_6.clicked.connect(self.update_quantity)
        self.display_msg = QtWidgets.QMessageBox()
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)


        self.retranslateUi(Stock)
        QtCore.QMetaObject.connectSlotsByName(Stock)
        Stock.setTabOrder(self.pushButton_4, self.pushButton_5)
        Stock.setTabOrder(self.pushButton_5, self.pushButton_3)
        Stock.setTabOrder(self.pushButton_3, self.pushButton_2)
        Stock.setTabOrder(self.pushButton_2, self.lineEdit)
        Stock.setTabOrder(self.lineEdit, self.pushButton)
        Stock.setTabOrder(self.pushButton, self.lineEdit_2)
        Stock.setTabOrder(self.lineEdit_2, self.pushButton_6)
        Stock.setTabOrder(self.pushButton_6, self.tableWidget)
        Stock.setTabOrder(self.tableWidget, self.pushButton_4)

    def retranslateUi(self, Stock):
        _translate = QtCore.QCoreApplication.translate
        Stock.setWindowTitle(_translate("Stock", "Stock"))
        self.lineEdit_2.setPlaceholderText(_translate("Stock", "New Quantity"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Stock", "Supplier Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Stock", "Item Id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Stock", "Item Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Stock", "Category"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Stock", "Brand Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Stock", "Quantity"))
        self.pushButton_6.setText(_translate("Stock", " Update Quantity"))
        self.lineEdit.setPlaceholderText(_translate("Stock", "Master Search"))
        self.pushButton_5.setText(_translate("Stock", "Refresh"))
        self.pushButton.setText(_translate("Stock", "Search"))
        self.pushButton_4.setText(_translate("Stock", "Advance Search"))
        self.pushButton_2.setText(_translate("Stock", "Delete Item"))
        self.label_2.setText(_translate("Stock", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Stock</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Stock", "Add Item"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stock = QtWidgets.QMainWindow()
    ui = Ui_Stock()
    ui.setupUi(Stock)
    Stock.show()
    sys.exit(app.exec_())

