import csv
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

with open("users.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""
            INSERT INTO users (name, email)
            VALUES (?, ?)
        """, (row["name"], row["email"]))

conn.commit()

print("\nUsers stored in SQLite database:\n")
cursor.execute("SELECT * FROM users")
for user in cursor.fetchall():
    print(f"ID: {user[0]} | Name: {user[1]} | Email: {user[2]}")

conn.close()
