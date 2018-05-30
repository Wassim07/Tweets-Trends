#--------------------------------------------------------------------------------------------
# If we want to pass args from cmd instead of using parameters.py
# we have to change some of the code by restoring get_parser() function
# and run it as the following:
#
#   python twitter_stream_download.py -q "BigData MachineLearning" -d outputFolder
#
#   It will produce the list of tweets containing "#BigData" or "#MachineLearning" hashtags
#   in the file outputFolder/stream_BigData_MachineLearning.json
#--------------------------------------------------------------------------------------------


import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import twitter_credentials,parameters
import json
from kafka import KafkaProducer


class TweetsListener(StreamListener):

    #Custom StreamListener for streaming data
    def __init__(self, data_dir, api):
        self.api=api
        self.outfile = "%s/streaming_data.json" % (data_dir)

    def on_status(self, status):
        try:

            created_at = str(status.created_at)
            full_text = (status.extended_tweet["full_text"])[:-1].replace('\n', '')
            location = status.user.location
            id_str = status.id_str

            tweet = { 'created_at' : created_at,
                      'full_text' : full_text,
                      'location': location,
                      'id_str': id_str
                    }
            tweet=json.dumps(tweet)

            producer.send(topic_name, str.encode(tweet))
            #with open(self.outfile, 'a') as f:
            #    f.write(tweet + "\n")
        except AttributeError:
            return

    def on_error(self, status):
        print(status)
        return True



if __name__ == '__main__':
    #if we want to pass args from cmd instead of parameters.py
    #parser = get_parser()
    #args = parser.parse_args()

    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    topic_name = 'tweets-trends'

    hashtags = parameters.get_stream_query()

    print('Search will be done on the following hashtags :')
    for line in hashtags:
        print ('\t'+line)

    auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
    auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
    api = tweepy.API(auth)

    twitter_stream = Stream(auth, TweetsListener(parameters.stream_data_dir, api))
    twitter_stream.filter(track = hashtags , async = True)




    """""""""""""""
        def on_data(self, data):
            try:
                with open(self.outfile, 'a') as f:
                    #f.write(data)
                    aaa = jsonpickle.decode(data)
                    f.write(aaa["text"])
                    #print(aaa["entities"]["hashtags"])
                    return True
            except BaseException as e:
                print("Error on_data: %s" % str(e))
                time.sleep(5)
            return True
            
            
    
    
    
        def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                #f.write(data)
                aaa = jsonpickle.decode(data)
                f.write(aaa["text"])

                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True        
            
    """""""""""""""