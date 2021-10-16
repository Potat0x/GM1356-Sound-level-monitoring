import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=13306,
    database="gm1356_monitoring"
)

cursor = db.cursor()

cursor.execute("select * from readings union select 'test', 'ok';")

for x in cursor:
    print(x)

def insert_reading(value, timestamp):
    sql = "insert into readings (_value, _timestamp) VALUES (%s, %s);"
    cursor.execute(sql, (value, timestamp))
    db.commit()
