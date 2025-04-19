import sqlite3

with sqlite3.connect("test.db") as conn:  
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT)"""
    )

    c.execute("INSERT INTO test (name) VALUES('niikun')")
    c.execute("INSERT INTO test (name) VALUES('sankun')")
    c.execute("INSERT INTO test (name) VALUES('yonkun')")

    # データを取り出す
    c.execute('SELECT * FROM test')
    for row in c.fetchall():
        print(row)
