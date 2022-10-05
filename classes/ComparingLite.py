from PyQt5.QtWidgets import QWidget
from uiFiles.CompareIndicatorsLite import Ui_Form as CompareWidget


class ComparingLite(QWidget, CompareWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.first_indicators = []
        self.second_indicators = []
        self.buttonBox.accepted.connect(self.hide)

    # def format_indicators(self, indicators):

    def set_first_indicators(self, ind_name, indicators=None):
        self.first_indicators = []
        self.first_indicators[0] = ind_name
        self.first_indicators[1] = ''
        self.first_indicators[2:] = indicators

    def set_second_indicators(self, ind_name, indicators=None):
        self.second_indicators = []
        self.second_indicators[0] = ind_name
        self.second_indicators[1] = ''
        self.second_indicators[2:] = indicators

    def showWidget(self):
        self.firstIndListWidget.addItems(self.first_indicators)
        self.secondIndListWidget.addItems(self.second_indicators)

        self.show()
