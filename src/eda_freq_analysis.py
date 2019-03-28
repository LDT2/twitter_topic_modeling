import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import collections
import math

'''
# Frequency Analysis
- Count top hashtags
- Count tagged-users (mentions)
- Count URLs
- Count top words (not implemented yet)
'''

def top_hashtags(df, top_n):
    hashtags = collections.Counter()
    for tweet in df["hashtags"]:
        if tweet == '[]':
            hashtags[tweet] += 1
        elif type(tweet) == float:
            pass
        else:
            tweet = str.split(tweet[1:-1].lower(),", ")
            for item in tweet:
                hashtags[item] += 1
    return hashtags.most_common()[:top_n]
    
def top_mentions(df, top_n):
    mentions = collections.Counter()
    for tweet in df["user_mentions"]:
        if tweet == '[]':
            mentions[tweet] += 1
        elif type(tweet) == float:
            pass
        else:
            tweet = str.split(tweet[1:-1],", ")
            for item in tweet:
                mentions[item] += 1
    return mentions.most_common()[:top_n]

def top_urls(df, top_n):
    urls = collections.Counter()
    for tweet in df["urls"]:
        if tweet == '[]':
            urls[tweet] += 1
        elif type(tweet) == float:
            pass 
        else:
            tweet = str.split(tweet[1:-1].split("//")[1],"/")[0]
            #for item in tweet:
            urls[tweet] += 1
    return urls.most_common()[:top_n]

# Data Preprocessing
data["tweet_time"] = pd.to_datetime(data["tweet_time"])
data.set_index("tweet_time", inplace = True)
data['year'] = data.index.year
data['month'] = data.index.month

final = data[(data['year'] >=2014) & (data['year'] <= 2018)]

top_stats = collections.defaultdict()
for year in final['year'].unique():
    temp = final[ final['year'] == year ]
    
    yr_hashtags = 'hashtags_'+str(year)
    top_stats[yr_hashtags] = top_hashtags(temp, 20)
    
    yr_mentions = 'mentions_'+str(year)
    top_stats[yr_mentions] = top_mentions(temp, 20)
    
    yr_urls = 'urls_'+str(year)
    top_stats[yr_urls] = top_urls(temp, 20)

