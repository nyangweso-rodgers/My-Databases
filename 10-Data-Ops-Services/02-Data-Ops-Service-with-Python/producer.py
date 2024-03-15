import os as os
import time
from time import sleep
import random
import json
from kafka import KafkaProducer

KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:8098")
KAFKA_TOPIC_TEST = os.environ.get("test-kafka-topic", "test-topic")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.6.0")
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
    api_version=KAFKA_API_VERSION,
)
i = 0
while i <= 30:
    producer.send(
        KAFKA_TOPIC_TEST,
        json.dumps({"message": f"Hello, Kafka! - test {i}"}).encode("utf-8"),
    )
    i += 1
    time.sleep(random.randint(1, 5))
producer.flush()