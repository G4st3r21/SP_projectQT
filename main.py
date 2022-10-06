import os
import sys
from PyQt5.QtWidgets import QApplication

from classes import SPMainWindow, SPIndWidget, SPIndWidgetPlus, ComparingLite
from classes.DBThreadInteraction import DBInteraction
# from other.logger_cfg import logging
#
# os.system("python -m PyQt5.uic.pyuic -x uiFiles/MainWindow.ui -o uiFiles/MainWindow.py")
# os.system("python -m PyQt5.uic.pyuic -x uiFiles/updateSettings.ui -o uiFiles/UpdateSettings.py")
# os.system("python -m PyQt5.uic.pyuic -x uiFiles/IndSubMenuWidget.ui -o uiFiles/IndSubMenuWidget.py")
# os.system("python -m PyQt5.uic.pyuic -x uiFiles/IndSubMenuWidget1.ui -o uiFiles/IndSubMenuWidget1.py")
# os.system("python -m PyQt5.uic.pyuic -x uiFiles/CompareIndicatorsLite.ui -o uiFiles/CompareIndicatorsLite.py")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    DBInteraction.start()
    while DBInteraction.percent != 100:
        pass

    # logging.info("Загрузка виджетов")
    exWidget = SPIndWidget.SPIndWidget()
    exWidgetPlus = SPIndWidgetPlus.SPIndWidgetPlus()
    exWidgetComparingLite = ComparingLite.ComparingLite()
    ex = SPMainWindow.SPMainWindow(exWidget, exWidgetPlus, exWidgetComparingLite)

    DBInteraction.main_window = ex
    # logging.info("Все виджеты успешно загружены")

    sys.exit(app.exec_())
