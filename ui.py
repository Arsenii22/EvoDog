# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 399)
        icon = QIcon()
        icon.addFile(u"logo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLabel {\n"
"	font: 10pt \"Franklin Gothic Medium\";\n"
"}\n"
"\n"
"QScrollArea QWidget {\n"
"	background-color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 600, 400))
        self.newDog = QWidget()
        self.newDog.setObjectName(u"newDog")
        self.newDog.setStyleSheet(u"QPushButton {\n"
"    background-color: #4BA641;\n"
"    width: 100px;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"	font-size: 17px;\n"
"}\n"
"\n"
"QLabel[objectName=title] {\n"
"	font-size: 30px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QFrame[objectName=borderFrame] {\n"
"border: 1px solid black;\n"
"border-radius: 20%;\n"
"}")
        self.submit = QPushButton(self.newDog)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(220, 320, 160, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)
        self.title = QLabel(self.newDog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 0, 571, 61))
        self.title.setAlignment(Qt.AlignCenter)
        self.borderFrame = QFrame(self.newDog)
        self.borderFrame.setObjectName(u"borderFrame")
        self.borderFrame.setGeometry(QRect(10, 70, 571, 231))
        self.borderFrame.setFrameShape(QFrame.StyledPanel)
        self.borderFrame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.borderFrame)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 0, 551, 211))
        self.data_2 = QGridLayout(self.gridLayoutWidget_2)
        self.data_2.setSpacing(15)
        self.data_2.setObjectName(u"data_2")
        self.data_2.setContentsMargins(0, 0, 0, 0)
        self.third = QVBoxLayout()
        self.third.setObjectName(u"third")
        self.label_third = QLabel(self.gridLayoutWidget_2)
        self.label_third.setObjectName(u"label_third")
        self.label_third.setAlignment(Qt.AlignCenter)

        self.third.addWidget(self.label_third)

        self.spinBox_third = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_third.setObjectName(u"spinBox_third")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBox_third.sizePolicy().hasHeightForWidth())
        self.spinBox_third.setSizePolicy(sizePolicy1)
        self.spinBox_third.setMaximum(1000)

        self.third.addWidget(self.spinBox_third)


        self.data_2.addLayout(self.third, 2, 1, 1, 1)

        self.first = QVBoxLayout()
        self.first.setObjectName(u"first")
        self.label_first = QLabel(self.gridLayoutWidget_2)
        self.label_first.setObjectName(u"label_first")
        self.label_first.setAlignment(Qt.AlignCenter)

        self.first.addWidget(self.label_first)

        self.spinBox_first = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_first.setObjectName(u"spinBox_first")
        sizePolicy1.setHeightForWidth(self.spinBox_first.sizePolicy().hasHeightForWidth())
        self.spinBox_first.setSizePolicy(sizePolicy1)
        self.spinBox_first.setMaximum(1000)

        self.first.addWidget(self.spinBox_first)


        self.data_2.addLayout(self.first, 0, 1, 1, 1)

        self.fourth = QVBoxLayout()
        self.fourth.setObjectName(u"fourth")
        self.label_fourth = QLabel(self.gridLayoutWidget_2)
        self.label_fourth.setObjectName(u"label_fourth")
        self.label_fourth.setAlignment(Qt.AlignCenter)

        self.fourth.addWidget(self.label_fourth)

        self.spinBox_fourth = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_fourth.setObjectName(u"spinBox_fourth")
        sizePolicy1.setHeightForWidth(self.spinBox_fourth.sizePolicy().hasHeightForWidth())
        self.spinBox_fourth.setSizePolicy(sizePolicy1)
        self.spinBox_fourth.setMaximum(1000)

        self.fourth.addWidget(self.spinBox_fourth)


        self.data_2.addLayout(self.fourth, 2, 2, 1, 1)

        self.second = QVBoxLayout()
        self.second.setObjectName(u"second")
        self.label_second = QLabel(self.gridLayoutWidget_2)
        self.label_second.setObjectName(u"label_second")
        self.label_second.setAlignment(Qt.AlignCenter)

        self.second.addWidget(self.label_second)

        self.spinBox_second = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_second.setObjectName(u"spinBox_second")
        sizePolicy1.setHeightForWidth(self.spinBox_second.sizePolicy().hasHeightForWidth())
        self.spinBox_second.setSizePolicy(sizePolicy1)
        self.spinBox_second.setMaximum(1000)

        self.second.addWidget(self.spinBox_second)


        self.data_2.addLayout(self.second, 0, 2, 1, 1)

        self.tabWidget.addTab(self.newDog, "")
        self.newDogByParents = QWidget()
        self.newDogByParents.setObjectName(u"newDogByParents")
        self.newDogByParents.setStyleSheet(u"QPushButton {\n"
"    background-color: #4BA641;\n"
"    width: 100px;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"  font-size: 17px;\n"
"}\n"
"\n"
"QLabel[objectName=title] {\n"
"  font-size: 28px;\n"
"}\n"
"\n"
"QLabel {\n"
"  font-size: 20px;\n"
"}\n"
"\n"
"QFrame[objectName=borderFrame], QFrame[objectName=borderFrame_2] {\n"
"	border: 1px solid black;\n"
"	border-radius: 20%;\n"
"}")
        self.submit_2 = QPushButton(self.newDogByParents)
        self.submit_2.setObjectName(u"submit_2")
        self.submit_2.setGeometry(QRect(210, 320, 170, 40))
        sizePolicy.setHeightForWidth(self.submit_2.sizePolicy().hasHeightForWidth())
        self.submit_2.setSizePolicy(sizePolicy)
        self.title1 = QLabel(self.newDogByParents)
        self.title1.setObjectName(u"title1")
        self.title1.setGeometry(QRect(10, 0, 571, 61))
