import json
from kafka import KafkaConsumer



consumer = KafkaConsumer(
    'retail_topic_1',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: x.decode('utf-8'))


"""
consumer = KafkaConsumer(
    'retail_topic_1',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))
consumer.subscribe(['retail_topic_1'])



consumer = KafkaConsumer(
    'retail_topic_1',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')))
"""
for message in consumer:
    message = message.value
    print(message)

