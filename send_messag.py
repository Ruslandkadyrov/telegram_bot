import requests
import pymysql
import schedule
import time

def term_of_the_certificate_not_async():
    db_for_bot = pymysql.connect(host="", user="", password="", db='')
    cur = db_for_bot.cursor()
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
    return "\n".join(list_result)

def telegram_bot_sendtext():
    bot_token = ""
    chat_ID = ''
    message_from_sql = term_of_the_certificate_not_async()
    messege_from_bot = f""" Истекает срок действия удостоверения менее чем через месяц у следующих инженеров:
    {message_from_sql}"""
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_ID}&text={messege_from_bot}'
    if message_from_sql != '':
        response = requests.get(url)
        return response.json()

schedule.every().tuesday.at('15:00').do(telegram_bot_sendtext)
while True:
    schedule.run_pending()
    time.sleep(1)


