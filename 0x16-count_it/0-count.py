#!/usr/bin/python3
"""
Reddit API
"""


import requests


def count_words(subreddit, word_list, nextPage=None, dic={}):
    headers = {"User-Agent": "JadsyHB"}
    if nextPage:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, nextPage)
        res = requests.get(url, headers=headers, allow_redirects=False)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        titles = []

        for elem in res.json()['data']['children']:
            titles.append(elem['data']['title'])

        for word in word_list:
            word = word.lower()
            for title in titles:
                title_words = list(map(lambda x: x.lower(), title.split()))
                if word in title_words:
                    if word in dic:
                        dic[word] += title_words.count(word)
                    else:
                        dic[word] = title_words.count(word)

        nextPage = res.json()['data']['after']
        if nextPage:
            count_words(subreddit, word_list, nextPage, dic)
        else:
            sA = sorted(dic.items(), key=lambda x: x[0])
            s = sorted(sA.items(), key=lambda x: x[1], reverse=True)
            for i in s:
                print("{}: {}".format(i[0], i[1]))
    else:
        return
