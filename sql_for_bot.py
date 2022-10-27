import pymysql

async def db_connect() -> None:
    global db_for_bot, cur
    db_for_bot = pymysql.connect(host="", user="", password="", db='')
    cur = db_for_bot.cursor()

async def get_all_ingeners(name):
    query = """ select ФИО, Должность, Охрана_труда, Оказание_1_помощи_пострадавшим, Пожарно_технический_минимум, Электробезопасность, Стропальщик, Высота, ГНВП, Промышленная_безопасность, Промышленная_безопасность_2  FROM Аттестация where ФИО = %s """
    cur.execute(query, name)
    ingeners = cur.fetchall()
    for i in ingeners:
        return f"""{i[0]}
Должность - {i[1]} 
Охрана_труда до {i[2]} 
Первая_помощь до {i[3]}
ПТМ до {i[4]}
Электробезопасность до {i[5]}
Стропальщик до {i[6]}
Высота до {i[7]}
ГНВП до {i[8]} 
Промбезопасность до {i[9]} 
Промбезопасность_2 до {i[10]} """

async def term_of_the_certificate():
    query = """ SELECT ФИО
FROM Аттестация
WHERE Охрана_труда < CURRENT_DATE + 30 or
Оказание_1_помощи_пострадавшим < CURRENT_DATE + 30 or
Пожарно_технический_минимум < CURRENT_DATE + 30 or
Электробезопасность < CURRENT_DATE + 30 or
Стропальщик < CURRENT_DATE + 30 or
Высота < CURRENT_DATE + 30 or
ГНВП < CURRENT_DATE + 30 or
Промышленная_безопасность < CURRENT_DATE + 30 or
Промышленная_безопасность_2 < CURRENT_DATE + 30 """
    cur.execute(query)
    result = cur.fetchall()
    list_result = []
    for i in result:
        for x in i:
            list_result.append(x)
    return f"""Истекает срок действия удостоверения менее чем через месяц у следующих инженеров:
{"; ".join(list_result)} """




