# Topic Modeling and Trend Analysis of Twitter's Elections Integrity Venezuelan Dataset
Exploratory text analysis to understand the hidden structures and themes of Twitter’s Elections Integrity Datasets

## Overview
Starting in October 2018, Twitter released a repository of data based on their investigations into foreign interference in US political conversations using their platform. Twitter identified and suspended a number of accounts who were affiliated with the Internet Research Agency (IRA) or originated from Iran, Russia, Venezuela, and Bangladesh. In an effort to improve transparency and to help the public understand the “alleged foreign influence” on US politics, Twitter has released data associated with the identified accounts.

My project focuses on using natural language processing to understand the topics and trends discussed in the Venezuelan dataset. I apply unsupervised learning to understand what topics were discussed and to see how this behavior could be linked back to suspicious activity on Twitter’s platform. 

## Data source
The data from this study comes from Twitter’s Election Integrity Datasets - https://about.twitter.com/en_us/values/elections-integrity.html#data

## Data processing
- Criteria for data inclusion: focus on 2016 US presidential election year; no retweets
- Develop iterative text processing pipeline for majority Spanish language tweets: building stopword corpus, removing URLs and emojis, lowercasing, tokenizing, remo ving symbols, removing accents, removing stopwords, creating bi/trigrams, lemmatizing words
- Data aggregation: tweets are text documents that inherently short due to character limitations. After removing URLs and special characters/words, individual tweets may be sparse and not contain enough information alone. Aggregating tweets by shared author can improve topic modeling of tweets.


## Data analysis and modeling
- In natural language processing, topic modeling is a common approach to understand the latent topics in a corpus of texts. This study used a Latent Dirichlet Allocation (LDA) method to extract the topics in Venezuelan Twitter dataset.

## Results 
- Topics corresponded with current events in 2016
- Spike in tweets related to US news could be considered as suspicious requiring further investigation

## Acknowledgments


