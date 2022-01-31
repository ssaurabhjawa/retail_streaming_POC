import json
from json import dumps, dump
import time

filename= '/data/test_data/part-00000'
fb=open('/data/test_data/part-00000')
"""
for line in fb:
    print(line)

with open(filename,'rb') as f:
    lines_f=f.read()
print(lines_f)
"""

for lines in fb:
    print(lines)
    time.sleep(2)


"""
fb=open('/Users/jai_dev/PycharmProjects/retail_poc/data/test_data/part-00000')
with open(filename,'rb') as f:
    lines=f.read()
print(type(lines))
"""

"""
with open(filename,'rb') as f:
    lines=f.read()
with open("retail_j.json", 'w') as rj:
    json.dumps(lines.decode("utf-8"))
"""

"""
fb=open('/home/saurabh/test_source/part-00000')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
"""


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