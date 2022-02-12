# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_browsersXZiLa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide6.QtCore import *
# from PySide6.QtGui import *
# from PySide6.QtWidgets import *

# from PySide6.QtWebEngineWidgets import QWebEngineView
from qt_core import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(860, 600)
        Form.setMinimumSize(QSize(860, 600))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.webEngineView = QWebEngineView(Form)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setMinimumSize(QSize(840, 580))
        self.webEngineView.setUrl(QUrl(u"https://www.audible.de/"))

        self.gridLayout.addWidget(self.webEngineView, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.HomeBtn = QPushButton(Form)
        self.HomeBtn.setObjectName(u"HomeBtn")

        self.horizontalLayout_2.addWidget(self.HomeBtn)

        self.BackBtn = QPushButton(Form)
        self.BackBtn.setObjectName(u"BackBtn")

        self.horizontalLayout_2.addWidget(self.BackBtn)

        self.ForwardBtn = QPushButton(Form)
        self.ForwardBtn.setObjectName(u"ForwardBtn")

        self.horizontalLayout_2.addWidget(self.ForwardBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.ForwardBtn.pressed.connect(self.webEngineView.forward)
        self.BackBtn.pressed.connect(self.webEngineView.back)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.HomeBtn.setText(QCoreApplication.translate("Form", u"Home", None))
        self.BackBtn.setText(QCoreApplication.translate("Form", u"<-", None))
        self.ForwardBtn.setText(QCoreApplication.translate("Form", u"->", None))
    # retranslateUi


