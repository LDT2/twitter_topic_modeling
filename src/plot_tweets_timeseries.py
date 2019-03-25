import pandas as pd
import matplotlib.pyplot as plt

# Number of Tweets Over Time
df_time = pd.DataFrame(pd.to_datetime( tweets1["tweet_time"] ))

df_time["count"] = 1
df_time.set_index("tweet_time", inplace = True)

# hourly
hourly = df_time['count'].resample('H').sum()

# daily
daily = df_time.resample('D').sum()

# monthly
monthly = df_time['count'].resample('M').sum()

# plot num tweets over time
plt.figure(figsize=(25,8))
plt.plot(monthly)
plt.xlabel('YEARS', fontsize = 16)
plt.ylabel('Total No. Tweets', fontsize = 18)
plt.title('Monthly Number of Tweets\n2010 and 2019', fontsize = 16)
plt.savefig('../images/num_tweets_overtime.png')
