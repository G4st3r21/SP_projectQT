from classes.DataBase import DataBase
from classes.TableBlockConstructor import TableBlockConstructor


class CompareFull:
    def __init__(self, first_field, second_field):
        self.constructor = TableBlockConstructor("", "")
        self.first_field = first_field
        self.second_field = second_field

    def test_comparing_CYR_GP(self, cyr_params, gp_params, path):
        testDB = DataBase()
        test_gp_info = testDB.get_GP_info(*gp_params)
        test_cyr_info = testDB.get_CYR_info(*cyr_params)
        self.constructor.fill_CYR_GP_sample(*test_gp_info, *test_cyr_info, path)
