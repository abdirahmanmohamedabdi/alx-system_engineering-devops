#!/usr/bin/python3
"""a function that queries the reddut api"""
import requests

def number_of_subscribers(subreddit):
    """returns number of subscribers in reddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent':'request'}
    response = requests.get(url, headers=headers, allows_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    num_subs = data.get("subscribers")
    return num_subs
