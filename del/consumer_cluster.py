import json
from kafka import KafkaConsumer

def kafka_consumer(env, appName):
    c = Consumer({
        'bootstrap.servers': 'cdp03.itversity.com:9092,cdp04.itversity.com:9092,cdp05.itversity.com:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    })
    c.subscribe(['retail_topic_1'])
    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print('Received message: {}'.format(msg.value().decode('utf-8')))
    c.close()





consumer = KafkaConsumer(
    'retail_topic_1',
     bootstrap_servers=['cdp03.itversity.com:9092,cdp04.itversity.com:9092,cdp05.itversity.com:9092'],
     api_version=(20, 2, 1),
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: x.decode('utf-8'))


for message in consumer:
    print(type(message))
    message1 = message.value
    print(message1)

