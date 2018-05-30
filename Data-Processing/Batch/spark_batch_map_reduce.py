from pyspark import SparkContext,SparkConf
from pymongo import MongoClient
import pymongo_spark
import json


hashtags = ["#AI", "#ArtificialIntelligence", "#MachineLearning", "#ML", "#DeepLearning", "#DL", "#DataMining", "#VR", "#VirtualReality", "#AR","#AugmentedReality","#BigData","#DevOps"]
hashtags_lowercased = ["#ai", "#artificialintelligence", "#machinelearning", "#ml", "#deeplearning", "#dl", "#datamining", "#vr", "#virtualreality","#ar", "#augmentedreality","#bigdata","#devops"]


def get_hashtag(x):
    if x.lower() in hashtags_lowercased:
        for hashtag in hashtags:
            if hashtag.lower() == x.lower():
                return hashtag


# Important: activate pymongo_spark.
pymongo_spark.activate()


conf = SparkConf().setAppName('SparkBatch').setMaster('local[2]')
sc=SparkContext(conf = conf)


#Reading
mongo_rdd = sc.mongoRDD('mongodb://wassimB:123456@ds129540.mlab.com:29540/bigdata.tweets')\
          .map(lambda x: json.loads(x['value'])['full_text'])\
          .flatMap(lambda x: x.split()) \
          .filter(lambda x: x.lower() in hashtags_lowercased) \
          .map(lambda x: (get_hashtag(x),1)) \
          .reduceByKey(lambda x,y:x+y) \
          .saveToMongoDB('mongodb://wassimB:123456@ds129540.mlab.com:29540/bigdata.hashtags')