#if QT_CONFIG(whatsthis)
        self.title1.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.title1.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.newDogByParents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 70, 281, 221))
        self.males = QScrollArea(self.groupBox)
        self.males.setObjectName(u"males")
        self.males.setGeometry(QRect(10, 20, 261, 191))
        self.males.setWidgetResizable(True)
        self.males_content = QWidget()
        self.males_content.setObjectName(u"males_content")
        self.males_content.setGeometry(QRect(0, 0, 259, 189))
        self.males_list = QListWidget(self.males_content)
        self.males_list.setObjectName(u"males_list")
        self.males_list.setGeometry(QRect(0, 0, 261, 192))
        self.males.setWidget(self.males_content)
        self.groupBox_2 = QGroupBox(self.newDogByParents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(310, 70, 271, 221))
        self.females = QScrollArea(self.groupBox_2)
        self.females.setObjectName(u"females")
        self.females.setGeometry(QRect(10, 20, 251, 191))
        self.females.setWidgetResizable(True)
        self.females_content = QWidget()
        self.females_content.setObjectName(u"females_content")
        self.females_content.setGeometry(QRect(0, 0, 249, 189))
        self.females_list = QListWidget(self.females_content)
        self.females_list.setObjectName(u"females_list")
        self.females_list.setGeometry(QRect(0, 0, 251, 192))
        self.females.setWidget(self.females_content)
        self.tabWidget.addTab(self.newDogByParents, "")
        self.myDogs = QWidget()
        self.myDogs.setObjectName(u"myDogs")
        self.myDogs.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-color: transparent;\n"
"    outline: none;\n"
"	font-size: 15px;\n"
"}")
        self.dogs_list = QListWidget(self.myDogs)
        self.dogs_list.setObjectName(u"dogs_list")
        self.dogs_list.setGeometry(QRect(0, 0, 591, 371))
        self.dogs_list.setStyleSheet(u"")
        self.tabWidget.addTab(self.myDogs, "")

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EvoDog", None))
        self.submit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u043f\u043e\u0440\u043e\u0434\u0443", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u0435\u0434\u0438 \u0441\u0432\u043e\u044e \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0443\u044e \u043f\u043e\u0440\u043e\u0434\u0443!", None))
        self.label_third.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0445\u0432\u043e\u0441\u0442\u0430", None))
        self.label_first.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0440\u043e\u0442\u0430 \u0441\u043b\u0443\u0445\u0430", None))
        self.label_fourth.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u0442\u0443\u043b\u043e\u0432\u0438\u0449\u0430", None))
        self.label_second.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u0448\u0435\u0440\u0441\u0442\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.newDog), QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u043f\u043e\u0440\u043e\u0434\u0443", None))
        self.submit_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0449\u0435\u043d\u043a\u0430", None))
        self.title1.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u043d\u0430\u0439, \u043a\u0430\u043a\u0430\u044f \u0431\u0443\u0434\u0435\u0442 \u0441\u043e\u0431\u0430\u043a\u0430 \u043e\u0442 \u0435\u0451 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043e\u0431\u044c 1", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043e\u0431\u044c 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.newDogByParents), QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u043f\u043e\u0440\u043e\u0434\u0443 \u043f\u043e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f\u043c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.myDogs), QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0438 \u0441\u043e\u0431\u0430\u043a\u0438", None))
    # retranslateUi

