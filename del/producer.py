from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer
from time import sleep
from json import dumps


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
for e in range(1000):
    data = {'number' : e}
    producer.send(retail_topic_1, value=data)
    sleep(5)

