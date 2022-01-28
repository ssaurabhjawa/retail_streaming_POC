import os
from kafka import KafkaProducer
import time

# List all files in a directory using os.listdir
def read_send_message(src_dir):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: bytes(x, 'utf-8'))

    for entry in os.listdir(src_dir):
        file_dir = os.path.join(src_dir, entry)
        for filesInDir in os.listdir(file_dir):
            table_folder = os.path.join(file_dir,filesInDir)
            retailDB_files=open(table_folder)
            for line in retailDB_files:
                producer.send('retail_topic_1', value=line)
                time.sleep(1)
            producer.flush()

read_send_message('/Users/jai_dev/PycharmProjects/retail_poc/data/retail-topic/')


"""
# List all files in a directory using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)



src_directories = os.listdir(src_dir)
print(src_directories)
for d_entry in src_directories:
    file=open(os.path.join(src_dir,d_entry))
    if os.path.isfile(f'{file}'):
        print(True)
    else:
        print(False)
        
import os



        
"""
"""
def read_from_files(src_dir):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x:bytes(x, 'utf-8'))
    src_directories=os.lisdir(src_dir)
    for d_entry in src_directories:
        if os.path.isfile(os.path.join(src_directories, d_entry)):
            print(src_directories/d_entry)
            src_file=open(src_dir/d_entry)
            for lines in src_file:
                producer.send('retail_topic_1', value=lines)
                time.sleep(1)
            producer.flush()

"""