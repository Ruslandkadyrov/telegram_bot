import pymysql
import schedule
import time

def delete_row():
    db = pymysql.connect(host="", user="", password="", db= '')
    cursor = db.cursor()
    query = """DELETE FROM Аттестация"""
    cursor.execute(query)
    cursor.close()
    db.commit()
    db.close()

delete_row()

# schedule.every().monday.at('12:39').do(delete_row)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

