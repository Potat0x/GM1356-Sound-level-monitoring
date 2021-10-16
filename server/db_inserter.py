import mysql.connector
import time
from logger import log_info, log_error

database = None
cursor = None


def connect_to_db():
    global database
    global cursor
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=13306,
        database="gm1356_monitoring"
    )
    cursor = database.cursor()


def run_test_query():
    cursor.execute("SELECT * FROM readings UNION SELECT 'test', 'ok' limit 3;")
    for record in cursor:
        log_info("read test data: " + str(record))


def try_reconnect_to_database_infinitely():
    while True:
        try:
            log_info("trying to reconnect database")
            time.sleep(1)
            connect_to_db()
            run_test_query()
            break
        except Exception as e:
            log_error("reconnect to database failed" + str(e))


def insert_reading(value, timestamp):
    sql = "INSERT INTO readings (_value, _timestamp) VALUES (%s, %s);"
    try:
        cursor.execute(sql, (value, timestamp))
        database.commit()
    except Exception as e:
        log_error("insert to database failed" + str(e))
        try_reconnect_to_database_infinitely()


try_reconnect_to_database_infinitely()
