from kafka.admin import KafkaAdminClient, NewTopic
import json
from pyspark.sql import SparkSession
from kafka import KafkaProducer
from json import dumps, dump
import time




filename='/Users/jai_dev/PycharmProjects/retail_poc/data/test_data/part-00000'
fb=open('/Users/jai_dev/PycharmProjects/retail_poc/data/test_data/part-00000')
"""
with open(filename,'rb') as f:
    lines=f.read()
with open("retail_j.json", 'w') as rj:
    json.dumps(lines.decode("utf-8"))
"""


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x:
                         bytes(str(x),'utf-8'))
producer.flush()

for lines in fb:
    producer.send('retail_topic_1', value=lines)
    time.sleep(1)
producer.flush()


"""
fb=open('/home/saurabh/test_source/part-00000')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
"""