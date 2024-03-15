import os
from kafka import KafkaConsumer

KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:8098")
KAFKA_TOPIC_TEST = os.environ.get("KAFKA_TOPIC_TEST", "test-topic")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.6.0")
consumer = KafkaConsumer(
    KAFKA_TOPIC_TEST,
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
    api_version=KAFKA_API_VERSION,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
)
for message in consumer:
    print(message.value.decode("utf-8"))