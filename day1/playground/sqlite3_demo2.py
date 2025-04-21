import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()


# データを取り出す
c.execute('SELECT * FROM test')
for row in c.fetchall():
    print(row)

conn.close()