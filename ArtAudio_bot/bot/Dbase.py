import sqlite3
import os
from config import BASE_DIR, DATABASE, path_with_db

# Main path for db
PATH = os.path.join(BASE_DIR, DATABASE)

# Need fot testing db
TEST_PATH = path_with_db()


def connect():
    conn = sqlite3.connect(TEST_PATH)
    return conn


def create_db():
    conn = connect()
    cursor = conn.cursor()

    sql = """ CREATE TABLE IF NOT EXISTS settings(
            path TEXT NOT NULL,
            exit_path TEXT NOT NULL
           
    ) """

    cursor.execute(sql)
    conn.commit()


def update_path(path, exit_path):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(f""" UPDATE settings SET path='{path}', exit_path='{exit_path}' """)

    cursor.close()
    connection.commit()


def select_path():

    connection = connect()
    cursor = connection.cursor()

    sql = """ SELECT * FROM settings"""

    cursor.execute(sql)

    result = cursor.fetchone()

    if result:
        return result
    return ''


def select_path_videos():

    connection = connect()
    cursor = connection.cursor()

    sql = """ SELECT path FROM settings"""

    cursor.execute(sql)

    result = cursor.fetchone()

    if result:
        return result[0]
    return ''


def select_exit_path():

    connection = connect()
    cursor = connection.cursor()

    sql = """ SELECT exit_path FROM settings"""

    cursor.execute(sql)

    result = cursor.fetchone()

    if result:
        return result[0]
    return ''


def insert_path(path, exit_path):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(""" INSERT INTO settings VALUES(?,?)""", (path, exit_path,))

    cursor.close()
    connection.commit()
