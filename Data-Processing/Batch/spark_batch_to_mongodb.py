from pyspark import SparkContext,SparkConf
import pymongo_spark
import json


def containsStartupHashtags(x):
    if "#Startup" in x or "#startup" in x or "#Startups" in x or "#startups" in x:
        return true

def cleanData(x):
    x = json.loads(x)
    tweet = { "created_at" : x["created_at"],
              "full_text" : x["full_text"],
              "location": x["location"]
            }
    tweet=json.dumps(tweet)
    return tweet


# Important: activate pymongo_spark.
pymongo_spark.activate()


conf = SparkConf().setAppName('SparkBatch').setMaster('local[2]')
sc=SparkContext(conf = conf)

sc.textFile('/root/data/*')\
    .map(lambda x: cleanData(x))\
    .filter(lambda x: "#startups" in x or "#Startups" in x or "#startup" in x or "#Startup" in x)\
    .saveToMongoDB('mongodb://wassimB:123456@ds129540.mlab.com:29540/bigdata.tweets')
