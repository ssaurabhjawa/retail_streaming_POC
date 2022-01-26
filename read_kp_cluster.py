
from kafka import KafkaProducer
import time

fb=open('/Users/jai_dev/PycharmProjects/retail_poc/data/test_data/part-00000')

producer = KafkaProducer(bootstrap_servers=['cdp01.itversity.com:2181,cdp02.itversity.com:2181,cdp03.itversity.com:2181'],
                         value_serializer=lambda x:bytes(x,'utf-8'))
producer.flush()

for lines in fb:
    producer.send('retail_topic_1', value=lines)
    time.sleep(1)
producer.flush()

