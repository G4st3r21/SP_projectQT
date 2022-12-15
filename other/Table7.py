import time

from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from classes.DataBase import DataBase
from openpyxl import load_workbook

from other.paste import parsing


def get_schema_names():
    wb: Workbook = load_workbook("xlsx/Gosprogrammy_v_tablitse_7.xlsx")
    ws: Worksheet = wb.worksheets[0]
    rows = list(ws.rows)
    schema_names = dict()
    for row in rows:
        schema_names[row[2].value] = row[1].value

    return schema_names


class DataBaseTable7(DataBase):
    def __init__(self):
        super().__init__()
        print("Получение схем")
        self.schema_names: dict = get_schema_names()
        print("Схемы получены")
        print("Получение показателей по схемам")
        self.indicators_by_gp = self.get_indicators_by_gp(self.schema_names)
        print("Схемы по показателям получены")
        self.end_indicator_dict = dict()

    def find_all_for_table_7(self):
        wb = load_workbook("xlsx/Таблица 7.xlsx")
        ws = wb.worksheets[0]
        rows = list(ws.iter_rows(min_row=8, max_row=240))
        schema_gp_list = [(row[2].value, row[9].value) for row in rows if row[2].value]

        for sgp in schema_gp_list:
            if sgp[0] and sgp[1]:
                real_schema_name = self.schema_names[sgp[0].strip()]
                print(sgp)
                sgp_indicators = sgp[1].split('\n')
                for sgp_indicator in sgp_indicators:
                    for indicator_name in self.indicators_by_gp[real_schema_name]:
                        if indicator_name in sgp_indicator and indicator_name not in [" ", "\n"]:
                            print("Найден показатель:", indicator_name)
                            self.end_indicator_dict[sgp_indicator] = self.get_indicators_by_name(
                                real_schema_name,
                                indicator_name
                            )
                            break

        return self.end_indicator_dict

    def get_indicators_by_gp(self, schema_list):
        indicators_by_gp = dict()
        for key, schema in schema_list.items():
            indicators_by_gp[schema] = self.get_GP_indicator_names(schema)

        return indicators_by_gp

    def get_indicators_by_name(self, schema_name, ind_name: str):
        ind_name = ind_name.replace('%', '%%') if '%' in ind_name else ind_name

        tables_with_titles = self.get_table_list_by_schema_and_table_name(schema_name, "names_indicators____")
        tables_with_indicators = self.get_table_list_by_schema_and_table_name(schema_name, "indicators____")

        titles_id_by_years = [
            (table[-4:],
             self.conn.execute(
                 f"SELECT id, type FROM " +
                 f'"{schema_name}"' + f".{table} WHERE '{ind_name}' LIKE title_indication"
             ).first()
             ) for table in tables_with_titles
        ]

        indicators_by_years = []
        for year in range(len(titles_id_by_years)):
            if titles_id_by_years[year][1] is not None:
                indicators_by_years.append(
                    (titles_id_by_years[year][0],
                     self.conn.execute(
                         f"SELECT plan, fact, unit_of_measurement FROM " +
                         f'"{schema_name}"' +
                         f".{tables_with_indicators[year]} WHERE id = {titles_id_by_years[year][1][0]}"
                     ).first()
                     )
                )
            else:
                indicators_by_years.append((titles_id_by_years[year][0], "-"))

        return indicators_by_years


test = DataBaseTable7()
start = time.time()
with open("output.txt", 'w') as output_file:
    table_7 = test.find_all_for_table_7()
    items = list(table_7.items())
    print(*items, file=output_file, sep='\n')
    # parsing(table_7)
print(time.time() - start)
