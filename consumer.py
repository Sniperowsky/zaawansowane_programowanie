import os
import sys
import time
from contextlib import contextmanager

QUEUE_FILE = "queue.csv"
LOCK_FILE = "queue.lock"
POLL_INTERVAL = 5   # co ile sekund sprawdzamy plik
JOB_DURATION = 30   # czas wykonania jednej pracy


@contextmanager
def lock():
    """Prosty lock oparty o plik - tylko jeden proces naraz modyfikuje kolejkę."""
    while True:
        try:
            fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL)
            break
        except FileExistsError:
            time.sleep(0.05)
    try:
        yield
    finally:
        os.close(fd)
        os.remove(LOCK_FILE)


def read_jobs():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE) as f:
        return [line.strip().split(",") for line in f if line.strip()]


def write_jobs(jobs):
    with open(QUEUE_FILE, "w") as f:
        for job_id, status in jobs:
            f.write(f"{job_id},{status}\n")


def take_job():
    """Znajduje pierwszą pracę pending i zmienia jej status na in_progress."""
    with lock():
        jobs = read_jobs()
        for job in jobs:
            if job[1] == "pending":
                job[1] = "in_progress"
                write_jobs(jobs)
                return job[0]
    return None


def finish_job(job_id):
    with lock():
        jobs = read_jobs()
        for job in jobs:
            if job[0] == job_id:
                job[1] = "done"
        write_jobs(jobs)


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else f"consumer-{os.getpid()}"
    print(f"[{name}] Start")
    while True:
        job_id = take_job()
        if job_id is None:
            print(f"[{name}] Brak pracy, czekam {POLL_INTERVAL}s...")
            time.sleep(POLL_INTERVAL)
            continue
        print(f"[{name}] Zadanie {job_id} -> in_progress")
        time.sleep(JOB_DURATION)
        finish_job(job_id)
        print(f"[{name}] Zadanie {job_id} -> done")