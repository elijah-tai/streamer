from kafka import KafkaConsumer

consumer = KafkaConsumer('streamer')

for msg in consumer:
    print(msg)
