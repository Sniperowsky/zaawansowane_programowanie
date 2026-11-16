"""Consumer: działa w pętli, co 5 s sprawdza plik i konsumuje zadania 'pending'.

Użycie:
    python consumer.py            # nazwa workera = PID
    python consumer.py operator1  # własna nazwa workera
"""
import contextlib
import csv
import os
import sys
import time

QUEUE_FILE = "queue.csv"
LOCK_FILE = QUEUE_FILE + ".lock"
FIELDS = ["id", "status", "created_at", "worker", "started_at", "finished_at", "payload"]

POLL_INTERVAL = 5   # co ile sekund sprawdzać plik, gdy nie ma pracy
JOB_DURATION = 30   # czas wykonania jednego zadania


def now() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


@contextlib.contextmanager
def file_lock(timeout=15.0, stale_after=30.0):
    """Wyłączny dostęp do pliku (atomowe tworzenie pliku .lock)."""
    start = time.time()
    while True:
        try:
            os.close(os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
            break
        except FileExistsError:
            try:
                if time.time() - os.path.getmtime(LOCK_FILE) > stale_after:
                    os.remove(LOCK_FILE)
                    continue
            except FileNotFoundError:
                continue
            if time.time() - start > timeout:
                raise TimeoutError("Nie udało się zdobyć blokady pliku kolejki")
            time.sleep(0.05)
    try:
        yield
    finally:
        with contextlib.suppress(FileNotFoundError):
            os.remove(LOCK_FILE)


def read_rows():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(rows):
    tmp = QUEUE_FILE + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, QUEUE_FILE)


def claim_job(worker):
    """Pod blokadą: pierwsze 'pending' -> 'in_progress'."""
    with file_lock():
        rows = read_rows()
        for row in rows:
            if row["status"] == "pending":
                row["status"] = "in_progress"
                row["worker"] = worker
                row["started_at"] = now()
                write_rows(rows)
                return dict(row)
    return None


def finish_job(job_id):
    """Pod blokadą: zadanie -> 'done'."""
    with file_lock():
        rows = read_rows()
        for row in rows:
            if row["id"] == job_id:
                row["status"] = "done"
                row["finished_at"] = now()
        write_rows(rows)


def main():
    worker = sys.argv[1] if len(sys.argv) > 1 else f"worker-{os.getpid()}"
    print(f"[{worker}] Start. Sprawdzam kolejkę co {POLL_INTERVAL}s. Ctrl+C aby zakończyć.")

    try:
        while True:
            job = claim_job(worker)
            if job is None:
                time.sleep(POLL_INTERVAL)
                continue

            print(f"[{worker}] {now()} START  id={job['id']} ({job['payload']})")
            time.sleep(JOB_DURATION)  # symulacja pracy (rozmowy)
            finish_job(job["id"])
            print(f"[{worker}] {now()} DONE   id={job['id']}")
    except KeyboardInterrupt:
        print(f"[{worker}] Zatrzymany.")


if __name__ == "__main__":
    main()