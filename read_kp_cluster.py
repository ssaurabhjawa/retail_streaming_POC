
from kafka import KafkaProducer
import time

fb=open('/home/saurabh/part-00000')

producer = KafkaProducer(bootstrap_servers=['cdp01.itversity.com:2181,cdp02.itversity.com:2181,cdp03.itversity.com:2181'],
                         api_version=(20, 2, 1),
                         value_serializer=lambda x:bytes(x,'utf-8'))
producer.flush()

for lines in fb:
    producer.send('retail_topic_1', value=lines)
    time.sleep(1)
producer.flush()

