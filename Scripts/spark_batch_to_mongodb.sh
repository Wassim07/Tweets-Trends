#!/bin/bash

#spark-submit --packages org.mongodb.mongo-hadoop:mongo-hadoop-spark:1.5.2 /root/spark_batch.py >> out
spark-submit --packages org.mongodb:mongo-java-driver:3.6.3 --packages org.mongodb.spark:mongo-spark-connector_2.10:1.1.0 --driver-class-path  /root/mongo-hadoop/spark/build/libs/mongo-hadoop-spark-2.0.2.jar --driver-class-path /root/mongo-hadoop/build/libs/mongo-hadoop-2.0.2.jar --py-files /root/mongo-hadoop/spark/src/main/python/pymongo_spark.py /root/Code/Data-Processing/Batch/spark_batch_to_mongodb.py > out

#spark-submit --packages org.mongodb.spark:mongo-spark-connector:2.1.0 /root/spark_batch.py >> out
#spark-submit --packages org.mongodb.mongo-hadoop:mongo-hadoop-core:1.3.1,org.mongodb:mongo-java-driver:3.1.0 /root/spark_batch.py
#spark-submit /root/spark_batch.py > out
#spark-submit --master yarn --deploy-mode cluster --driver-memory 4g --executor-memory 2g --executor-cores 1 /root/spark_batch.py > out
