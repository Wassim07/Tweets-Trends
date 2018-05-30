from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.streaming.kafka import KafkaUtils
from firebase import firebase
import json

hashtags = ["#AI", "#ArtificialIntelligence", "#MachineLearning", "#ML", "#DeepLearning", "#DL", "#DataMining", "#VR", "#VirtualReality", "#AR", "#AugmentedReality", "#BigData", "#DevOps"]
hashtags_lowercased = ["#ai", "#artificialintelligence", "#machinelearning", "#ml", "#deeplearning", "#dl", "#datamining", "#vr", "#virtualreality", "#ar", "#augmentedreality", "#bigdata", "#devops"]

def get_hashtag(x):
    if x.lower() in hashtags_lowercased:
        for hashtag in hashtags:
            if hashtag.lower() == x.lower():
                return hashtag

def process(firebase,rdd):
    print("Starting to process")
    tweets=rdd.collect()
    totalHashtags=len(tweets)
    print("TOTAL Hashtags: ",totalHashtags)

    firebase.post('/tweets_counts',tweets)

if __name__ == '__main__':
    print("------ RUNNING SPARK STREAMING APP ------")
    firebase = firebase.FirebaseApplication('https://tweets-trends.firebaseio.com/')
    print("--- CONNECTED TO FIREBASE ---")


    conf = SparkConf().setAppName('SparkKafkaWordCount').setMaster('local[2]')
    sc=SparkContext(conf = conf)
    sqlContext = SQLContext(sc)
    ssc = StreamingContext(sc, 5) # 5 seconds window
    zkQuorm = "localhost:2181"
    topic = "tweets-trends"
    messages = KafkaUtils.createStream(ssc, \
                                  zkQuorm, \
                                  'test',{topic:1})


    lines = messages.map(lambda x: json.loads(x[1])['full_text'])\
        .flatMap(lambda x: x.split()) \
        .filter(lambda x: x.lower() in hashtags_lowercased) \
        .map(lambda x: (get_hashtag(x),1)) \
        .reduceByKey(lambda x,y:x+y) \
        .foreachRDD(lambda rdd: process(firebase,rdd))

    ssc.start()
    ssc.awaitTermination()