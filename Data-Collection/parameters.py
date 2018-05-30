stream_data_dir = "."
batch_data_dir = "."
count = 300 #batch_size

def get_stream_query():
    query = []
    with open("keywords.txt", 'r') as f:
        for line in f:
            for hashtag in line.split():
                query.append(hashtag)
                #query.append(hashtag+" #Startups")
    return query


def get_batch_query():
    query = ''
    with open("keywords.txt", 'r') as f:
        for line in f:
            for hashtag in line.split():
                #query += hashtag + " OR "
                query+=hashtag+ " #Startups OR "
    return query[:-4]


#--------------------------------------------------------------------------------------------
# Streaming API accepts an array of keywords
#
# However, Rest API (batch) accepts a string in which different keywords
# are seperated by 'OR'
# Example:
# query = #'AI OR #ArtificialIntelligence OR #MachineLearning OR #ML' \
#         'OR #DeepLearning OR #DL OR #DataMining OR #VR OR #VirtualReality' \
#         'OR #AR OR #AugmentedReality OR #BigData OR #DevOps '
#--------------------------------------------------------------------------------------------