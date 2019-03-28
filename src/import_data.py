import pandas as pd
import numpy as np


def read_data(path, yr_start, yr_end, min_tweets):
    '''
    path (str): path to data files
    yr_start (int): start year of range to restrict data
    yr_end (int): end year of range to restrict data
    min_tweets (int): minimum number of tweets per user needed 
                to include in dataframe
    '''

    # read in data files
    data1 = pd.read_csv(path+'/venezuela_201901_1_tweets_csv_hashed.csv')
    data2 = pd.read_csv(path+'/venezuela_201901_2_tweets_csv_hashed.csv')

    # select variables to keep
    user_vars = ["tweetid", "userid", "user_display_name", "user_screen_name", "user_reported_location", "user_profile_description",
                "follower_count", "following_count", "account_creation_date"  ]
    tweet_vars = ["tweet_text", "tweet_time", "is_retweet", "retweet_userid", "retweet_tweetid", "hashtags", "urls", "user_mentions"]
    like_vars = ["reply_count", "like_count", "retweet_count" ]

    # filter dataframes
    data1_cleaned = data1[user_vars + tweet_vars + like_vars]
    data2_cleaned = data2[user_vars + tweet_vars + like_vars]

    # clean time variables
    data1_cleaned["tweet_time"] = pd.to_datetime(data1_cleaned["tweet_time"])
    data1_cleaned.set_index("tweet_time", inplace = True)
    data1_cleaned['year'] = data1_cleaned.index.year
    data1_cleaned['month'] = data1_cleaned.index.month

    data2_cleaned["tweet_time"] = pd.to_datetime(data2_cleaned["tweet_time"])
    data2_cleaned.set_index("tweet_time", inplace = True)
    data2_cleaned['year'] = data2_cleaned.index.year
    data2_cleaned['month'] = data2_cleaned.index.month

    # restrict dataframes to 2014-2018
    final1 = data1_cleaned[(data1_cleaned['year'] >= yr_start) & (data1_cleaned['year'] <= yr_end)]
    final2 = data2_cleaned[(data2_cleaned['year'] >= yr_start) & (data2_cleaned['year'] <=  yr_end)]

    # merge data1 and data2
    final = pd.concat([final1, final2])

    # count number of tweets for each user
    users_grp = final.groupby('userid')['tweet_text'].count().sort_values(ascending = False)
    users_grp = users_grp.reset_index()
    users_grp = users_grp.rename(index=str, columns={"tweet_text": "num_tweets"})

    final_ = pd.merge(final, users_grp, how = 'left', on = 'userid')

    # mask to filter min num tweets to keep
    keep_users = final_['num_tweets'] > min_tweets
    final_ = final_[keep_users]

    return final_