import sqlite3
from msilib.text import tables

DATABASE_NAME = "db_tekkom_0465.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_table_news():
    tables = [
        """CREATE TABLE IF NOT EXISTS
                tbl_students(
                    news_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    datetime TEXT NOT NULL,
                    flag TEXT NOT NULL)"""

    ]

    db = get_db()
    cursor = db.cursor()

    for table in tables:
        cursor.execute(table)