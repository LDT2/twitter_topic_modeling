import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import preprocessor as p
from nltk.corpus import stopwords
import nltk
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
import string
import spacy
import es_core_news_sm
import re

def preprocessing_text(text, lemmatize=True):
    '''
    INPUT: string tweet
    OUTPUT: str w/ emojis, urls, numbers, and reserved words removed
    '''
    def remove_symbols(word, symbol_set):
        return ''.join(char for char in word
                       if char not in symbol_set)

    def fix_lemmatized_hashtags(tweet):
        '''
        Lemmatizing function separates # and word.
        This function returns string that rejoins hashtags
        '''
        tokens = []
        for i, j in enumerate(tweet.split()):
            if j == '#':
                j = tweet.split()[i] + tweet.split()[i+1]
                tokens.append(j)
                continue
            if (tweet.split()[i-1] == '#'):
                continue
            elif j != '#':
                tokens.append(j)

        return ' '.join(tokens)

    # define stopwords
    stop_words_sp = stopwords.words('spanish')
    stop_words_en = stopwords.words('english')
    stop_words = stop_words_sp + stop_words_en + [' ']

    # define punctuation
    punct = set('!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~¿… °¡')

    # remove laughter
    matcher = re.compile(r'(ja)\1*')
    jaja = [match.group() for match in matcher.finditer(text)]
    jaja += ['lol', 'LOL', 'Lol', 'LoL']

    text = ' '.join([word for word in text.split() if word not in jaja])

    if lemmatize == True:
        # Lemmatize and rejoin
        nlp = es_core_news_sm.load()
        nlp_text = nlp(text)
        text = ' '.join([token.lemma_ for token in nlp_text])
        text = fix_lemmatized_hashtags(text)

    else:
        # Stem and rejoin
        stemmer = SnowballStemmer('spanish')
        text = ' '.join([stemmer.stem(token) for token in text.split()])

    # remove emojis, urls, numbers, and reserved words
    p.set_options(p.OPT.EMOJI, p.OPT.URL, p.OPT.NUMBER, p.OPT.RESERVED)
    clean_text = p.clean(text)

    # split tweet, remove stopwords, and len(words) <= 2
    clean_text = [word for word in clean_text.split()
                  if (remove_symbols(word, punct).lower() not in stop_words)
                  and (word not in punct)
                  and (len(remove_symbols(word, punct)) > 2)
                  and (p.clean(remove_symbols(word, punct)) != '')]

    clean_text = [word.lower() if word.startswith('@') else remove_symbols(word, punct).lower()
                  for word in clean_text]

    return clean_text
