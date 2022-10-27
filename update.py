import xlrd
import pymysql
import schedule
import time

def update_row():
    book = xlrd.open_workbook('/Users/ruslan/Downloads/Мои проекты по прогр-ию/полевики июнь 2021 — копия.xls')
    sheet = book.sheet_by_index(0)
    db = pymysql.connect(host="", user="", password="", db= '')
    cursor = db.cursor()
    query = """INSERT INTO Аттестация (
    ФИО, 
    Должность, 
    Охрана_труда,
    Оказание_1_помощи_пострадавшим,
    Пожарно_технический_минимум,
    Электробезопасность,
    Стропальщик,
    Высота,
    ГНВП,
    Промышленная_безопасность,
    Промышленная_безопасность_2
    ) VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    for r in range (0, sheet.nrows):
        ФИО = sheet.cell(r, 0).value
        Должность = sheet.cell(r, 1).value
        Охрана_труда = xlrd.xldate_as_datetime(sheet.cell(r, 2).value, 0)
        Оказание_1_помощи_пострадавшим = xlrd.xldate_as_datetime(sheet.cell(r, 3).value, 0)
        Пожарно_технический_минимум = xlrd.xldate_as_datetime(sheet.cell(r, 4).value, 0)
        Электробезопасность = xlrd.xldate_as_datetime(sheet.cell(r, 5).value, 0)
        Стропальщик = xlrd.xldate_as_datetime(sheet.cell(r, 6).value, 0)
        Высота = xlrd.xldate_as_datetime(sheet.cell(r, 7).value, 0)
        ГНВП = xlrd.xldate_as_datetime(sheet.cell(r, 8).value, 0)
        Промышленная_безопасность = xlrd.xldate_as_datetime(sheet.cell(r, 9).value, 0)
        Промышленная_безопасность_2 = xlrd.xldate_as_datetime(sheet.cell(r, 10).value, 0)

        values = (ФИО, Должность, Охрана_труда, Оказание_1_помощи_пострадавшим, Пожарно_технический_минимум, Электробезопасность, Стропальщик, Высота, ГНВП, Промышленная_безопасность, Промышленная_безопасность_2)

        cursor.execute(query, values)

    cursor.close()

    db.commit()

    db.close()

update_row()

# schedule.every().monday.at('12:43').do(update_row)
# while True:
#     schedule.run_pending()
#     time.sleep(1)




