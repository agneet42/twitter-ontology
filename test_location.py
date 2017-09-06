'''import tweepy

ckey = "VyPkKU9U33oircSBIZvffxchA"
csecret = "2h5aoGWbjTjrEHxooRVo9djwepNOjT2uRiIbQadLXanKfeCF8C"
atoken = "841758106598146048-YTTT0NYq8gXU0U1YJyhEDFt169LtdSM"
asecret = "RHZ5KDu7Ca0nS2yLDNxTbkF4d6oZNNglmer5FJtfIZ77f"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,
 'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])'''
import tweepy

auth = tweepy.OAuthHandler("VyPkKU9U33oircSBIZvffxchA","2h5aoGWbjTjrEHxooRVo9djwepNOjT2uRiIbQadLXanKfeCF8C")
auth.set_access_token("841758106598146048-YTTT0NYq8gXU0U1YJyhEDFt169LtdSM", "RHZ5KDu7Ca0nS2yLDNxTbkF4d6oZNNglmer5FJtfIZ77f")
api = tweepy.API(auth)

# place = api.geo_search(query="Mumbai",granularity ="city")
# place_id = place[0].id
# cricTweet = tweepy.Cursor(api.search, q='cricket', geocode="-22.9122,-43.2302,1km").items(10)

tweets = api.search(q="GST",geocode="-22.9122,-43.2302,1km")
for tweet in tweets:
   print (tweet.created_at,tweet.text,tweet.retweet_count)
