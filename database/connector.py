import os
import mysql.connector


def connect():
    db_host = os.environ['MYSQL_HOST']
    db_user = os.environ['MYSQL_USER']
    db_password = os.environ['MYSQL_PASSWORD']
    db_name = os.environ['MYSQL_DATABASE']

    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    return db, db.cursor()


def disconnect(cursor, connection):
    cursor.close()
    connection.close()
