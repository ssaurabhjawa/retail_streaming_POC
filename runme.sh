export HADOOP_CONF_DIR="/etc/hadoop/conf"
export PYSPARK_PYTHON=python3
export ENVIRON=PROD
export SRC_DIR=/home/${USER}/retail_json_data/
export TGT_FOLDER=''
export TGT_FILE_FORMAT=''
spark-submit \
--master yarn \
--conf spark.ui.port=0 \
--py-files packages.zip \
--files configs/etl_config.json \
jobs/app.py



