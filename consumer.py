import os
import sys
import time
import sqlite3

DB_FILE = "baza.db"
POLL_INTERVAL = 5
JOB_DURATION = 30


def init_db(con):
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL DEFAULT 'pending'
        )
        """
    )


def take_job(con):
    con.execute("BEGIN IMMEDIATE")
    try:
        row = con.execute(
            "SELECT id FROM jobs WHERE status = 'pending' ORDER BY id LIMIT 1"
        ).fetchone()
        if row:
            con.execute(
                "UPDATE jobs SET status = 'in_progress' WHERE id = ?", (row[0],)
            )
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise
    return row[0] if row else None


def finish_job(con, job_id):
    con.execute("UPDATE jobs SET status = 'done' WHERE id = ?", (job_id,))


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else f"consumer-{os.getpid()}"
    con = sqlite3.connect(DB_FILE, timeout=10, isolation_level=None)
    init_db(con)
    print(f"[{name}] Start")
    while True:
        job_id = take_job(con)
        if job_id is None:
            print(f"[{name}] Brak pracy, czekam {POLL_INTERVAL}s...")
            time.sleep(POLL_INTERVAL)
            continue
        print(f"[{name}] Zadanie {job_id} -> in_progress")
        time.sleep(JOB_DURATION)
        finish_job(con, job_id)
        print(f"[{name}] Zadanie {job_id} -> done")