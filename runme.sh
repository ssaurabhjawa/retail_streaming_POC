export HADOOP_CONF_DIR="/etc/hadoop/conf"
export PYSPARK_PYTHON=python3
export ENVIRON=PROD
export SRC_DIR=/home/${USER}/retail_json_data/

spark-submit --master yarn --properties-file /home/{USER}/retail_streaming_POC/configs/streaming_retail_data.conf git app.py
