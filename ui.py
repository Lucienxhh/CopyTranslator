# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import QMetaObject, QRect, QCoreApplication
from PySide2.QtWidgets import QGridLayout, QScrollArea, QWidget, QTextEdit
from PySide2.QtGui import QFont


class Ui_Dialog(object):
    def changeText(self, srcText, destText):
        self.srcText.setText(srcText)
        self.destText.setText(destText)
    

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(532, 523)
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.srcArea = QScrollArea(Dialog)
        self.srcArea.setObjectName(u"srcArea")
        self.srcArea.setWidgetResizable(True)
        self.scrScroll = QWidget()
        self.scrScroll.setObjectName(u"scrScroll")
        self.scrScroll.setGeometry(QRect(0, 0, 512, 248))
        self.gridLayout_2 = QGridLayout(self.scrScroll)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.srcText = QTextEdit(self.scrScroll)
        self.srcText.setObjectName(u"srcText")
        font = QFont()
        font.setPointSize(12)
        self.srcText.setFont(font)

        self.gridLayout_2.addWidget(self.srcText, 0, 0, 1, 1)

        self.srcArea.setWidget(self.scrScroll)

        self.gridLayout_3.addWidget(self.srcArea, 0, 0, 1, 1)

        self.destArea = QScrollArea(Dialog)
        self.destArea.setObjectName(u"destArea")
        self.destArea.setWidgetResizable(True)
        self.destScroll = QWidget()
        self.destScroll.setObjectName(u"destScroll")
        self.destScroll.setGeometry(QRect(0, 0, 512, 247))
        self.gridLayout = QGridLayout(self.destScroll)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.destText = QTextEdit(self.destScroll)
        self.destText.setObjectName(u"destText")
        self.destText.setFont(font)
        self.destText.setLineWidth(1)

        self.gridLayout.addWidget(self.destText, 0, 0, 1, 1)

        self.destArea.setWidget(self.destScroll)

        self.gridLayout_3.addWidget(self.destArea, 1, 0, 1, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Xyh's CopyTranslator", None))
        self.srcText.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">loading...</p></body></html>", None))
    # retranslateUi

