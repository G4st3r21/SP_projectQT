from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from classes.config import *
from models.public import Year, IndicatorsName, Indicator
from models.public import IndicationsRf, IndicationsVo, Cyr, ResponseObj, Gosprogram, Task, \
    t_indications_rf_vo, t_indications_rf_target, t_gosprogram_target
from models import information_schema


def optimize_id_list(id_list):  # Оптимизация списка id
    optimized_list, temp_list = [], []
    for ind_id in id_list:
        if not temp_list:
            temp_list.append(ind_id)
        elif ind_id - temp_list[-1] == 1:
            temp_list.append(ind_id)
        else:
            if len(temp_list) > 1:
                optimized_list.append((temp_list[0], temp_list[-1]))
            else:
                optimized_list.append(temp_list[0])
            temp_list.clear()
            temp_list.append(ind_id)

    if len(temp_list) > 1:
        optimized_list.append((temp_list[0], temp_list[-1]))
    else:
        optimized_list.append(temp_list[0])

    return optimized_list


def request_event(conn, schema_name, tables_with_events, code_event):
    for table in tables_with_events:
        event_title = conn.execute(
            f"SELECT * FROM " +
            f'"{schema_name}"' + f".{table} WHERE code = '{code_event}'"
        ).first()
        if event_title is not None:
            return event_title[1]

    return None


