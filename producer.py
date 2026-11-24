import sys
import pika

RABBIT_HOST = "localhost"
RABBIT_PORT = 8081
QUEUE = "jobs"


def add_job(channel, job_id):
    channel.basic_publish(
        exchange="",
        routing_key=QUEUE,
        body=str(job_id),
        properties=pika.BasicProperties(delivery_mode=2),
    )
    print(f"Dodano zadanie {job_id} (pending)")


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    con = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT)
    )
    channel = con.channel()
    channel.queue_declare(queue=QUEUE, durable=True)

    for i in range(1, count + 1):
        add_job(channel, i)

    con.close()