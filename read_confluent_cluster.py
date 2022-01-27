
from confluent_kafka import Producer
import time

fb = open('/home/saurabh/part-00000')

p = Producer({'bootstrap.servers': 'cdp03.itversity.com:9092,cdp04.itversity.com:9092,cdp05.itversity.com:9092'})


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


for data in fb:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('retail_topic_1', key="key", value="value", callback=delivery_report)
    time.sleep(1)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()
