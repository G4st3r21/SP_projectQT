# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/IndSubMenuWidget1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 755)
        self.lastSearchedScrollArea = QtWidgets.QScrollArea(Form)
        self.lastSearchedScrollArea.setGeometry(QtCore.QRect(10, 603, 381, 111))
        self.lastSearchedScrollArea.setWidgetResizable(True)
        self.lastSearchedScrollArea.setObjectName("lastSearchedScrollArea")
        self.LSScrollAreaWidgetContents = QtWidgets.QWidget()
        self.LSScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 109))
        self.LSScrollAreaWidgetContents.setObjectName("LSScrollAreaWidgetContents")
        self.lastSearchedListWidget = QtWidgets.QListWidget(self.LSScrollAreaWidgetContents)
        self.lastSearchedListWidget.setGeometry(QtCore.QRect(0, 1, 381, 111))
        self.lastSearchedListWidget.setObjectName("lastSearchedListWidget")
        self.lastSearchedScrollArea.setWidget(self.LSScrollAreaWidgetContents)
        self.chooseIndustrylabel = QtWidgets.QLabel(Form)
        self.chooseIndustrylabel.setGeometry(QtCore.QRect(10, 10, 381, 20))
        self.chooseIndustrylabel.setObjectName("chooseIndustrylabel")
        self.reccomendsLabel = QtWidgets.QLabel(Form)
        self.reccomendsLabel.setGeometry(QtCore.QRect(10, 440, 381, 20))
        self.reccomendsLabel.setObjectName("reccomendsLabel")
        self.allIndicatorsLabel = QtWidgets.QLabel(Form)
        self.allIndicatorsLabel.setGeometry(QtCore.QRect(10, 150, 381, 20))
        self.allIndicatorsLabel.setObjectName("allIndicatorsLabel")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(10, 720, 381, 35))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.allIndicatorsScrollArea = QtWidgets.QScrollArea(Form)
        self.allIndicatorsScrollArea.setGeometry(QtCore.QRect(10, 173, 381, 251))
        self.allIndicatorsScrollArea.setWidgetResizable(True)
        self.allIndicatorsScrollArea.setObjectName("allIndicatorsScrollArea")
        self.AIScrollAreaWidgetContents = QtWidgets.QWidget()
        self.AIScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 249))
        self.AIScrollAreaWidgetContents.setObjectName("AIScrollAreaWidgetContents")
        self.allIndicatorsListWidget = QtWidgets.QListWidget(self.AIScrollAreaWidgetContents)
        self.allIndicatorsListWidget.setGeometry(QtCore.QRect(0, 0, 381, 251))
        self.allIndicatorsListWidget.setObjectName("allIndicatorsListWidget")
        self.allIndicatorsScrollArea.setWidget(self.AIScrollAreaWidgetContents)
        self.lastSearchedLabel = QtWidgets.QLabel(Form)
        self.lastSearchedLabel.setGeometry(QtCore.QRect(10, 580, 381, 20))
        self.lastSearchedLabel.setObjectName("lastSearchedLabel")
        self.reccomendsScrollArea = QtWidgets.QScrollArea(Form)
        self.reccomendsScrollArea.setGeometry(QtCore.QRect(10, 463, 381, 111))
        self.reccomendsScrollArea.setWidgetResizable(True)
        self.reccomendsScrollArea.setObjectName("reccomendsScrollArea")
        self.RScrollAreaWidgetContents = QtWidgets.QWidget()
        self.RScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 109))
        self.RScrollAreaWidgetContents.setObjectName("RScrollAreaWidgetContents")
        self.recommendsListWidget = QtWidgets.QListWidget(self.RScrollAreaWidgetContents)
        self.recommendsListWidget.setGeometry(QtCore.QRect(0, 0, 381, 111))
        self.recommendsListWidget.setObjectName("recommendsListWidget")
        self.reccomendsScrollArea.setWidget(self.RScrollAreaWidgetContents)
        self.searchIndicatorsTextEdit = QtWidgets.QTextEdit(Form)
        self.searchIndicatorsTextEdit.setGeometry(QtCore.QRect(10, 90, 381, 31))
        self.searchIndicatorsTextEdit.setObjectName("searchIndicatorsTextEdit")
        self.searchLabel = QtWidgets.QLabel(Form)
        self.searchLabel.setGeometry(QtCore.QRect(10, 70, 381, 20))
        self.searchLabel.setObjectName("searchLabel")
        self.chooseIndustryComboBox = QtWidgets.QComboBox(Form)
        self.chooseIndustryComboBox.setGeometry(QtCore.QRect(15, 30, 371, 25))
        self.chooseIndustryComboBox.setObjectName("chooseIndustryComboBox")
        self.updateIndicatorsToolButton = QtWidgets.QToolButton(Form)
        self.updateIndicatorsToolButton.setGeometry(QtCore.QRect(370, 150, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.updateIndicatorsToolButton.setFont(font)
        self.updateIndicatorsToolButton.setObjectName("updateIndicatorsToolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.chooseIndustrylabel.setText(_translate("Form", "<html><head/><body><p align=\"center\">Выбор отрасли</p></body></html>"))
        self.reccomendsLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\">Рекомендуемые</p></body></html>"))
        self.allIndicatorsLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\">Все показатели</p></body></html>"))
        self.lastSearchedLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\">Последние</p></body></html>"))
        self.searchLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\">Поиск среди всех показателей выбранной отрасли</p></body></html>"))
        self.updateIndicatorsToolButton.setText(_translate("Form", "↻"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
