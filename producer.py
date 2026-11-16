import os
import sys
import time
from contextlib import contextmanager

QUEUE_FILE = "queue.csv"
LOCK_FILE = "queue.lock"


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


def add_job():
    with lock():
        job_id = 1
        if os.path.exists(QUEUE_FILE):
            with open(QUEUE_FILE) as f:
                job_id = len(f.readlines()) + 1
        with open(QUEUE_FILE, "a") as f:
            f.write(f"{job_id},pending\n")
    print(f"Dodano zadanie {job_id} (pending)")


if __name__ == "__main__":
    # python producer.py        -> 1 zadanie
    # python producer.py 100    -> 100 zadań
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for _ in range(count):
        add_job()