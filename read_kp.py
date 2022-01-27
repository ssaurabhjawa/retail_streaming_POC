
from kafka import KafkaProducer
import time

fb=open('/Users/jai_dev/PycharmProjects/retail_poc/data/test_data/part-00000')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x:
                         bytes(x,'utf-8'))

for lines in fb:
    producer.send('retail_topic_1', value=lines)
    time.sleep(1)
producer.flush()

