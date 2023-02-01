from PyQt5.QtWidgets import QDialog

from classes.DBThreadInteraction import DBInteraction
from uiFiles.UpdateSettings import Ui_Dialog


class SPAutoUpdateSettings(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        # uic.loadUi('uiFiles/MainWindow1.ui', self) # Подгрузка из ui файла
        self.setupUi(self)  # Подгрузка из py класса
        self.setWindowTitle('Настройка')
        self.buttonBox.accepted.connect(self.update_settings)

    def update_settings(self):
        minutes = self.minSpinBox.text()
        seconds = self.secSpinBox.text()
        if not ((minutes == 0 and seconds == 0) or (minutes == 0 and seconds <= 5)):
            DBInteraction.time_to_wait = int(minutes) * 60 + int(seconds)

        self.hide()
