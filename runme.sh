export HADOOP_CONF_DIR="/etc/hadoop/conf"
export PYSPARK_PYTHON=python3
export ENVIRON=PROD
export SRC_DIR=/user/${user}/retail_json_data/
export TGT_FOLDER=''
export TGT_FILE_FORMAT=''
kafka-topics --create --partitions 1--replication-factor 1--topic quickstart-events --bootstrap-server cdp01.itversity.com:2181,cdp02.itversity.com:2181,cdp03.itversity.com:2181/kafka
spark-submit \
--master yarn \
--conf spark.ui.port=0 \
app.py

