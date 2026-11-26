import requests
import sqlite3

url = "https://openlibrary.org/search.json?q=python&limit=10"
response = requests.get(url, timeout=20)

if response.status_code == 200:
    data = response.json()
    print("API data fetched successfully.")

    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    """)

    cursor.execute("DELETE FROM books")

    for book in data.get("docs", []):
        title = book.get("title", "Unknown")
        author = (book.get("author_name") or ["Unknown"])[0]
        publication_year = (book.get("publish_year") or [None])[0]

        cursor.execute("""
            INSERT INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
        """, (title, author, publication_year))

    conn.commit()

    print("\nBooks stored in SQLite database:\n")
    cursor.execute("SELECT id, title, author, publication_year FROM books")
    for book in cursor.fetchall():
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Year: {book[3]}")

    conn.close()
else:
    print("Failed to fetch data.")
    print("Status Code:", response.status_code)
