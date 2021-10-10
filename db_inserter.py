import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    port=13306,
    database="spl_readings"
)

cursor = db.cursor()

cursor.execute("select * from readings limit 3;")

for x in cursor:
    print(x)


def insert_reading(value, timestamp):
    sql = "insert into readings (value, timestamp) VALUES (%s, %s)"
    cursor.execute(sql, (value, timestamp))
    db.commit()
