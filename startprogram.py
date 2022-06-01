# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forkeshe.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QAbstractItemView, QHeaderView
from startDAG import transfer, startrun
import sys
import os


class Ui_forkeshe(object):
    def setupUi(self, forkeshe):
        forkeshe.setObjectName("forkeshe")
        forkeshe.resize(1304, 1013)
        forkeshe.setFixedSize(1304, 1013)
        forkeshe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.res = []
        self.centralwidget = QtWidgets.QWidget(forkeshe)
        self.centralwidget.setObjectName("centralwidget")
        self.code_r = QtWidgets.QTableWidget(self.centralwidget)
        self.code_r.setGeometry(QtCore.QRect(10, 50, 511, 451))
        self.code_r.setStyleSheet("QHeaderView{\n"
                                  "              font-size: 19px;\n"
                                  "          border: 1px solid rgb(255, 255, 255);\n"
                                  "        background: rgb(100, 188, 238);\n"
                                  "          min-height:40px;\n"
                                  "           \n"
                                  "} \n"
                                  " \n"
                                  " \n"
                                  "QHeaderView::section:horizontal { \n"
                                  "        border: 1px solid rgb(255, 255, 255);\n"
                                  "          border-bottom: 0px;\n"
                                  "        color: rgb(2, 65, 132);\n"
                                  "        background: transparent;\n"
                                  "        padding-left: 2px;\n"
                                  "        min-width:60px;\n"
                                  "}\n"
                                  "QHeaderView::section:horizontal:hover {    \n"
                                  "        color: white;\n"
                                  "        background: rgb(11,82,202);\n"
                                  "}\n"
                                  "QHeaderView::section:horizontal:pressed {\n"
                                  "        color: white;\n"
                                  "        background: rgb(39,106,220);\n"
                                  "}\n"
                                  "QHeaderView::section:vertical { \n"
                                  "        border: 1px solid rgb(255, 255, 255);\n"
                                  "          border-bottom: 0px;\n"
                                  "        color: rgb(2, 65, 132);\n"
                                  "        background: rgb(255, 255, 255,180);\n"
                                  "        padding-top: 3px;\n"
                                  "        min-width:60px;\n"
                                  "        \n"
                                  "}\n"
                                  "QHeaderView::section:vertical:hover {\n"
                                  "        color: white;\n"
                                  "        background: rgb(11,82,202);    \n"
                                  "}\n"
                                  "QHeaderView::section:vertical:pressed {    \n"
                                  "        color: white;\n"
                                  "        background: rgb(39,106,220);\n"
                                  "}\n"
                                  " \n"
                                  " \n"
                                  "QHeaderView::up-arrow {\n"
                                  "        width: 13px;\n"
                                  "        height: 11px;\n"
                                  "        padding-right: 0px;\n"
                                  "        image: url(:/arrow_up.png);\n"
                                  "        subcontrol-position: center right;\n"
                                  "}\n"
                                  "QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
                                  "     \n"
                                  "}\n"
                                  "QHeaderView::down-arrow {\n"
                                  "        width: 13px;\n"
                                  "        height: 11px;\n"
                                  "        padding-right: 10px;\n"
                                  "        image: url(:/arrow_down.png);\n"
                                  "        subcontrol-position: center right;\n"
                                  "}\n"
                                  "QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
                                  "     \n"
                                  "}\n"
                                  "QTableWidget,QTableView {\n"
                                  "        font-size: 17px;\n"
                                  "        color : rgb(1,37,116);                \n"
                                  "        border: 2px solid rgb(100, 188, 238);        \n"
                                  "        background: rgb(248,248,248);\n"
                                  "        gridline-color: rgb(196,226,255);    \n"
                                  "        text-align: center;    \n"
                                  "        outline:0px;\n"
                                  "}\n"
                                  "QTableWidget::item,QTableView::item {    \n"
                                  "        padding-left: 5px;\n"
                                  "        padding-right: 5px;\n"
                                  "        border: none; \n"
                                  "        background: rgba(251,251,253,200);\n"
                                  "}\n"
                                  "QTableWidget::item:selected,QTableView::item:selected {\n"
                                  "        background: rgba(207,230,253,200);\n"
                                  "        color : rgb(1,37,116);                \n"
                                  "}\n"
                                  " \n"
                                  " \n"
                                  "QTableView::item:alternate:!selected,QTableWidget::item:alternate:!selected,QListView::item:alternate:!selected \n"
                                  "{ \n"
                                  "    background: rgb(250,250,250); \n"
                                  "}\n"
                                  " \n"
                                  "QTableView::item:!alternate:!selected,QTableWidget::item:!alternate:!selected\n"
                                  "{ \n"
                                  "    background: rgb(240,247,254); \n"
                                  "}\n"
                                  "QScrollBar:vertical\n"
                                  "{\n"
                                  "    width:8px;\n"
                                  "    background:rgba(0,0,0,0%);\n"
                                  "    margin:0px,0px,0px,0px;\n"
                                  "    padding-top:9px; \n"
                                  "    padding-bottom:9px;\n"
                                  "}\n"
                                  "QScrollBar::handle:vertical\n"
                                  "{\n"
                                  "    width:8px;\n"
                                  "    background:rgba(0,0,0,25%);\n"
                                  "    border-radius:4px; \n"
                                  "    min-height:20;\n"
                                  "}\n"
                                  "QScrollBar::handle:vertical:hover\n"
                                  "{\n"
                                  "    width:8px;\n"
                                  "    background:rgba(0,0,0,50%);  \n"
                                  "    border-radius:4px;\n"
                                  "    min-height:20;\n"
                                  "}\n"
                                  "QScrollBar::add-line:vertical\n"
                                  "{\n"
                                  "    height:9px;width:8px;\n"
                                  "    border-image:url(:/images/a/3.png);\n"
                                  "    subcontrol-position:bottom;\n"
                                  "}\n"
                                  "QScrollBar::sub-line:vertical\n"
                                  "{\n"
                                  "    height:9px;width:8px;\n"
                                  "    border-image:url(:/images/a/1.png);\n"
                                  "    subcontrol-position:top;\n"
                                  "}\n"
                                  "QScrollBar::add-line:vertical:hover \n"
                                  "{\n"
                                  "    height:9px;width:8px;\n"
                                  "    border-image:url(:/images/a/4.png);\n"
                                  "    subcontrol-position:bottom;\n"
                                  "}\n"
                                  "QScrollBar::sub-line:vertical:hover\n"
                                  "{\n"
                                  "    height:9px;width:8px;\n"
                                  "    border-image:url(:/images/a/2.png);\n"
                                  "    subcontrol-position:top;\n"
                                  "}\n"
                                  "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
                                  "{\n"
                                  "    background:rgba(0,0,0,10%);\n"
                                  "    border-radius:4px;\n"
                                  "}")
        self.code_r.setObjectName("code_r")
        self.code_r.setColumnCount(4)
        self.code_r.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.code_r.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.code_r.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.code_r.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.code_r.setHorizontalHeaderItem(3, item)
        self.code = QtWidgets.QTableWidget(self.centralwidget)
        self.code.setGeometry(QtCore.QRect(10, 560, 511, 451))
        self.code.setStyleSheet("QHeaderView{\n"
                                "              font-size: 19px;\n"
                                "          border: 1px solid rgb(255, 255, 255);\n"
                                "        background: rgb(100, 188, 238);\n"
                                "          min-height:40px;\n"
                                "           \n"
                                "} \n"
                                " \n"
                                " \n"
                                "QHeaderView::section:horizontal { \n"
                                "        border: 1px solid rgb(255, 255, 255);\n"
                                "          border-bottom: 0px;\n"
                                "        color: rgb(2, 65, 132);\n"
                                "        background: transparent;\n"
                                "        padding-left: 2px;\n"
                                "        min-width:60px;\n"
                                "}\n"
                                "QHeaderView::section:horizontal:hover {    \n"
                                "        color: white;\n"
                                "        background: rgb(11,82,202);\n"
                                "}\n"
                                "QHeaderView::section:horizontal:pressed {\n"
                                "        color: white;\n"
                                "        background: rgb(39,106,220);\n"
                                "}\n"
                                "QHeaderView::section:vertical { \n"
                                "        border: 1px solid rgb(255, 255, 255);\n"
                                "          border-bottom: 0px;\n"
                                "        color: rgb(2, 65, 132);\n"
                                "        background: rgb(255, 255, 255,180);\n"
                                "        padding-top: 3px;\n"
                                "        min-width:60px;\n"
                                "        \n"
                                "}\n"
                                "QHeaderView::section:vertical:hover {\n"
                                "        color: white;\n"
                                "        background: rgb(11,82,202);    \n"
                                "}\n"
                                "QHeaderView::section:vertical:pressed {    \n"
                                "        color: white;\n"
                                "        background: rgb(39,106,220);\n"
                                "}\n"
                                " \n"
                                " \n"
                                "QHeaderView::up-arrow {\n"
                                "        width: 13px;\n"
                                "        height: 11px;\n"
                                "        padding-right: 0px;\n"
                                "        image: url(:/arrow_up.png);\n"
                                "        subcontrol-position: center right;\n"
                                "}\n"
                                "QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
                                "     \n"
                                "}\n"
                                "QHeaderView::down-arrow {\n"
                                "        width: 13px;\n"
                                "        height: 11px;\n"
                                "        padding-right: 10px;\n"
                                "        image: url(:/arrow_down.png);\n"
                                "        subcontrol-position: center right;\n"
                                "}\n"
                                "QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
                                "     \n"
                                "}\n"
                                "QTableWidget,QTableView {\n"
                                "        font-size: 17px;\n"
                                "        color : rgb(1,37,116);                \n"
                                "        border: 2px solid rgb(100, 188, 238);        \n"
                                "        background: rgb(248,248,248);\n"
                                "        gridline-color: rgb(196,226,255);    \n"
                                "        text-align: center;    \n"
                                "        outline:0px;\n"
                                "}\n"
                                "QTableWidget::item,QTableView::item {    \n"
                                "        padding-left: 5px;\n"
                                "        padding-right: 5px;\n"
                                "        border: none; \n"
                                "        background: rgba(251,251,253,200);\n"
                                "}\n"
                                "QTableWidget::item:selected,QTableView::item:selected {\n"
                                "        background: rgba(207,230,253,200);\n"
                                "        color : rgb(1,37,116);                \n"
                                "}\n"
                                " \n"
                                " \n"
                                "QTableView::item:alternate:!selected,QTableWidget::item:alternate:!selected,QListView::item:alternate:!selected \n"
                                "{ \n"
                                "    background: rgb(250,250,250); \n"
                                "}\n"
                                " \n"
                                "QTableView::item:!alternate:!selected,QTableWidget::item:!alternate:!selected\n"
                                "{ \n"
                                "    background: rgb(240,247,254); \n"
                                "}\n"
                                "QScrollBar:vertical\n"
                                "{\n"
                                "    width:8px;\n"
                                "    background:rgba(0,0,0,0%);\n"
                                "    margin:0px,0px,0px,0px;\n"
                                "    padding-top:9px; \n"
                                "    padding-bottom:9px;\n"
                                "}\n"
                                "QScrollBar::handle:vertical\n"
                                "{\n"
                                "    width:8px;\n"
                                "    background:rgba(0,0,0,25%);\n"
                                "    border-radius:4px; \n"
                                "    min-height:20;\n"
                                "}\n"
                                "QScrollBar::handle:vertical:hover\n"
                                "{\n"
                                "    width:8px;\n"
                                "    background:rgba(0,0,0,50%);  \n"
                                "    border-radius:4px;\n"
                                "    min-height:20;\n"
                                "}\n"
                                "QScrollBar::add-line:vertical\n"
                                "{\n"
                                "    height:9px;width:8px;\n"
                                "    border-image:url(:/images/a/3.png);\n"
                                "    subcontrol-position:bottom;\n"
                                "}\n"
                                "QScrollBar::sub-line:vertical\n"
                                "{\n"
                                "    height:9px;width:8px;\n"
                                "    border-image:url(:/images/a/1.png);\n"
                                "    subcontrol-position:top;\n"
                                "}\n"
                                "QScrollBar::add-line:vertical:hover \n"
                                "{\n"
                                "    height:9px;width:8px;\n"
                                "    border-image:url(:/images/a/4.png);\n"
                                "    subcontrol-position:bottom;\n"
                                "}\n"
                                "QScrollBar::sub-line:vertical:hover\n"
                                "{\n"
                                "    height:9px;width:8px;\n"
                                "    border-image:url(:/images/a/2.png);\n"
                                "    subcontrol-position:top;\n"
                                "}\n"
                                "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
                                "{\n"
                                "    background:rgba(0,0,0,10%);\n"
                                "    border-radius:4px;\n"
                                "}")
        self.code.setObjectName("tableWidget_2")
        self.code.setColumnCount(4)
        self.code.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.code.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.code.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.code.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.code.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 31))
        self.label.setStyleSheet("font: 15pt \"黑体\"; \n"
                                 "color:rgb(255, 171, 25)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 510, 141, 31))
        self.label_2.setStyleSheet("font: 15pt \"黑体\"; \n"
                                   "color:rgb(255, 171, 25)")
        self.label_2.setObjectName("label_2")
        self.DAGcode = QtWidgets.QTableWidget(self.centralwidget)
        self.DAGcode.setGeometry(QtCore.QRect(530, 50, 761, 451))
        self.DAGcode.setStyleSheet("QHeaderView{\n"
                                   "              font-size: 19px;\n"
                                   "          border: 1px solid rgb(255, 255, 255);\n"
                                   "        background: rgb(100, 188, 238);\n"
                                   "          min-height:40px;\n"
                                   "           \n"
                                   "} \n"
                                   " \n"
                                   " \n"
                                   "QHeaderView::section:horizontal { \n"
                                   "        border: 1px solid rgb(255, 255, 255);\n"
                                   "          border-bottom: 0px;\n"
                                   "        color: rgb(2, 65, 132);\n"
                                   "        background: transparent;\n"
                                   "        padding-left: 2px;\n"
                                   "        min-width:60px;\n"
                                   "}\n"
                                   "QHeaderView::section:horizontal:hover {    \n"
                                   "        color: white;\n"
                                   "        background: rgb(11,82,202);\n"
                                   "}\n"
                                   "QHeaderView::section:horizontal:pressed {\n"
                                   "        color: white;\n"
                                   "        background: rgb(39,106,220);\n"
                                   "}\n"
                                   "QHeaderView::section:vertical { \n"
                                   "        border: 1px solid rgb(255, 255, 255);\n"
                                   "          border-bottom: 0px;\n"
                                   "        color: rgb(2, 65, 132);\n"
                                   "        background: rgb(255, 255, 255,180);\n"
                                   "        padding-top: 3px;\n"
                                   "        min-width:60px;\n"
                                   "        \n"
                                   "}\n"
                                   "QHeaderView::section:vertical:hover {\n"
                                   "        color: white;\n"
                                   "        background: rgb(11,82,202);    \n"
                                   "}\n"
                                   "QHeaderView::section:vertical:pressed {    \n"
                                   "        color: white;\n"
                                   "        background: rgb(39,106,220);\n"
                                   "}\n"
                                   " \n"
                                   " \n"
                                   "QHeaderView::up-arrow {\n"
                                   "        width: 13px;\n"
                                   "        height: 11px;\n"
                                   "        padding-right: 0px;\n"
                                   "        image: url(:/arrow_up.png);\n"
                                   "        subcontrol-position: center right;\n"
                                   "}\n"
                                   "QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
                                   "     \n"
                                   "}\n"
                                   "QHeaderView::down-arrow {\n"
                                   "        width: 13px;\n"
                                   "        height: 11px;\n"
                                   "        padding-right: 10px;\n"
                                   "        image: url(:/arrow_down.png);\n"
                                   "        subcontrol-position: center right;\n"
                                   "}\n"
                                   "QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
                                   "     \n"
                                   "}\n"
                                   "QTableWidget,QTableView {\n"
                                   "        font-size: 17px;\n"
                                   "        color : rgb(1,37,116);                \n"
                                   "        border: 2px solid rgb(100, 188, 238);        \n"
                                   "        background: rgb(248,248,248);\n"
                                   "        gridline-color: rgb(196,226,255);    \n"
                                   "        text-align: center;    \n"
                                   "        outline:0px;\n"
                                   "}\n"
                                   "QTableWidget::item,QTableView::item {    \n"
                                   "        padding-left: 5px;\n"
                                   "        padding-right: 5px;\n"
                                   "        border: none; \n"
                                   "        background: rgba(251,251,253,200);\n"
                                   "}\n"
                                   "QTableWidget::item:selected,QTableView::item:selected {\n"
                                   "        background: rgba(207,230,253,200);\n"
                                   "        color : rgb(1,37,116);                \n"
                                   "}\n"
                                   " \n"
                                   " \n"
                                   "QTableView::item:alternate:!selected,QTableWidget::item:alternate:!selected,QListView::item:alternate:!selected \n"
                                   "{ \n"
                                   "    background: rgb(250,250,250); \n"
                                   "}\n"
                                   " \n"
                                   "QTableView::item:!alternate:!selected,QTableWidget::item:!alternate:!selected\n"
                                   "{ \n"
                                   "    background: rgb(240,247,254); \n"
                                   "}\n"
                                   "QScrollBar:vertical\n"
                                   "{\n"
                                   "    width:8px;\n"
                                   "    background:rgba(0,0,0,0%);\n"
                                   "    margin:0px,0px,0px,0px;\n"
                                   "    padding-top:9px; \n"
                                   "    padding-bottom:9px;\n"
                                   "}\n"
                                   "QScrollBar::handle:vertical\n"
                                   "{\n"
                                   "    width:8px;\n"
                                   "    background:rgba(0,0,0,25%);\n"
                                   "    border-radius:4px; \n"
                                   "    min-height:20;\n"
                                   "}\n"
                                   "QScrollBar::handle:vertical:hover\n"
                                   "{\n"
                                   "    width:8px;\n"
                                   "    background:rgba(0,0,0,50%);  \n"
                                   "    border-radius:4px;\n"
                                   "    min-height:20;\n"
                                   "}\n"
                                   "QScrollBar::add-line:vertical\n"
                                   "{\n"
                                   "    height:9px;width:8px;\n"
                                   "    border-image:url(:/images/a/3.png);\n"
                                   "    subcontrol-position:bottom;\n"
                                   "}\n"
                                   "QScrollBar::sub-line:vertical\n"
                                   "{\n"
                                   "    height:9px;width:8px;\n"
                                   "    border-image:url(:/images/a/1.png);\n"
                                   "    subcontrol-position:top;\n"
                                   "}\n"
                                   "QScrollBar::add-line:vertical:hover \n"
                                   "{\n"
                                   "    height:9px;width:8px;\n"
                                   "    border-image:url(:/images/a/4.png);\n"
                                   "    subcontrol-position:bottom;\n"
                                   "}\n"
                                   "QScrollBar::sub-line:vertical:hover\n"
                                   "{\n"
                                   "    height:9px;width:8px;\n"
                                   "    border-image:url(:/images/a/2.png);\n"
                                   "    subcontrol-position:top;\n"
                                   "}\n"
                                   "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
                                   "{\n"
                                   "    background:rgba(0,0,0,10%);\n"
                                   "    border-radius:4px;\n"
                                   "}")
        self.DAGcode.setObjectName("DAGcode")
        self.DAGcode.setColumnCount(6)
        self.DAGcode.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DAGcode.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DAGcode.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DAGcode.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DAGcode.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.DAGcode.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.DAGcode.setHorizontalHeaderItem(5, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 10, 111, 31))
        self.label_3.setStyleSheet("font: 15pt \"黑体\"; \n"
                                   "color:rgb(255, 171, 25)")
        self.label_3.setObjectName("label_3")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(530, 520, 760, 500))
        self.result.setText("")
        self.result.setObjectName("result")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 510, 120, 30))
        self.label_4.setStyleSheet("font: 15pt \"黑体\"; \n"
                                   "color:rgb(255, 171, 25)")
        self.label_4.setObjectName("label_4")
        self.gin = QtWidgets.QPushButton(self.centralwidget)
        self.gin.setGeometry(QtCore.QRect(1100, 10, 93, 28))
        self.gin.setStyleSheet("QPushButton\n"
                               "{\n"
                               "    color:white;\n"
                               "    background-color:rgb(14 , 150 , 254);\n"
                               "    border-radius:5px;\n"
                               "    font:15px \"微软雅黑\";\n"
                               "}\n"
                               "\n"
                               "::hover\n"
                               "{\n"
                               "    color:white;\n"
                               "    background-color:rgb(44 , 137 , 255);\n"
                               "}\n"
                               "\n"
                               "::pressed\n"
                               "{\n"
                               "    color:white;\n"
                               "    background-color:rgb(14 , 135 , 228);\n"
                               "    padding-left:3px;\n"
                               "    padding-top:3px;\n"
                               "}")
        self.gin.setObjectName("in")
        self.gstart = QtWidgets.QPushButton(self.centralwidget)
        self.gstart.setGeometry(QtCore.QRect(1200, 10, 93, 28))
        self.gstart.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "    color:white;\n"
                                  "    background-color:rgb(14 , 150 , 254);\n"
                                  "    border-radius:5px;\n"
                                  "    font:15px \"微软雅黑\";\n"
                                  "}\n"
                                  "\n"
                                  "::hover\n"
                                  "{\n"
                                  "    color:white;\n"
                                  "    background-color:rgb(44 , 137 , 255);\n"
                                  "}\n"
                                  "\n"
                                  "::pressed\n"
                                  "{\n"
                                  "    color:white;\n"
                                  "    background-color:rgb(14 , 135 , 228);\n"
                                  "    padding-left:3px;\n"
                                  "    padding-top:3px;\n"
                                  "}")
        self.gstart.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(670, 10, 421, 31))
        self.lineEdit.setStyleSheet("background:white;\n"
                                    "    padding-left:5px ;\n"
                                    "    padding-top:1px ;\n"
                                    "    border-bottom-left-radius:3px;\n"
                                    "    border-bottom-right-radius:3px;\n"
                                    "    border: 1px solid rgb(209 , 209 , 209);\n"
                                    "    border-top:transparent;")
        self.lineEdit.setObjectName("lineEdit")
        self.code_r.verticalHeader().setVisible(False)
        self.code.verticalHeader().setVisible(False)
        self.DAGcode.verticalHeader().setVisible(False)
        self.code.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.code_r.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.DAGcode.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.code.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.code_r.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.DAGcode.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        forkeshe.setCentralWidget(self.centralwidget)
        self.retranslateUi(forkeshe)
        QtCore.QMetaObject.connectSlotsByName(forkeshe)
        self.gstart.clicked.connect(lambda: self.StartRun(forkeshe))
        self.gin.clicked.connect(lambda: self.ReadIn(forkeshe))

    def retranslateUi(self, forkeshe):
        _translate = QtCore.QCoreApplication.translate
        forkeshe.setWindowTitle(_translate("forkeshe", "MainWindow"))
        item = self.code_r.horizontalHeaderItem(0)
        item.setText(_translate("forkeshe", "code[0]"))
        item = self.code_r.horizontalHeaderItem(1)
        item.setText(_translate("forkeshe", "code[1]"))
        item = self.code_r.horizontalHeaderItem(2)
        item.setText(_translate("forkeshe", "code[2]"))
        item = self.code_r.horizontalHeaderItem(3)
        item.setText(_translate("forkeshe", "code[3]"))
        item = self.code.horizontalHeaderItem(0)
        item.setText(_translate("forkeshe", "code[0]"))
        item = self.code.horizontalHeaderItem(1)
        item.setText(_translate("forkeshe", "code[1]"))
        item = self.code.horizontalHeaderItem(2)
        item.setText(_translate("forkeshe", "code[2]"))
        item = self.code.horizontalHeaderItem(3)
        item.setText(_translate("forkeshe", "code[3]"))
        self.label.setText(_translate("forkeshe", "优化前代码"))
        self.label_2.setText(_translate("forkeshe", "优化后代码"))
        item = self.DAGcode.horizontalHeaderItem(0)
        item.setText(_translate("forkeshe", "num"))
        item = self.DAGcode.horizontalHeaderItem(1)
        item.setText(_translate("forkeshe", "sign"))
        item = self.DAGcode.horizontalHeaderItem(2)
        item.setText(_translate("forkeshe", "affi_sign"))
        item = self.DAGcode.horizontalHeaderItem(3)
        item.setText(_translate("forkeshe", "son"))
        item = self.DAGcode.horizontalHeaderItem(4)
        item.setText(_translate("forkeshe", "left"))
        item = self.DAGcode.horizontalHeaderItem(5)
        item.setText(_translate("forkeshe", "right"))
        self.label_3.setText(_translate("forkeshe", "DAG代码"))
        self.label_4.setText(_translate("forkeshe", "DAG可视化"))
        self.gin.setText(_translate("forkeshe", "导  入"))
        self.gstart.setText(_translate("forkeshe", "运  行"))

    def ReadIn(self, forkeshe):
        if os.path.exists(self.lineEdit.text()) is False:
            QMessageBox.critical(forkeshe, "错误", "文件路径错误！",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        intext = open(self.lineEdit.text()).read()
        self.res, flag = transfer(intext)
        if flag:
            self.code_r.setColumnCount(4)
            self.code_r.setRowCount(len(self.res))
            for i in range(len(self.res)):
                self.code_r.setItem(i, 0, QTableWidgetItem(self.res[i][0]))
                self.code_r.setItem(i, 1, QTableWidgetItem(self.res[i][1]))
                self.code_r.setItem(i, 2, QTableWidgetItem(self.res[i][2]))
                self.code_r.setItem(i, 3, QTableWidgetItem(self.res[i][3]))
        else:
            QMessageBox.critical(forkeshe, "错误", "文件格式错误！",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return

    def StartRun(self, forkeshe):
        if len(self.res) == 0:
            QMessageBox.critical(forkeshe, "错误", "请先读入文件！",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        dagcode, daginfo = startrun(self.res)
        res_dagcode = ''
        res_daginfo = ''
        self.code.setColumnCount(4)
        self.code.setRowCount(len(daginfo))
        for i in range(len(daginfo)):
            self.code.setItem(i, 0, QTableWidgetItem(daginfo[i][0]))
            self.code.setItem(i, 1, QTableWidgetItem(daginfo[i][1]))
            self.code.setItem(i, 2, QTableWidgetItem(daginfo[i][2]))
            self.code.setItem(i, 3, QTableWidgetItem(daginfo[i][3]))
            res_daginfo += daginfo[i][0] + ', ' + daginfo[i][1] + ', ' + daginfo[i][2] + ', ' + daginfo[i][3] + '\n'
        self.DAGcode.setColumnCount(6)
        self.DAGcode.setRowCount(len(dagcode))
        for i in range(len(dagcode)):
            self.DAGcode.setItem(i, 0, QTableWidgetItem(str(i)))
            self.DAGcode.setItem(i, 1, QTableWidgetItem(dagcode[i]['sign']))
            res_dagcode += str(i) + ', sigh:' + dagcode[i]['sign']
            affisignn = ""
            for j in dagcode[i]['affi_sign']:
                affisignn += j
            if affisignn == "":
                res_dagcode += ', affi_sign:none'
            else:
                res_dagcode += ', affi_sign:' + affisignn
            self.DAGcode.setItem(i, 2, QTableWidgetItem(affisignn))
            if 'son' in dagcode[i]:
                self.DAGcode.setItem(i, 3, QTableWidgetItem(dagcode[i]['son']))
                self.DAGcode.setItem(i, 4, QTableWidgetItem("-"))
                self.DAGcode.setItem(i, 5, QTableWidgetItem("-"))
                res_dagcode += ', son:' + str(dagcode[i]['son'])
            elif 'left' in dagcode[i] and 'right' in dagcode[i]:
                self.DAGcode.setItem(i, 3, QTableWidgetItem("-"))
                self.DAGcode.setItem(i, 4, QTableWidgetItem(str(dagcode[i]['left'])))
                self.DAGcode.setItem(i, 5, QTableWidgetItem(str(dagcode[i]['right'])))
                res_dagcode += ', left:' + str(dagcode[i]['left']) + ', right:' + str(dagcode[i]['right'])
            else:
                self.DAGcode.setItem(i, 3, QTableWidgetItem("-"))
                self.DAGcode.setItem(i, 4, QTableWidgetItem("-"))
                self.DAGcode.setItem(i, 5, QTableWidgetItem("-"))
            res_dagcode += '\n'
        print("================================")
        print("DAGcode:")
        print(res_dagcode)
        print("================================")
        print("DAGinfo:")
        print(res_daginfo)
        print("================================")
        f_dagcode = open("daggode.txt", 'w')
        f_daginfo = open("daginfo.txt", 'w')
        f_dagcode.write(res_dagcode)
        f_daginfo.write(res_daginfo)
        f_dagcode.close()
        f_daginfo.close()
        img_path = 'result.png'
        showImage = QPixmap(img_path).scaled(self.result.width(), self.result.height())
        self.result.setPixmap(showImage)


def go():
    app = QtWidgets.QApplication(sys.argv)
    aw = Ui_forkeshe()
    w = QtWidgets.QMainWindow()
    aw.setupUi(w)
    w.setWindowTitle("何煦-编译原理课设")
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    go()
