'''
Grab URL Content
'''

import requests
from bs4 import BeautifulSoup

def grab_urls(tweet):
    return [ word for word in tweet.split() \
                    if word.startswith("http")]

def grab_url_content(url):
    url = url
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    title = soup.find('title').decode()
    title = title[7:-8]   
    return title

def grab_all_url_conent(urls):
    content = []
    for url in urls:
        if len(url) == 0:
            return ""
        result = grab_url_content (url)
        if result == 'Twitter / Account Suspended':
            result = ''
        content.append( result )
    return content
