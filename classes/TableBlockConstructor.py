from copy import copy

import openpyxl
from openpyxl.cell import Cell, \
    MergedCell  # КЛАСС ЯЧЕЙКИ, С КОТОРЫМ ТЕБЕ ПРЕДСТОИТ РАБОТАТЬ, ПОЧИТАЙ О НЕМ ПОДРОБНЕЕ В ДОКАХ
from openpyxl.worksheet.worksheet import Worksheet


def getPattern(file):
    book = openpyxl.open(file)
    sheet = book.active['B2':'C12']
    # cells = sheet['B2':'C12']
    # print(type(sheet['B2']))
    # book = xlwt.Workbook(encoding="utf-8")
    # sheet1 = book.add_sheet("Python Sheet 1")
    # sheet1.write(1, 1, sheet.cell(2, 2).value)
    # book.save("spreadsheet.xls")
    # wb = Workbook()
    # ws = wb.active
    # ws.cell(2, 2).value = sheet.cell(2, 2).value
    # wb.save("sample.xlsx")
    return sheet


class TableBlockConstructor:
    def __init__(self):
        """
        В инициализации класса у тебя будут готовые шаблоны(списки ячеек типа "Cell"), которые нужно будет брать из
        таблицы(именно пустые). Все это с помощью openpyxl(через тот же load_workbook(), например).
        """
        self.GP_sample: list[Cell] = []
        self.RP_sample: list = []
        self.strategy_sample: list = []
        self.PM_sample: list = []
        self.CYR_sample: list = []

    def fill_GP_sample(self):
        """
        Тут заполняешь шаблон ячеек под гос. программы, остальные 4 метода по аналогии пишешь.
        В аргументах указываешь все, что тебе нужно для конкретного шаблона блока(показатели, наименования и т.д.)
        В return передаешь готовый список заполненных ячеек.
        """
        pass  # Временная заглушка, чтобы PyCharm не ругался на пустой метод

    def fill_CYR_sample(self, indicator_rf, task_id, task, cyr_id, cyr, indicator_vo, gosprogram, response_obj):
        file = "../tableTemplates/ЦУР — Госпрограмма.xlsx"
        self.CYR_sample = getPattern(file)
        cnt = 0
        for first, second in self.CYR_sample:
            if cnt == 1:
                second.value = indicator_rf
            elif cnt == 3:
                first.value = first.value[:8] + task_id
                second.value = task
            elif cnt == 4:
                first.value = first.value[:5] + cyr_id
                second.value = cyr
            elif cnt == 8:
                second.value = indicator_vo
            elif cnt == 9:
                second.value = gosprogram
            elif cnt == 10:
                second.value = response_obj
            cnt += 1
        return self.CYR_sample


test = TableBlockConstructor()
test_sample = test.fill_CYR_sample("1", "1", "1", "1", "1", "1", "1", "1")
print(test_sample)

test_book = openpyxl.Workbook()
test_book.create_sheet("test", 0)
test_sheet: Worksheet = test_book.worksheets[0]

for row in test_sample:
    for cell in row:
        if type(cell) is not MergedCell:
            temp_cell: Cell = test_sheet.cell(cell.row, cell.col_idx)
            if cell.has_style:
                temp_cell._style = copy(cell.style)

test_book.save("../test.xlsx")
