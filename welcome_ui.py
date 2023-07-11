# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_qusPage(object):
    def setupUi(self, qusPage):
        if not qusPage.objectName():
            qusPage.setObjectName(u"qusPage")
        qusPage.resize(1175, 749)
        qusPage.setStyleSheet(u"QWidget {\n"
"	background: rgb(42, 42, 42);\n"
"}")
        self.qusLabel = QLabel(qusPage)
        self.qusLabel.setObjectName(u"qusLabel")
        self.qusLabel.setGeometry(QRect(350, 30, 491, 131))
        self.qusLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 29px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.qusLabel.setTextFormat(Qt.AutoText)
        self.qusLabel.setScaledContents(False)
        self.qusLabel.setAlignment(Qt.AlignCenter)
        self.qusLabel.setWordWrap(True)
        self.utc2dButton = QPushButton(qusPage)
        self.utc2dButton.setObjectName(u"utc2dButton")
        self.utc2dButton.setGeometry(QRect(380, 220, 421, 51))
        self.utc2dButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.utc3dButton = QPushButton(qusPage)
        self.utc3dButton.setObjectName(u"utc3dButton")
        self.utc3dButton.setGeometry(QRect(380, 330, 421, 51))
        self.utc3dButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.ceus2dButton = QPushButton(qusPage)
        self.ceus2dButton.setObjectName(u"ceus2dButton")
        self.ceus2dButton.setGeometry(QRect(380, 440, 421, 51))
        self.ceus2dButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.ceus3dButton = QPushButton(qusPage)
        self.ceus3dButton.setObjectName(u"ceus3dButton")
        self.ceus3dButton.setGeometry(QRect(380, 550, 421, 51))
        self.ceus3dButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")

        self.retranslateUi(qusPage)

        QMetaObject.connectSlotsByName(qusPage)
    # setupUi

    def retranslateUi(self, qusPage):
        qusPage.setWindowTitle(QCoreApplication.translate("qusPage", u"QUS Tools", None))
        self.qusLabel.setText(QCoreApplication.translate("qusPage", u"Quantitative Ultrasound (QUS) Tools:", None))
#if QT_CONFIG(tooltip)
        self.utc2dButton.setToolTip(QCoreApplication.translate("qusPage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.utc2dButton.setText(QCoreApplication.translate("qusPage", u"2D Ultrasound Tissue Characterization (UTC)", None))
#if QT_CONFIG(tooltip)
        self.utc3dButton.setToolTip(QCoreApplication.translate("qusPage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.utc3dButton.setText(QCoreApplication.translate("qusPage", u"3D Ultrasound Tissue Characterization (UTC)", None))
#if QT_CONFIG(tooltip)
        self.ceus2dButton.setToolTip(QCoreApplication.translate("qusPage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ceus2dButton.setText(QCoreApplication.translate("qusPage", u"2D Contrast-Enhanced Ultrasound (CEUS)", None))
#if QT_CONFIG(tooltip)
        self.ceus3dButton.setToolTip(QCoreApplication.translate("qusPage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ceus3dButton.setText(QCoreApplication.translate("qusPage", u"3D Contrast-Enhanced Ultrasound (CEUS)", None))
    # retranslateUi

