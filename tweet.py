import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'qFXllRbcNUnarP6aATv9dDEH5'
consumer_secret= 'Gt75nSJ0pmmNbtYA7dcCZY8KTWQLWXDtfcNLGmaxLeBjCek0pb'

access_token='703321353051611136-zzubrR2XpmEeusB203tHEJZhV2NsVlj'
access_token_secret='lbi3vKO5hkwgLBBv6XUA3SfykbqIB5JMJ5F11WmEzcccU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('ilem')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
