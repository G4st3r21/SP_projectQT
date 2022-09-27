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
        MainWindow.resize(1040, 897)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.SaveParametersFrame = QtWidgets.QFrame(self.centralWidget)
        self.SaveParametersFrame.setGeometry(QtCore.QRect(330, 680, 371, 171))
        self.SaveParametersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SaveParametersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SaveParametersFrame.setObjectName("SaveParametersFrame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.SaveParametersFrame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 351, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.saveParametersHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveParametersHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.saveParametersHorizontalLayout.setObjectName("saveParametersHorizontalLayout")
        self.comparePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.comparePushButton.setMinimumSize(QtCore.QSize(0, 75))
        self.comparePushButton.setObjectName("comparePushButton")
        self.saveParametersHorizontalLayout.addWidget(self.comparePushButton)
        self.savePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.savePushButton.setMinimumSize(QtCore.QSize(0, 75))
        self.savePushButton.setObjectName("savePushButton")
        self.saveParametersHorizontalLayout.addWidget(self.savePushButton)
        self.saveAsVerticalLayout = QtWidgets.QVBoxLayout()
        self.saveAsVerticalLayout.setObjectName("saveAsVerticalLayout")
        self.saveAsLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.saveAsLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.saveAsLabel.setObjectName("saveAsLabel")
        self.saveAsVerticalLayout.addWidget(self.saveAsLabel)
        self.textRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.textRadioButton.setObjectName("textRadioButton")
        self.saveAsVerticalLayout.addWidget(self.textRadioButton)
        self.tableRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.tableRadioButton.setObjectName("tableRadioButton")
        self.saveAsVerticalLayout.addWidget(self.tableRadioButton)
        self.graphRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.graphRadioButton.setObjectName("graphRadioButton")
        self.saveAsVerticalLayout.addWidget(self.graphRadioButton)
        self.saveParametersHorizontalLayout.addLayout(self.saveAsVerticalLayout)
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
        self.layoutWidget = QtWidgets.QWidget(self.IndicatorsFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1001, 504))
        self.layoutWidget.setObjectName("layoutWidget")
        self.indicatorsHorizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.indicatorsHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.indicatorsHorizontalLayout.setObjectName("indicatorsHorizontalLayout")
        self.firstIndicatorFrame = QtWidgets.QFrame(self.layoutWidget)
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
        self.secondIndicatorFrame = QtWidgets.QFrame(self.layoutWidget)
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
        self.frame_3 = QtWidgets.QFrame(self.centralWidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 680, 311, 170))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.firstIndicatorInfo = QtWidgets.QLabel(self.frame_3)
        self.firstIndicatorInfo.setGeometry(QtCore.QRect(10, 10, 291, 150))
        self.firstIndicatorInfo.setObjectName("firstIndicatorInfo")
        self.frame_4 = QtWidgets.QFrame(self.centralWidget)
        self.frame_4.setGeometry(QtCore.QRect(710, 680, 311, 170))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.secondIndicatorInfo = QtWidgets.QLabel(self.frame_4)
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
        self.comparePushButton.setText(_translate("MainWindow", "СРАВНИТЬ"))
        self.savePushButton.setText(_translate("MainWindow", "Сохранить"))
        self.saveAsLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Сохранить как:</p></body></html>"))
        self.textRadioButton.setText(_translate("MainWindow", "Текст"))
        self.tableRadioButton.setText(_translate("MainWindow", "Таблица"))
        self.graphRadioButton.setText(_translate("MainWindow", "График"))
        self.planRadioButton.setText(_translate("MainWindow", "План"))
        self.factRadioButton.setText(_translate("MainWindow", "Факт"))
        self.planFactLabel.setText(_translate("MainWindow", "Выберите:"))
        self.oneYearButton.setText(_translate("MainWindow", "Один год"))
        self.yearPeriodButton.setText(_translate("MainWindow", "Период "))
        self.headerLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ПЕРИОД</p></body></html>"))
        self.fromLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ОТ</p></body></html>"))
        self.toLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ДО</p></body></html>"))
        self.footerLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Дата указывается включительно</p></body></html>"))
        self.updateDataInfoLabel.setText(_translate("MainWindow", "Информация из базы данных обновлена"))
        self.updateDataInfoLabel2.setText(_translate("MainWindow", "Автообновление через: "))
        self.firstIndicatorLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">ПЕРВЫЙ ПОКАЗАТЕЛЬ</span></p></body></html>"))
        self.GPPushButton.setText(_translate("MainWindow", "Государственные программы"))
        self.strategyPushButton.setText(_translate("MainWindow", "Стратегия развития"))
        self.PMPushButton.setText(_translate("MainWindow", "План мероприятий по реализации Стратегии развития"))
        self.RPPushButton.setText(_translate("MainWindow", "Региональные проекты"))
        self.CYRPushButton.setText(_translate("MainWindow", "ЦУР"))
        self.secondIndicatorLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">ВТОРОЙ ПОКАЗАТЕЛЬ</span></p></body></html>"))
        self.GPPushButton2.setText(_translate("MainWindow", "Государственные программы"))
        self.strategyPushButton2.setText(_translate("MainWindow", "Стратегия развития"))
        self.PMPushButton2.setText(_translate("MainWindow", "План мероприятий по реализации Стратегии развития"))
        self.RPPushButton2.setText(_translate("MainWindow", "Региональные проекты"))
        self.CYRPushButton2.setText(_translate("MainWindow", "ЦУР"))
        self.firstIndicatorInfo.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.secondIndicatorInfo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "Настройки"))
        self.autoUpdateAction.setText(_translate("MainWindow", "Частота автообновления"))
        self.update.setText(_translate("MainWindow", "Ручное обновление"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
