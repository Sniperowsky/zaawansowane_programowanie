"""Producer: dopisuje do pliku kolejki zadania (rozmowy) o statusie 'pending'.

Użycie:
    python producer.py              # 1 uruchomienie = 1 rekord (1 rozmowa)
    python producer.py --count 100  # wrzuca 100 zadań naraz (do testów)
"""
import argparse
import contextlib
import csv
import os
import time

QUEUE_FILE = "queue.csv"
LOCK_FILE = QUEUE_FILE + ".lock"
FIELDS = ["id", "status", "created_at", "worker", "started_at", "finished_at", "payload"]


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=1, help="ile zadań dodać (domyślnie 1)")
    args = parser.parse_args()

    with file_lock():
        rows = read_rows()
        next_id = max((int(r["id"]) for r in rows), default=0) + 1
        for i in range(args.count):
            job_id = next_id + i
            rows.append({
                "id": job_id,
                "status": "pending",
                "created_at": now(),
                "worker": "",
                "started_at": "",
                "finished_at": "",
                "payload": f"Rozmowa telefoniczna #{job_id}",
            })
        write_rows(rows)

    print(f"[producer] Dodano {args.count} zadań (id {next_id}..{next_id + args.count - 1}), status=pending")


if __name__ == "__main__":
    main()