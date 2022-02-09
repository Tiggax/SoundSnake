# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designervPOUqJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BookItem(object):
    def setupUi(self, BookItem):
        if not BookItem.objectName():
            BookItem.setObjectName(u"BookItem")
        BookItem.resize(600, 64)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BookItem.sizePolicy().hasHeightForWidth())
        BookItem.setSizePolicy(sizePolicy)
        BookItem.setMinimumSize(QSize(600, 64))
        BookItem.setMaximumSize(QSize(600, 64))
        self.AuthorLabel = QLabel(BookItem)
        self.AuthorLabel.setObjectName(u"AuthorLabel")
        self.AuthorLabel.setGeometry(QRect(70, 40, 200, 20))
        sizePolicy.setHeightForWidth(self.AuthorLabel.sizePolicy().hasHeightForWidth())
        self.AuthorLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.AuthorLabel.setFont(font)
        self.BookTitle = QLabel(BookItem)
        self.BookTitle.setObjectName(u"BookTitle")
        self.BookTitle.setGeometry(QRect(70, 10, 300, 30))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.BookTitle.setFont(font1)
        self.BookPicture = QGraphicsView(BookItem)
        self.BookPicture.setObjectName(u"BookPicture")
        self.BookPicture.setGeometry(QRect(0, 0, 64, 64))
        self.StatusField = QWidget(BookItem)
        self.StatusField.setObjectName(u"StatusField")
        self.StatusField.setGeometry(QRect(370, 10, 220, 50))
        self.StatusField.setStyleSheet(u"")

        self.retranslateUi(BookItem)

        QMetaObject.connectSlotsByName(BookItem)
    # setupUi

    def retranslateUi(self, BookItem):
        BookItem.setWindowTitle(QCoreApplication.translate("BookItem", u"Form", None))
        self.AuthorLabel.setText(QCoreApplication.translate("BookItem", u"Max Mathias Shoperenehager", None))
        self.BookTitle.setText(QCoreApplication.translate("BookItem", u"Die Erster Nihtklasskundeklaver im Mittnah", None))
    # retranslateUi

