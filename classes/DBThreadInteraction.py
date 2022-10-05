import time

from PyQt5.QtCore import QThread

from classes.DataBase import DataBase
from classes.IndustriesIndicators import industries_indicators


class DBThreadInteraction(QThread):
    def __init__(self):
        super().__init__()
        self.main_window = None

        self.strategies = StrategiesThread()
        self.PM = PMThread()
        self.CYR = CYRThread()
        self.GP = GPThread()
        self.RP = RPThread()

        self.time_to_wait = 60
        self.updated_set = set()
        self.percent = 0
        self.all_indicators_loaded = False

    def run(self) -> None:
        while True:
            self.updated_set = set()
            self.start_requests()
            while True:
                self.update_progressBar()
                if self.main_window is not None:
                    self.main_window.updateDataInfoLabel.setText("Обновление информации из базы данных")

                if self.percent == 100:
                    self.push_to_dataclass()
                    self.all_indicators_loaded = True
                    if self.main_window is not None and self.percent == 100:
                        self.main_window.updateDataInfoLabel.setText("Информация из базы данных обновлена")
                    break

            self.sleep_timer()

    def push_to_dataclass(self):
        industries_indicators.indicators["Strategies"] = self.strategies.strategy_list
        industries_indicators.indicators["PM"] = self.PM.PM_list
        industries_indicators.indicators["CYR"] = self.CYR.CYR_list

        industries_indicators.GP_industries_all = self.GP.GP_industries_all
        industries_indicators.GP_industries = self.GP.GP_industries_all[0]
        industries_indicators.GP_industries_ru = self.GP.GP_industries_all[1]

        industries_indicators.RP_industries_all = self.RP.RP_industries_all
        industries_indicators.RP_industries = self.RP.RP_industries_all[0]
        industries_indicators.RP_industries_ru = self.RP.RP_industries_all[1]

        industries_indicators.GP_indicators_by_industries = self.GP.indicators_by_industries
        industries_indicators.RP_indicators_by_industries = self.RP.indicators_by_industries

    def start_requests(self):
        print("Загрузка ГП показателей")
        self.GP.start()

        print("Загрузка РП показателей")
        self.RP.start()

        print("Загрузка показателей стратегий")
        self.strategies.start()

        print("Загрузка показателей ЦУР")
        self.CYR.start()

        print("Загрузка показателей ПМ")
        self.PM.start()

    def update_progressBar(self):
        if self.strategies.strategy_updated and self.strategies not in self.updated_set:
            self.updated_set.add(self.strategies)
            print("Показатели стратегий загружены")

        if self.PM.PM_updated and self.PM not in self.updated_set:
            self.updated_set.add(self.PM)
            print("Показатели ПМ загружены")

        if self.CYR.CYR_updated and self.CYR not in self.updated_set:
            self.updated_set.add(self.CYR)
            print("Показатели ЦУР загружены")

        if self.GP.GP_updated and self.GP not in self.updated_set:
            self.updated_set.add(self.GP)
            print("Показатели ГП загружены")

        if self.RP.RP_updated and self.RP not in self.updated_set:
            self.updated_set.add(self.RP)
            print("Показатели РП загружены")

        self.percent = len(self.updated_set) * 20
        if self.main_window is not None:
            self.main_window.progressBar.setValue(self.percent)

    def sleep_timer(self):
        remaining_time = self.time_to_wait
        while remaining_time > 0:
            time.sleep(1)
            remaining_time -= 1
            if self.main_window is not None:
                if remaining_time / 60 >= 1:
                    self.main_window.updateDataInfoLabel2.setText(
                        f"Автообновление через: {int(remaining_time / 60)} мин. "
                        f"{remaining_time - int(remaining_time / 60) * 60} сек."
                    )
                else:
                    self.main_window.updateDataInfoLabel2.setText(
                        f"Автообновление через: {remaining_time} сек."
                    )


class StrategiesThread(QThread):
    def __init__(self):
        super().__init__()
        self.DB = DataBase()
        self.strategy_list = []
        self.strategy_updated = False

    def run(self) -> None:
        self.strategy_updated = False
        self.strategy_list = self.DB.get_strategy_indicators_names()
        self.strategy_updated = True


class PMThread(QThread):
    def __init__(self):
        super().__init__()
        self.DB = DataBase()
        self.PM_list = []
        self.PM_updated = False

    def run(self) -> None:
        self.PM_updated = False
        self.PM_list = self.DB.get_PM_indicators_names()
        self.PM_updated = True


class CYRThread(QThread):
    def __init__(self):
        super().__init__()
        self.DB = DataBase()
        self.CYR_list = []
        self.CYR_updated = False

    def run(self) -> None:
        self.CYR_updated = False
        self.CYR_list = self.DB.get_CYR_indicators_names()
        self.CYR_updated = True


class GPThread(QThread):
    def __init__(self):
        super().__init__()
        self.DB = DataBase()

        self.indicators_by_industries = dict()

        self.GP_industries_all = []
        self.GP_industries = []
        self.GP_industries_ru = []
        self.GP_updated = False

    def run(self):
        self.GP_updated = False
        self.GP_industries_all = self.DB.get_industries()
        self.GP_industries = self.GP_industries_all[0]
        self.GP_industries_ru = self.GP_industries_all[1]

        self.__request_all_GP_indicators_by_industries__()
        self.GP_updated = True

    def __request_all_GP_indicators_by_industries__(self):
        for industry in self.GP_industries:
            indicators = self.DB.get_GP_indicators_names(industry)
            self.indicators_by_industries[industry] = indicators


class RPThread(QThread):
    def __init__(self):
        super().__init__()
        self.DB = DataBase()

        self.indicators_by_industries = dict()

        self.RP_industries_ru = []
        self.RP_industries = []
        self.RP_industries_all = []
        self.RP_updated = False

    def run(self):
        self.RP_updated = False

        self.RP_industries_all = self.DB.get_industries()
        self.RP_industries = self.RP_industries_all[0]
        self.RP_industries_ru = self.RP_industries_all[1]

        self.__request_all_RP_indicators_by_industries__()
        self.RP_updated = True

    def __request_all_RP_indicators_by_industries__(self):
        for industry in self.RP_industries:
            indicators = self.DB.get_RP_indicators_names(industry)
            self.indicators_by_industries[industry] = indicators


DBInteraction = DBThreadInteraction()
