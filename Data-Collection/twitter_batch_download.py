#--------------------------------------------------------------------------------------------
# If we want to pass args from cmd instead of using parameters.py
# we have to change some of the code by restoring get_parser() function
# and run it as the following:
#
#   python twitter_batch_download.py -q "BigData MachineLearning" -d outputFolder
#
#   It will produce the list of tweets containing "#BigData" or "#MachineLearning" hashtags
#   in the file outputFolder/batch_BigData_MachineLearning.json
#--------------------------------------------------------------------------------------------

import tweepy
from tweepy import OAuthHandler
import json
import twitter_credentials,parameters


def write_data(tweets):
    # --------------------------------------------------------------------------------------------
    # check this url to know more about Status class json format
    #       https://gist.github.com/dev-techmoe/ef676cdd03ac47ac503e856282077bf2
    # ---------------------------------------

    tweetCount = 0
    full_text = ''
    for tweet_info in tweets:
        tweetCount += 1

        id_str = tweet_info.id_str
        created_at = str(tweet_info.created_at)
        location = tweet_info.user.location

        if 'retweeted_status' in dir(tweet_info):
            full_text = tweet_info.retweeted_status.full_text[:-1].replace('\n', '')
        else:
            full_text = tweet_info.full_text[:-1].replace('\n', '')

        tweet = {
                 'created_at': created_at,
                 'full_text': full_text,
                 'location':location,
                 'id_str': id_str
                 }
        tweet = json.dumps(tweet)

        with open(outfile, 'a') as f:
            f.write(tweet+ "\n")
    # Display how many tweets we have collected
    print("Downloaded {0} tweets".format(tweetCount))



if __name__ == '__main__':
    outfile = "%s/batch_data.json" % (parameters.batch_data_dir)

    hashtags = parameters.get_batch_query()

    print('Search will be done on the following hashtags :')
    print ('\t'+hashtags.replace(' OR ','\n\t'))

    auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
    auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
    api = tweepy.API(auth)


    # we can add : ,since = "2015-10-10",until = "2015-10-11", lang = 'en')
    # to the following method, we can make it since last week for example
    tweets = tweepy.Cursor(api.search, q=hashtags, count=parameters.count, tweet_mode='extended').items(parameters.count)
    write_data(tweets)





#-----------------------------------------------------------------------
# check these urls :
#    http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/
#    http://docs.tweepy.org/en/v3.5.0/api.html#API.search
#-----------------------------------------------------------------------



"""""""""""""""""""""""
Filtering Data

tweetsgen = api.search(q=query, count=100)

       # Columns to retrieve and store from Twitter
       # Also, we use this to figure ou the index the id field when merging old and new tweets
       cols = ['id', 'created_at', 'text', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'retweeted',
               'retweet_count', 'favorited', 'favorite_count', 'source']

       tweets = [[getattr(t, x) for x in cols] for t in tweetsgen]
       table = pd.DataFrame(tweets, columns=cols)
       return table
"""""""""""""""""""""""