class DataBase:
    def __init__(self):
        self.engine = create_engine(f'postgresql://{username}:{password}@{host_name}:{port}/{db_name}', echo=False)
        self.conn = self.engine.connect()
        self.meta = MetaData(self.engine)
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def get_table_list_by_schema_and_table_name(self, schema_name, table_name):
        all_columns = information_schema.t_tables
        get_schema_tables = self.session.query(all_columns).filter(
            all_columns.c.table_schema == schema_name
        ).filter(
            all_columns.c.table_name.like(table_name)
        ).all()

        return sorted(list(set(table.table_name for table in get_schema_tables)))

    def get_table_list_by_schema_and_column_name(self, schema_name, column_name):
        all_columns = information_schema.t_columns
        get_schema_tables = self.session.query(all_columns).filter(
            all_columns.c.table_schema == schema_name
        ).filter(
            all_columns.c.column_name == column_name
        ).all()

        return sorted(list(set(table.table_name for table in get_schema_tables)))

    def get_indicators_names_by_id(self, id_list):
        indicators = []
        for ind_id in optimize_id_list(id_list):
            if type(ind_id) == int:
                indicators.append(
                    self.session.query(IndicatorsName).filter(
                        IndicatorsName.id == ind_id
                    ).first().indicator_title
                )
            else:
                indicators_names = self.session.query(IndicatorsName).filter(
                    IndicatorsName.id >= ind_id[0]
                ).filter(
                    IndicatorsName.id <= ind_id[-1]
                ).all()
                for ind_name in indicators_names:
                    indicators.append(ind_name.indicator_title)

        return sorted(indicators)

    def get_years(self):
        years = self.session.query(Year).all()

        return sorted([str(x.year) for x in years])

    def get_industries(self):
        all_columns = information_schema.t_columns
        industries = self.session.query(all_columns).filter(
            all_columns.c.table_name.like('events_grbs____')
        ).all()
        industries_names = sorted(list(set(industry[1] for industry in industries)))

        industries_names_ru = []
        for industry in industries_names:
            sql_request = f'''
            SELECT obj_description('"{industry}"'::regnamespace, 'pg_namespace')
            '''
            industries_names_ru.append(self.conn.execute(sql_request).fetchall()[0][0])

        return industries_names, industries_names_ru

    def get_strategy_indicators_names(self):
        table_list = self.get_table_list_by_schema_and_column_name("Strategies", "id_indicator_name")
        indicators = set()
        for table in table_list:
            sql_request = f'SELECT id_indicator_name FROM "Strategies".{table}'
            table_indicators = self.conn.execute(sql_request).fetchall()
            for ind in table_indicators:
                indicators.add(int(ind[0]))

        return self.get_indicators_names_by_id(indicators)

    def get_strategy_indicators(self):
        table_list = self.get_table_list_by_schema_and_column_name("Strategies", "id_indicator_name")
        indicators = set()
        for table in table_list:
            sql_request = f'SELECT * FROM "Strategies".{table}'
            table_indicators = self.conn.execute(sql_request).fetchall()
            indicators += table_indicators

        return indicators

    def get_GP_indicator_names(self, schema_name):
        tables_with_ind_names = "names_indicators____"
        tables = self.get_table_list_by_schema_and_table_name(schema_name, tables_with_ind_names)

        indicators_names = []
        for table in tables:
            sql_request = f'SELECT title_indication FROM "{schema_name}".{table}'
            indicators_names += self.conn.execute(sql_request).fetchall()

        return [ind_name[0] for ind_name in indicators_names]

    def get_GP_info(self, schema_name, indicator_name):
        tables_with_titles = self.get_table_list_by_schema_and_table_name(schema_name, "names_indicators____")
        tables_with_indicators = self.get_table_list_by_schema_and_table_name(schema_name, "indicators____")
        tables_with_events = self.get_table_list_by_schema_and_table_name(schema_name, "all_events____")
        tables_with_rejections = self.get_table_list_by_schema_and_table_name(schema_name, "rejection____")

        try:
            titles_id_by_years = [
                (table[-4:],
                 self.conn.execute(
                     f"SELECT id, type FROM " +
                     f'"{schema_name}"' + f".{table} WHERE title_indication like '{indicator_name}'"
                 ).first()
                 ) for table in tables_with_titles
            ]
        except Exception as e:
            print("Произошла ошибка при поиске ID, TYPE в таблицах names_indicators____")
            return None

        try:
            indicators_by_years = [
                self.conn.execute(
                    f"SELECT * FROM " +
                    f'"{schema_name}"' + f".{tables_with_indicators[year]} WHERE id = {titles_id_by_years[year][1][0]}"
                ).first()
                for year in range(len(titles_id_by_years))
            ]
        except Exception as e:
            print("Произошла ошибка при поиске всех данных о показателе в таблицах indicators____")
            return None

        code_event = indicators_by_years[0][1]

        match len(code_event):
            case 5:
                event_title = request_event(self.conn, schema_name, tables_with_events, code_event)
                main_event_title = request_event(self.conn, schema_name, tables_with_events, code_event[:4])
                subprogram_title = request_event(self.conn, schema_name, tables_with_events, code_event[0])
            case 3:
                event_title = None
                main_event_title = request_event(self.conn, schema_name, tables_with_events, code_event[:4])
                subprogram_title = request_event(self.conn, schema_name, tables_with_events, code_event[0])
            case 1:
                event_title = None
                main_event_title = None
                subprogram_title = request_event(self.conn, schema_name, tables_with_events, code_event[0])
            case _:
                event_title = None
                main_event_title = None
                subprogram_title = None

        rejection = [
            (
                table[-4:],
                self.conn.execute(
                    f"SELECT * FROM " +
                    f'"{schema_name}"' +
                    f".{table} WHERE id_value = {indicators_by_years[tables_with_rejections.index(table)][0]}")
            ) for table in tables_with_rejections
        ][-1]

        return [
            str(indicator_name),
            str(code_event[:5]) if event_title is not None else None,
            str(event_title),
            str(code_event[:4]) if main_event_title is not None else None,
            str(main_event_title),
            str(code_event[0]) if subprogram_title is not None else None,
            str(subprogram_title),
            str(tables_with_titles[0][2]),
            str(indicators_by_years[0][3]),
            [str(title[0]) for title in titles_id_by_years],
            [float(ind[4]) if type(ind[4]) == float else float(ind[5]) for ind in indicators_by_years],
            [float(ind[5]) if type(ind[4]) == float else float(ind[6]) for ind in indicators_by_years],
            str(rejection[0]),
            str(rejection[1]),
        ]

    def get_PM_indicators_names(self):
        indicators = list(set(indicator.title_id for indicator in self.session.query(Indicator).all()))
        indicators_names = []
        for ind_id in optimize_id_list(indicators):
            temp_ind_names = self.session.query(IndicatorsName).filter(
                IndicatorsName.id >= ind_id[0]
            ).filter(
                IndicatorsName.id <= ind_id[-1]
            ).all()
            for ind_name in temp_ind_names:
                indicators_names.append(ind_name.indicator_title)

        return indicators_names

    def get_PM_indicators(self):
        indicators = [
            [
                indicator.id,
                indicator.title_id,
                indicator.year_id,
                indicator.indicator,
                indicator.may_be_less,
                indicator.may_be_more
            ] for indicator in self.session.query(Indicator).all()
        ]

        return indicators

    def get_RP_indicators_names(self, schema_name):
        # ОЖИДАНИЕ ГОТОВЫХ РЕГИОНАЛЬНЫХ ПРОЕКТОВ
        pass

    def get_RP_indicators(self, schema_name):
        # ОЖИДАНИЕ ГОТОВЫХ РЕГИОНАЛЬНЫХ ПРОЕКТОВ
        pass

    def get_CYR_indicators_names(self):
        indicators = list(set(indicator.ind_title_rf for indicator in self.session.query(IndicationsRf).all())) + list(
            set(indicator.ind_title_vo for indicator in self.session.query(IndicationsVo).all()))

        return indicators

    def get_CYR_info(self, indicator_name):
        indicator_RF = self.session.query(IndicationsRf).filter(
            IndicationsRf.ind_title_rf == indicator_name
        ).first()
        indicator_VO = self.session.query(IndicationsVo).filter(
            IndicationsVo.ind_title_vo == indicator_name
        ).first()

        if indicator_RF is not None:
            indicator_RF_id = indicator_RF.id
            indicator_RF_id_task = indicator_RF.id_task
            indicator_VO_id = self.session.query(t_indications_rf_vo).filter(
                t_indications_rf_vo.c.id_ind_rf == indicator_RF_id
            ).first().id_ind_vo
        elif indicator_VO is not None:
            indicator_VO_id = indicator_VO.id
            indicator_RF_id = self.session.query(t_indications_rf_vo).filter(
                t_indications_rf_vo.c.id_ind_vo == indicator_VO_id
            ).first().id_ind_rf
            indicator_RF_id_task = self.session.query(IndicationsRf).filter(
                IndicationsRf.id == indicator_RF_id
            ).first().id_task
        else:
            raise ValueError("Не найден данный показатель в ЦУР")

        indicator_RF_target_id = self.session.query(t_indications_rf_target).filter(
            t_indications_rf_target.c.id_ind_rf == indicator_RF_id
        ).first().id_target
        cyr_id = self.session.query(Task).filter(
            Task.id == indicator_RF_id_task
        ).first().id_cyr
        tasks = self.session.query(Task).filter(
            Task.id_cyr == cyr_id
        ).all()
        task_number = [tasks.index(task) + 1 for task in tasks if task.id == indicator_RF_id_task][0]

        gosprogram_id = self.session.query(t_gosprogram_target).filter(
            t_gosprogram_target.c.id_target == indicator_RF_target_id
        ).first().id_prog
        response_obj_id = self.session.query(IndicationsVo).filter(
            IndicationsVo.id == indicator_VO_id
        ).first().id_response

        return [
            str(self.session.query(IndicationsRf).filter(
                IndicationsRf.id == indicator_RF_id
            ).first().ind_title_rf),
            f"{cyr_id}.{task_number}",
            str(self.session.query(Task).filter(
                Task.id == indicator_RF_id_task
            ).first().task),
            str(cyr_id),
            str(self.session.query(Cyr).filter(
                Cyr.id == cyr_id
            ).first().title_cyr),
            str(self.session.query(IndicationsVo).filter(
                IndicationsVo.id == indicator_VO_id
            ).first().ind_title_vo),
            str(self.session.query(Gosprogram).filter(
                Gosprogram.id == gosprogram_id
            ).first().title_prog),
            str(self.session.query(ResponseObj).filter(
                ResponseObj.id == response_obj_id
            ).first().response_obj)
        ]
