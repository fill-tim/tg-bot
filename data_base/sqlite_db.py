import sqlite3 as sq


base = sq.connect('bot.db')
cur = base.cursor()


def start_db():
    cur.execute("CREATE TABLE IF NOT EXISTS participant("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "chat_id INTEGER, "
                "user_name TEXT, "
                "user_id INTEGER, "
                "num INTEGER)")


