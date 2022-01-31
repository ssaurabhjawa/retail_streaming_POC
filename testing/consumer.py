from confluent_kafka import Consumer
from util import get_spark_session
from pyspark.sql.functions import date_format, to_date, split, substring
import getpass


def spark_consumer(env, appName):
    username = getpass.getuser()
    spark = get_spark_session(env, appName)
    kafka_bootstrap_servers = 'cdp03.itversity.com:9092,cdp04.itversity.com:9092,cdp05.itversity.com:9092'
    df = spark. \
        readStream. \
        format('kafka'). \
        option('kafka.bootstrap.servers', kafka_bootstrap_servers). \
        option('subscribe', 'retail_topic_1'). \
        option("startingOffsets", "earliest"). \
        load()


    df.selectExpr("CAST(key AS STRING) AS key", "CAST(value AS STRING) AS value").printSchema()
    df.printSchema()
    df.show(truncate=False)