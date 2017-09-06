#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import datetime
import xlsxwriter
import sys

# credentials from https://apps.twitter.com/

auth = tweepy.OAuthHandler("VyPkKU9U33oircSBIZvffxchA","2h5aoGWbjTjrEHxooRVo9djwepNOjT2uRiIbQadLXanKfeCF8C")
auth.set_access_token("841758106598146048-YTTT0NYq8gXU0U1YJyhEDFt169LtdSM","RHZ5KDu7Ca0nS2yLDNxTbkF4d6oZNNglmer5FJtfIZ77f")

api = tweepy.API(auth)

username = sys.argv[1]
startDate = datetime.datetime(2017, 9, 4, 0, 0, 0)
endDate =   datetime.datetime(2017, 9, 5, 0, 0, 0)

tweets = []
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

workbook = xlsxwriter.Workbook(username + ".xlsx")
worksheet = workbook.add_worksheet()
row = 0
for tweet in tweets:
    if("gst" in tweet.text.lower()):
        worksheet.write_string(row, 0, str(tweet.id))
        worksheet.write_string(row, 1, str(tweet.created_at))
        worksheet.write(row, 2, tweet.text)
        worksheet.write(row,3,tweet.retweet_count)
        worksheet.write(row,4,tweet.favorite_count)
        row += 1

workbook.close()
print("Excel file ready")
