#!/bin/bash

python3 twitter_batch_download.py
#hadoop fs -put ./batch_data.json /root/Data
hdfs dfs -appendToFile ./batch_data.json /root/Data/batch_data.json
rm batch_data.json
