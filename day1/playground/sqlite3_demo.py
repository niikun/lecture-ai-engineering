import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS test (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT)"""
)

c.execute("INSERT INTO test (name) VALUES('niikun')")
c.execute("INSERT INTO test (name) VALUES('sankun')")
c.execute("INSERT INTO test (name) VALUES('yonkun')")

conn.commit()

# データを取り出す
c.execute('SELECT * FROM test')
for row in c.fetchall():
    print(row)

conn.close()