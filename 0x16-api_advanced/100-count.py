#!/usr/bin/python3
""" recursive function"""
import requests
import sys
after = None
count_dic = []


def count_words(subreddit, word_list):
    """prints given words """
    global after
    global count_dic
    headers = {'User-agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    paramters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
