#!/bin/bash

echo "launching hadoop master container"
sudo docker start hadoop-master
sudo docker exec -it hadoop-master bash

