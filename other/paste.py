import openpyxl

# dict = {
#     ["наименование гос программы", "наименование показателя"]: [
#         [год, план, факт, ед.измерения],
#         [год, план, факт, ед.измерения]...
#     ]
# }


def parsing(dict):
    file = 'xlsx/Таблица 7.xlsx'
    book = openpyxl.open(file)
    sheet = book.active
    for i in range(9, 11):
        list_indicators = str(sheet['J' + str(i)].value).split('\n')
        if len(list_indicators) > 1:
            for indicator in list_indicators:
                if len(list_indicators) > 1 and indicator != list_indicators[0] and indicator != '':
                    print(indicator)
                    sheet['XEQ' + str(i)].value = str(sheet['XEQ' + str(i)].value) + '\n' + dict[indicator][0][3]
                    sheet['XER' + str(i)].value = str(sheet['XER' + str(i)].value) + '\n' + str(dict[indicator][0][1])
                    sheet['XES' + str(i)].value = str(sheet['XES' + str(i)].value) + '\n' + str(dict[indicator][0][2])
                    sheet['XET' + str(i)].value = str(sheet['XET' + str(i)].value) + '\n' + str(dict[indicator][1][1])
                    sheet['XEU' + str(i)].value = str(sheet['XEU' + str(i)].value) + '\n' + str(dict[indicator][1][2])
                    sheet['XEV' + str(i)].value = str(sheet['XEV' + str(i)].value) + '\n' + str(dict[indicator][2][1])
                    sheet['XEW' + str(i)].value = str(sheet['XEW' + str(i)].value) + '\n' + str(dict[indicator][2][2])
                    sheet['XEX' + str(i)].value = str(sheet['XEX' + str(i)].value) + '\n' + str(dict[indicator][3][1])
                    sheet['XEY' + str(i)].value = str(sheet['XEY' + str(i)].value) + '\n' + str(dict[indicator][3][2])
                    sheet['XEZ' + str(i)].value = str(sheet['XEZ' + str(i)].value) + '\n' + str(dict[indicator][4][1])
                    sheet['XFA' + str(i)].value = str(sheet['XFA' + str(i)].value) + '\n' + str(dict[indicator][5][1])
                    sheet['XFB' + str(i)].value = str(sheet['XFB' + str(i)].value) + '\n' + str(dict[indicator][6][1])
                elif indicator != '':
                    sheet['XEQ' + str(i)].value = dict[indicator][0][3]
                    sheet['XER' + str(i)].value = dict[indicator][0][1]
                    sheet['XES' + str(i)].value = dict[indicator][0][2]
                    sheet['XET' + str(i)].value = dict[indicator][1][1]
                    sheet['XEU' + str(i)].value = dict[indicator][1][2]
                    sheet['XEV' + str(i)].value = dict[indicator][2][1]
                    sheet['XEW' + str(i)].value = dict[indicator][2][2]
                    sheet['XEX' + str(i)].value = dict[indicator][3][1]
                    sheet['XEY' + str(i)].value = dict[indicator][3][2]
                    sheet['XEZ' + str(i)].value = dict[indicator][4][1]
                    sheet['XFA' + str(i)].value = dict[indicator][5][1]
                    sheet['XFB' + str(i)].value = dict[indicator][6][1]
        else:
            indicator = sheet['J' + str(i)].value
            sheet['XEQ' + str(i)].value = dict[indicator][0][3]
            sheet['XER' + str(i)].value = dict[indicator][0][1]
            sheet['XES' + str(i)].value = dict[indicator][0][2]
            sheet['XET' + str(i)].value = dict[indicator][1][1]
            sheet['XEU' + str(i)].value = dict[indicator][1][2]
            sheet['XEV' + str(i)].value = dict[indicator][2][1]
            sheet['XEW' + str(i)].value = dict[indicator][2][2]
            sheet['XEX' + str(i)].value = dict[indicator][3][1]
            sheet['XEY' + str(i)].value = dict[indicator][3][2]
            sheet['XEZ' + str(i)].value = dict[indicator][4][1]
            sheet['XFA' + str(i)].value = dict[indicator][5][1]
            sheet['XFB' + str(i)].value = dict[indicator][6][1]
    book.save('table7.xlsx')

# dict = { "11. Доля граждан, охваченных государственной социальной помощью на основании социального контракта, в общей численности малоимущих граждан (2021-2024)": [
# [2018, 1, 1, 'проц'],
# [2019, 1, 1, 'ед. измерения'],
# [2020, 1, 1, 'ghjwtyn'],
# [2021, 1, 1, 'ед. измерения'],
# [2022, 1, 1, 'ghjwtyn'],
# [2023, 1, 1, 'ед. измерения'],
# [2024, 1, 1, 'ед. измерения'],
# ], "12. Доля граждан, охваченных государственной социальной помощью на основании социального контракта, среднедушевой доход которых (среднедушевой доход "
#    "семьи которых) увеличился по окончании срока действия социального контракта в сравнении со среднедушевым доходом этих граждан (семьи) до заключения социального контракта, "
#    "в общей численности граждан, охваченных государственной социальной помощью на основании социального контракта (2021-2024)": [
# [2018, 1, 1, 'процент'],
# [2019, 1, 1, 'ед. измерения'],
# [2020, 1, 1, 'ghjwtyn'],
# [2021, 1, 1, 'ед. измерения'],
# [2022, 1, 1, 'ghjwtyn'],
# [2023, 1, 1, 'ед. измерения'],
# [2024, 1, 1, 'ед. измерения'],
#     ],
# "13 Доля граждан, охваченных государственной социальной помощью на основании социального контракта, среднедушевой доход которых (среднедушевой "
# "доход семьи которых) превысил величину прожиточного минимума, установленную в субъекте Российской Федерации, по окончании срока действия социального контракта в общей "
# "численности граждан, охваченных государственной социальной помощью на основании социального контракта (2021-2024)": [
# [2018, 50, 1, 'ghjwtynh'],
# [2019, 1, 60, 'ед. измерения'],
# [2020, 10, 1, 'ghjwtyn'],
# [2021, 1, 25, 'ед. измерения'],
# [2022, 123, 1, 'ghjwtyn'],
# [2023, 1, 5, 'ед. измерения'],
# [2024, 7, 1, 'ед. измерения']
# ],
# "6. Доля граждан, получивших меры социальной поддержки в виде субсидий, компенсаций, социальных выплат и "
# "государственной социальной помощи, в общей численности "
# "граждан, имеющих право на их получение и обратившихся за их получением  (2018-2024)": [
# [2018, 50, 1, 'tryryutt'],
# [2019, 1, 60, 'ед. измерения'],
# [2020, '-', 1, 'ghjwtyn'],
# [2021, 1, 25, 'ед. измерения'],
# [2022, 123, '-', 'ghjwtyn'],
# [2023, 1, 5, 'ед. измерения'],
# [2024, 70, 1, 'ед. измерения']
# ]
# }
# parsing(dict)
