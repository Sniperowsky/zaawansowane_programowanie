import sys
import sqlite3

DB_FILE = "baza.db"


def init_db(con):
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL DEFAULT 'pending'
        )
        """
    )
    con.commit()


def add_job(con):
    cur = con.execute("INSERT INTO jobs (status) VALUES ('pending')")
    con.commit()
    print(f"Dodano zadanie {cur.lastrowid} (pending)")


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    con = sqlite3.connect(DB_FILE, timeout=10)
    init_db(con)
    for _ in range(count):
        add_job(con)
    con.close()