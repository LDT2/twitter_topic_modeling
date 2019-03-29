def preprocessing_text(text, lemmatize = True):
    '''
    INPUT: str
    OUTPUT: str w/ emojis, urls, numbers, and reserved words removed
    '''    
    def remove_symbols(word, symbol_set):
        return ''.join(char for char in word 
                     if char not in symbol_set)
    
    # define stopwords
    stop_words_sp = stopwords.words('spanish')
    stop_words_en = stopwords.words('english')
    stop_words = stop_words_sp + stop_words_en + [' ']
    
    # define punctuation
    punct = set('!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~¿… °¡')
    
    if lemmatize == True:
        # Lemmatize and rejoin
        nlp_text = nlp(text)
        text = ' '.join([token.lemma_ for token in nlp_text ])
    else:
        # Stem and rejoin
        stemmer = SnowballStemmer('spanish')
        text = ' '.join([stemmer.stem(token) for token in text.split() ])
    
    # remove emojis, urls, numbers, and reserved words
    p.set_options(p.OPT.EMOJI, p.OPT.URL, p.OPT.NUMBER, p.OPT.RESERVED)
    clean_text = p.clean(text)
    
    # split tweet, remove stopwords, and len(words) <= 2
    clean_text = [ word for word in clean_text.split() 
                          if (remove_symbols(word, punct).lower() not in stop_words) \
                              and (word not in punct) \
                              and (len(remove_symbols(word, punct)) > 2) \
                              and (p.clean(remove_symbols(word, punct)) != '')]

    clean_text = [ word.lower() if word.startswith('@') else remove_symbols(word, punct).lower()
                  for word in clean_text ]
    
    return clean_text 