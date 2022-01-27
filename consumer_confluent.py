from confluent_kafka import Consumer


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