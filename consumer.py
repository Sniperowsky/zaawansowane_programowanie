import os
import sys
import pika

RABBIT_HOST = "localhost"
RABBIT_PORT = 8081
QUEUE = "jobs"
JOB_DURATION = 30


def make_callback(name, con):
    def on_message(ch, method, properties, body):
        job_id = body.decode()
        print(f"[{name}] Zadanie {job_id} -> in_progress")
        con.sleep(JOB_DURATION)  # sleep, który podtrzymuje połączenie (heartbeat)
        ch.basic_ack(delivery_tag=method.delivery_tag)  # potwierdzenie = done
        print(f"[{name}] Zadanie {job_id} -> done")

    return on_message


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else f"consumer-{os.getpid()}"

    con = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT)
    )
    channel = con.channel()
    channel.queue_declare(queue=QUEUE, durable=True)

    # bierz tylko jedno zadanie naraz, następne dopiero po ack
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE, on_message_callback=make_callback(name, con))

    print(f"[{name}] Start, czekam na zadania...")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    con.close()