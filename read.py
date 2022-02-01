import os
from confluent_kafka import Producer
import time
from util import get_config


def read_send_message(src_dir):
    configs = get_config()
    p = Producer(configs['bootstrap.servers'])
    for entry in os.listdir(src_dir):
        # Trigger any available delivery report callbacks from previous produce() calls
        p.poll(0)
        file_dir = os.path.join(src_dir, entry)
        for filesInDir in os.listdir(file_dir):
            table_folder = os.path.join(file_dir, filesInDir)
            retail_db_files = open(table_folder)
            for line in retail_db_files:
                # Asynchronously produce a message, the delivery report callback
                # will be triggered from poll() above, or flush() below, when the message has
                # been successfully delivered or failed permanently.
                p.produce('retail_topic_1', key="key", value=line)
                print(f'{line} is produced')
                time.sleep(1)

            # Wait for any outstanding messages to be delivered and delivery report
            # callbacks to be triggered.
            p.flush()


