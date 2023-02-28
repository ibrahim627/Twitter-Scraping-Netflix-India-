!pip install -q snscrape

#Import The Modulus Tools For Scraping
import snscrape.modules.twitter as sntwitter
import pandas as pd
import numpy as np

#Give Which Tweets & How Many Tweets WE Want
Username = "Netflix India"
Numbers= int(input())

#Create An Empty List For Storing An Items
Tweets_Data=[]

#Iterate The Collecting Items From There By Using Some Key Words..
#When Stop The Collection if The Condition Becomes Satisfied

for tweet in sntwitter.TwitterSearchScraper(Username).get_items():
 if len(Tweets_Data)==Numbers:
     break
  
 Tweets_Data.append ([tweet.date,tweet.id,tweet.url,tweet.content,tweet.user,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount])  

#Convert A List Into Data Frame By Using Pandas Library
df = pd.DataFrame(Tweets_Data, columns = ["DATE","ID","URL","CONTENT","USER","REPLYCOUNT","RETWEETCOUNT","LANG","SOURCE","LIKECOUNT"])  
df.to_csv('Twitter Scraped Data.csv', index = False)
