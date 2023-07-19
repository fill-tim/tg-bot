import sqlite3 as sq

base = sq.connect('bot.db')
cur = base.cursor()


def create_db():
    start_db()
    usage_record()


def start_db():
    cur.execute("CREATE TABLE IF NOT EXISTS participant("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "chat_id INTEGER, "
                "first_name TEXT, "
                "user_id INTEGER, "
                "num INTEGER)")


def usage_record():
    cur.execute("CREATE TABLE IF NOT EXISTS usage_record("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "chat_id INTEGER, "
                "usage_time TEXT)")
