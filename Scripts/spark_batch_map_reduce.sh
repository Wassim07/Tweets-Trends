#!/bin/bash

spark-submit --packages org.mongodb:mongo-java-driver:3.6.3 --packages org.mongodb.spark:mongo-spark-connector_2.10:1.1.0 --driver-class-path  /root/mongo-hadoop/spark/build/libs/mongo-hadoop-spark-2.0.2.jar --driver-class-path /root/mongo-hadoop/build/libs/mongo-hadoop-2.0.2.jar --py-files /root/mongo-hadoop/spark/src/main/python/pymongo_spark.py /root/Code/Data-Processing/Batch/spark_batch_map_reduce.py > out
