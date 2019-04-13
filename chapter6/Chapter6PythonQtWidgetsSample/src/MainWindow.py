# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui',
# licensing of 'ui/mainwindow.ui' applies.
#
# Created: Sun Apr 14 08:11:35 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 394)
        MainWindow.setMinimumSize(QtCore.QSize(400, 350))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(400, 350))
        self.centralWidget.setMaximumSize(QtCore.QSize(400, 350))
        self.centralWidget.setObjectName("centralWidget")
        self.widgetJudge = QtWidgets.QWidget(self.centralWidget)
        self.widgetJudge.setEnabled(True)
        self.widgetJudge.setGeometry(QtCore.QRect(10, 40, 380, 220))
        self.widgetJudge.setStyleSheet("background: transparent;")
        self.widgetJudge.setObjectName("widgetJudge")
        self.graphicsViewjudge = QtWidgets.QGraphicsView(self.widgetJudge)
        self.graphicsViewjudge.setGeometry(QtCore.QRect(0, 0, 381, 251))
        self.graphicsViewjudge.setStyleSheet("background: transparent;")
        self.graphicsViewjudge.setObjectName("graphicsViewjudge")
        self.labelJudge = QtWidgets.QLabel(self.widgetJudge)
        self.labelJudge.setGeometry(QtCore.QRect(106, 100, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelJudge.setFont(font)
        self.labelJudge.setText("")
        self.labelJudge.setAlignment(QtCore.Qt.AlignCenter)
        self.labelJudge.setObjectName("labelJudge")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 382, 330))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutComboBOx = QtWidgets.QHBoxLayout()
        self.horizontalLayoutComboBOx.setObjectName("horizontalLayoutComboBOx")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutComboBOx.addItem(spacerItem)
        self.comboBoxLanguage = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxLanguage.setObjectName("comboBoxLanguage")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.horizontalLayoutComboBOx.addWidget(self.comboBoxLanguage)
        self.verticalLayout.addLayout(self.horizontalLayoutComboBOx)
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(380, 190))
        self.graphicsView.setMaximumSize(QtCore.QSize(380, 190))
        self.graphicsView.setStyleSheet("background: transparent;")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        spacerItem1 = QtWidgets.QSpacerItem(377, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.labelQuestion = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelQuestion.setFont(font)
        self.labelQuestion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuestion.setObjectName("labelQuestion")
        self.verticalLayout.addWidget(self.labelQuestion)
        self.horizontalLayoutButton = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButton.setObjectName("horizontalLayoutButton")
        self.pushButtonMelon = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonMelon.setFont(font)
        self.pushButtonMelon.setObjectName("pushButtonMelon")
        self.horizontalLayoutButton.addWidget(self.pushButtonMelon)
        self.pushButtonApple = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonApple.setFont(font)
        self.pushButtonApple.setObjectName("pushButtonApple")
        self.horizontalLayoutButton.addWidget(self.pushButtonApple)
        self.pushButtonStrawbery = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonStrawbery.setFont(font)
        self.pushButtonStrawbery.setObjectName("pushButtonStrawbery")
        self.horizontalLayoutButton.addWidget(self.pushButtonStrawbery)
        self.verticalLayout.addLayout(self.horizontalLayoutButton)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtWidgets.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menuBar)
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.menu_File.addAction(self.action_Quit)
        self.menuBar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Fruits Quiz", None, -1))
        self.comboBoxLanguage.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "English", None, -1))
        self.comboBoxLanguage.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "German", None, -1))
        self.comboBoxLanguage.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Japanese", None, -1))
        self.comboBoxLanguage.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Chinese", None, -1))
        self.labelQuestion.setText(QtWidgets.QApplication.translate("MainWindow", "What\'s is this?", None, -1))
        self.pushButtonMelon.setText(QtWidgets.QApplication.translate("MainWindow", "Melon", None, -1))
        self.pushButtonApple.setText(QtWidgets.QApplication.translate("MainWindow", "Apple", None, -1))
        self.pushButtonStrawbery.setText(QtWidgets.QApplication.translate("MainWindow", "Strawberry", None, -1))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.action_Quit.setText(QtWidgets.QApplication.translate("MainWindow", "E&xit", None, -1))

