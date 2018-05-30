
Some useful links:
    https://www.programcreek.com/python/example/6809/tweepy.API
    http://docs.tweepy.org/en/v3.5.0/api.html#api-reference
    http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/

tweepy-Kafka:
	https://www.bmc.com/blogs/working-streaming-twitter-data-using-kafka/
Spark:
	https://www.bmc.com/blogs/reading-streaming-twitter-feeds-apache-spark/


before starting run the following cmd in order to install the required packages:

pip3 install -r requirements.txt


I) How to run streaming locally without using kafka (for test purpose):

comment everything related to kafka:
	
	producer.send(topic_name, str.encode(tweet))
	producer = KafkaProducer(bootstrap_servers='localhost:9092')
    	topic_name = 'tweets-trends'


uncomment the following lines:	

	#with open(self.outfile, 'a') as f:
	#    f.write(tweet + "\n")


then run: 
	python3 twitter_stream_download.py
a json file will be created in the same directory



II) How to run streaming on Docker with kafka:

- upload the src folder to docker using the following cmd:
	sudo docker cp src/ hadoop-trends-master:/root


- launch 3 terminals (T1,T2,T3) (using these commands :
					sudo docker exec -it hadoop-trends-master bash
					sudo docker start hadoop-trends-master
				)
T1)
launch the cluster then type:
	./start-kafka-zookeeper.sh

T2)
launch the cluster in other terminal and run:
	cd src
	python3 twitter_stream_download.py

T3)launch the cluster again then type:
	kafka-console-consumer.sh --zookeeper localhost:2181 --topic tweets-trends --from-beginning

