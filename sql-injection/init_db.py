import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
id INTEGER PRIMARY KEY,
username TEXT,
password TEXT
)
""")

cursor.execute("INSERT INTO users VALUES (1,'admin','admin123')")
cursor.execute("INSERT INTO users VALUES (2,'alice','alice123')")

conn.commit()
conn.close()
