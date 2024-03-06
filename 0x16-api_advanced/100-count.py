#!/sur/bin/python3
"""contains a function"""
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """queries the reddit api and parses the title"""
    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0
    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    res = requests.get(url, headers=header, params=params, 
                       allow_redirects= False)
    if res.status_code != 200:
        return None
    try:
        hot_posts = res.json()['data']['childern']
        aft = res.json()['data']['after']
        for post in hot_posts:
            title = post['data']['title']
            lower = [word.lower() for word in title.split('')]
            for word in word_dict.keys():
                word_dict[word] += lower.count(word)
    except Exception:
        return None
    count_words(subreddit, word_list, aft, word_dict)
