import sys
import tweepy

consumer_key="VyPkKU9U33oircSBIZvffxchA"
consumer_secret="2h5aoGWbjTjrEHxooRVo9djwepNOjT2uRiIbQadLXanKfeCF8C"
access_key="841758106598146048-YTTT0NYq8gXU0U1YJyhEDFt169LtdSM"
access_secret="RHZ5KDu7Ca0nS2yLDNxTbkF4d6oZNNglmer5FJtfIZ77f"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if 'a' in status.text.lower():
            print (status.text,status.created_at,status.retweet_count,status.favorite_count)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations=[78.9629,20.5937,113.552971,22.210928])