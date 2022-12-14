# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 906)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.SaveParametersFrame = QtWidgets.QFrame(self.centralWidget)
        self.SaveParametersFrame.setGeometry(QtCore.QRect(330, 680, 371, 181))
        self.SaveParametersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SaveParametersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SaveParametersFrame.setObjectName("SaveParametersFrame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.SaveParametersFrame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 351, 131))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.saveParametersHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveParametersHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.saveParametersHorizontalLayout.setObjectName("saveParametersHorizontalLayout")
        self.compareFrame = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.compareFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.compareFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.compareFrame.setObjectName("compareFrame")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.compareFrame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 112, 129))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.compareVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.compareVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.compareVerticalLayout.setObjectName("compareVerticalLayout")
        self.comparePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.comparePushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.comparePushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comparePushButton.setObjectName("comparePushButton")
        self.compareVerticalLayout.addWidget(self.comparePushButton)
        self.compareLitePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.compareLitePushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.compareLitePushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.compareLitePushButton.setObjectName("compareLitePushButton")
        self.compareVerticalLayout.addWidget(self.compareLitePushButton)
        self.saveParametersHorizontalLayout.addWidget(self.compareFrame)
        self.saveFrame = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.saveFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.saveFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.saveFrame.setObjectName("saveFrame")
        self.savePushButton = QtWidgets.QPushButton(self.saveFrame)
        self.savePushButton.setGeometry(QtCore.QRect(1, 20, 111, 90))
        self.savePushButton.setMinimumSize(QtCore.QSize(0, 80))
        self.savePushButton.setObjectName("savePushButton")
        self.saveParametersHorizontalLayout.addWidget(self.saveFrame)
        self.saveAsFrame = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.saveAsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.saveAsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.saveAsFrame.setObjectName("saveAsFrame")
        self.saveAsLabel = QtWidgets.QLabel(self.saveAsFrame)
        self.saveAsLabel.setGeometry(QtCore.QRect(0, 0, 110, 17))
        self.saveAsLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.saveAsLabel.setObjectName("saveAsLabel")
        self.layoutWidget = QtWidgets.QWidget(self.saveAsFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 112, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.saveAsVerticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.saveAsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.saveAsVerticalLayout.setObjectName("saveAsVerticalLayout")
        self.textRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.textRadioButton.setObjectName("textRadioButton")
        self.saveAsVerticalLayout.addWidget(self.textRadioButton)
        self.tableRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.tableRadioButton.setObjectName("tableRadioButton")
        self.saveAsVerticalLayout.addWidget(self.tableRadioButton)
        self.graphRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.graphRadioButton.setObjectName("graphRadioButton")
        self.saveAsVerticalLayout.addWidget(self.graphRadioButton)
        self.saveParametersHorizontalLayout.addWidget(self.saveAsFrame)
        self.gridLayoutWidget = QtWidgets.QWidget(self.SaveParametersFrame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 25))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.PFGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.PFGridLayout.setContentsMargins(0, 0, 0, 0)
        self.PFGridLayout.setObjectName("PFGridLayout")
        self.planRadioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.planRadioButton.setObjectName("planRadioButton")
        self.PFGridLayout.addWidget(self.planRadioButton, 0, 2, 1, 1)
        self.factRadioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.factRadioButton.setObjectName("factRadioButton")
        self.PFGridLayout.addWidget(self.factRadioButton, 0, 3, 1, 1)
        self.planFactLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.planFactLabel.setObjectName("planFactLabel")
        self.PFGridLayout.addWidget(self.planFactLabel, 0, 1, 1, 1)
        self.PeriodFrame = QtWidgets.QFrame(self.centralWidget)
        self.PeriodFrame.setGeometry(QtCore.QRect(10, 10, 401, 115))
        self.PeriodFrame.setMinimumSize(QtCore.QSize(0, 115))
        self.PeriodFrame.setMaximumSize(QtCore.QSize(16777215, 115))
        self.PeriodFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PeriodFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PeriodFrame.setObjectName("PeriodFrame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.PeriodFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.periodVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.periodVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.periodVerticalLayout.setObjectName("periodVerticalLayout")
        self.headerFrame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.headerFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.headerFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.headerFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 399, 27))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.buttonHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonHorizontalLayout.setObjectName("buttonHorizontalLayout")
        self.oneYearButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.oneYearButton.setStyleSheet("")
        self.oneYearButton.setObjectName("oneYearButton")
        self.buttonHorizontalLayout.addWidget(self.oneYearButton)
        self.yearPeriodButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.yearPeriodButton.setObjectName("yearPeriodButton")
        self.buttonHorizontalLayout.addWidget(self.yearPeriodButton)
        self.headerLabel = QtWidgets.QLabel(self.headerFrame)
        self.headerLabel.setGeometry(QtCore.QRect(0, 0, 399, 16))
        self.headerLabel.setObjectName("headerLabel")
        self.periodVerticalLayout.addWidget(self.headerFrame)
        self.periodLayout = QtWidgets.QVBoxLayout()
        self.periodLayout.setObjectName("periodLayout")
        self.periodHorizontalLayout = QtWidgets.QHBoxLayout()
        self.periodHorizontalLayout.setObjectName("periodHorizontalLayout")
        self.fromLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.fromLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.fromLabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.fromLabel.setBaseSize(QtCore.QSize(0, 0))
        self.fromLabel.setStyleSheet("")
        self.fromLabel.setObjectName("fromLabel")
        self.periodHorizontalLayout.addWidget(self.fromLabel)
        self.fromComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.fromComboBox.setObjectName("fromComboBox")
        self.periodHorizontalLayout.addWidget(self.fromComboBox)
        self.toLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.toLabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.toLabel.setObjectName("toLabel")
        self.periodHorizontalLayout.addWidget(self.toLabel)
        self.toComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.toComboBox.setObjectName("toComboBox")
        self.periodHorizontalLayout.addWidget(self.toComboBox)
        self.periodLayout.addLayout(self.periodHorizontalLayout)
        self.periodVerticalLayout.addLayout(self.periodLayout)
        self.oneYearComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.oneYearComboBox.setStyleSheet("")
        self.oneYearComboBox.setObjectName("oneYearComboBox")
        self.periodVerticalLayout.addWidget(self.oneYearComboBox)
        self.footerLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.footerLabel.setObjectName("footerLabel")
        self.periodVerticalLayout.addWidget(self.footerLabel)
        self.DBInfoFrame = QtWidgets.QFrame(self.centralWidget)
        self.DBInfoFrame.setGeometry(QtCore.QRect(640, 10, 371, 111))
        self.DBInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DBInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DBInfoFrame.setObjectName("DBInfoFrame")
        self.updateDataInfoLabel = QtWidgets.QLabel(self.DBInfoFrame)
        self.updateDataInfoLabel.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.updateDataInfoLabel.setObjectName("updateDataInfoLabel")
        self.progressBar = QtWidgets.QProgressBar(self.DBInfoFrame)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 351, 23))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.updateDataInfoLabel2 = QtWidgets.QLabel(self.DBInfoFrame)
        self.updateDataInfoLabel2.setGeometry(QtCore.QRect(20, 70, 331, 21))
        self.updateDataInfoLabel2.setObjectName("updateDataInfoLabel2")
        self.IndicatorsFrame = QtWidgets.QFrame(self.centralWidget)
        self.IndicatorsFrame.setGeometry(QtCore.QRect(10, 150, 1021, 521))
        self.IndicatorsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.IndicatorsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IndicatorsFrame.setObjectName("IndicatorsFrame")
        self.layoutWidget1 = QtWidgets.QWidget(self.IndicatorsFrame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 1001, 504))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.indicatorsHorizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.indicatorsHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.indicatorsHorizontalLayout.setObjectName("indicatorsHorizontalLayout")
        self.firstIndicatorFrame = QtWidgets.QFrame(self.layoutWidget1)
        self.firstIndicatorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.firstIndicatorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.firstIndicatorFrame.setObjectName("firstIndicatorFrame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.firstIndicatorFrame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 501, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.firstIndVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.firstIndVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.firstIndVerticalLayout.setObjectName("firstIndVerticalLayout")
        self.firstIndicatorLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.firstIndicatorLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.firstIndicatorLabel.setObjectName("firstIndicatorLabel")
        self.firstIndVerticalLayout.addWidget(self.firstIndicatorLabel)
        self.GPPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.GPPushButton.setMinimumSize(QtCore.QSize(400, 50))
        self.GPPushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.GPPushButton.setObjectName("GPPushButton")
        self.firstIndVerticalLayout.addWidget(self.GPPushButton, 0, QtCore.Qt.AlignHCenter)
        self.strategyPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.strategyPushButton.setMinimumSize(QtCore.QSize(400, 50))
        self.strategyPushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.strategyPushButton.setObjectName("strategyPushButton")
        self.firstIndVerticalLayout.addWidget(self.strategyPushButton, 0, QtCore.Qt.AlignHCenter)
        self.PMPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.PMPushButton.setMinimumSize(QtCore.QSize(400, 50))
        self.PMPushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.PMPushButton.setObjectName("PMPushButton")
        self.firstIndVerticalLayout.addWidget(self.PMPushButton, 0, QtCore.Qt.AlignHCenter)
        self.RPPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.RPPushButton.setEnabled(False)
        self.RPPushButton.setMinimumSize(QtCore.QSize(400, 50))
        self.RPPushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.RPPushButton.setObjectName("RPPushButton")
        self.firstIndVerticalLayout.addWidget(self.RPPushButton, 0, QtCore.Qt.AlignHCenter)
        self.CYRPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.CYRPushButton.setMinimumSize(QtCore.QSize(400, 50))
        self.CYRPushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.CYRPushButton.setObjectName("CYRPushButton")
        self.firstIndVerticalLayout.addWidget(self.CYRPushButton, 0, QtCore.Qt.AlignHCenter)
        self.indicatorsHorizontalLayout.addWidget(self.firstIndicatorFrame)
        self.secondIndicatorFrame = QtWidgets.QFrame(self.layoutWidget1)
        self.secondIndicatorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.secondIndicatorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.secondIndicatorFrame.setObjectName("secondIndicatorFrame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.secondIndicatorFrame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 501, 501))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.secondIndVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.secondIndVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.secondIndVerticalLayout.setObjectName("secondIndVerticalLayout")
        self.secondIndicatorLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.secondIndicatorLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.secondIndicatorLabel.setObjectName("secondIndicatorLabel")
        self.secondIndVerticalLayout.addWidget(self.secondIndicatorLabel)
        self.GPPushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.GPPushButton2.setMinimumSize(QtCore.QSize(400, 50))
        self.GPPushButton2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.GPPushButton2.setObjectName("GPPushButton2")
        self.secondIndVerticalLayout.addWidget(self.GPPushButton2, 0, QtCore.Qt.AlignHCenter)
        self.strategyPushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.strategyPushButton2.setMinimumSize(QtCore.QSize(400, 50))
        self.strategyPushButton2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.strategyPushButton2.setObjectName("strategyPushButton2")
        self.secondIndVerticalLayout.addWidget(self.strategyPushButton2, 0, QtCore.Qt.AlignHCenter)
        self.PMPushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.PMPushButton2.setMinimumSize(QtCore.QSize(400, 50))
        self.PMPushButton2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.PMPushButton2.setObjectName("PMPushButton2")
        self.secondIndVerticalLayout.addWidget(self.PMPushButton2, 0, QtCore.Qt.AlignHCenter)
        self.RPPushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.RPPushButton2.setEnabled(False)
        self.RPPushButton2.setMinimumSize(QtCore.QSize(400, 50))
        self.RPPushButton2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.RPPushButton2.setObjectName("RPPushButton2")
        self.secondIndVerticalLayout.addWidget(self.RPPushButton2, 0, QtCore.Qt.AlignHCenter)
        self.CYRPushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.CYRPushButton2.setMinimumSize(QtCore.QSize(400, 50))
        self.CYRPushButton2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.CYRPushButton2.setObjectName("CYRPushButton2")
        self.secondIndVerticalLayout.addWidget(self.CYRPushButton2, 0, QtCore.Qt.AlignHCenter)
        self.indicatorsHorizontalLayout.addWidget(self.secondIndicatorFrame)
        self.firstIndInfoFrame = QtWidgets.QFrame(self.centralWidget)
        self.firstIndInfoFrame.setGeometry(QtCore.QRect(10, 680, 311, 181))
        self.firstIndInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.firstIndInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.firstIndInfoFrame.setObjectName("firstIndInfoFrame")
        self.firstIndicatorInfo = QtWidgets.QLabel(self.firstIndInfoFrame)
        self.firstIndicatorInfo.setGeometry(QtCore.QRect(10, 10, 291, 150))
        self.firstIndicatorInfo.setObjectName("firstIndicatorInfo")
        self.secondIndInfoFrame = QtWidgets.QFrame(self.centralWidget)
        self.secondIndInfoFrame.setGeometry(QtCore.QRect(710, 680, 311, 181))
        self.secondIndInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.secondIndInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.secondIndInfoFrame.setObjectName("secondIndInfoFrame")
        self.secondIndicatorInfo = QtWidgets.QLabel(self.secondIndInfoFrame)
        self.secondIndicatorInfo.setGeometry(QtCore.QRect(10, 10, 291, 150))
        self.secondIndicatorInfo.setObjectName("secondIndicatorInfo")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.autoUpdateAction = QtWidgets.QAction(MainWindow)
        self.autoUpdateAction.setObjectName("autoUpdateAction")
        self.update = QtWidgets.QAction(MainWindow)
        self.update.setObjectName("update")
        self.menu.addAction(self.autoUpdateAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comparePushButton.setText(_translate("MainWindow", "????????????????"))
        self.compareLitePushButton.setText(_translate("MainWindow", "????????????????\n"
"(??????????????????)"))
        self.savePushButton.setText(_translate("MainWindow", "??????????????????"))
        self.saveAsLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">?????????????????? ??????:</p></body></html>"))
        self.textRadioButton.setText(_translate("MainWindow", "??????????"))
        self.tableRadioButton.setText(_translate("MainWindow", "??????????????"))
        self.graphRadioButton.setText(_translate("MainWindow", "????????????"))
        self.planRadioButton.setText(_translate("MainWindow", "????????"))
        self.factRadioButton.setText(_translate("MainWindow", "????????"))
        self.planFactLabel.setText(_translate("MainWindow", "????????????????:"))
        self.oneYearButton.setText(_translate("MainWindow", "???????? ??????"))
        self.yearPeriodButton.setText(_translate("MainWindow", "???????????? "))
        self.headerLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">????????????</p></body></html>"))
        self.fromLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">????</p></body></html>"))
        self.toLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">????</p></body></html>"))
        self.footerLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">???????? ?????????????????????? ????????????????????????</p></body></html>"))
        self.updateDataInfoLabel.setText(_translate("MainWindow", "???????????????????? ???? ???????? ???????????? ??????????????????"))
        self.updateDataInfoLabel2.setText(_translate("MainWindow", "???????????????????????????? ??????????: "))
        self.firstIndicatorLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">???????????? ????????????????????</span></p></body></html>"))
        self.GPPushButton.setText(_translate("MainWindow", "?????????????????????????????? ??????????????????"))
        self.strategyPushButton.setText(_translate("MainWindow", "?????????????????? ????????????????"))
        self.PMPushButton.setText(_translate("MainWindow", "???????? ?????????????????????? ???? ???????????????????? ?????????????????? ????????????????"))
        self.RPPushButton.setText(_translate("MainWindow", "???????????????????????? ??????????????"))
        self.CYRPushButton.setText(_translate("MainWindow", "??????"))
        self.secondIndicatorLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">???????????? ????????????????????</span></p></body></html>"))
        self.GPPushButton2.setText(_translate("MainWindow", "?????????????????????????????? ??????????????????"))
        self.strategyPushButton2.setText(_translate("MainWindow", "?????????????????? ????????????????"))
        self.PMPushButton2.setText(_translate("MainWindow", "???????? ?????????????????????? ???? ???????????????????? ?????????????????? ????????????????"))
        self.RPPushButton2.setText(_translate("MainWindow", "???????????????????????? ??????????????"))
        self.CYRPushButton2.setText(_translate("MainWindow", "??????"))
        self.firstIndicatorInfo.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.secondIndicatorInfo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "??????????????????"))
        self.autoUpdateAction.setText(_translate("MainWindow", "?????????????? ????????????????????????????"))
        self.update.setText(_translate("MainWindow", "???????????? ????????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
