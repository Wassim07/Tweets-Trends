#!/bin/bash

spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.0 /root/Code/Data-Processing/Stream/spark_streaming.py > out
