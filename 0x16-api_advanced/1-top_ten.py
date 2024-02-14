#!/usr/bin/python3

def top_ten(subreddit):
    """
    Write a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.

    Requirements:
    Prototype: def top_ten(subreddit)
    If not a valid subreddit, print None.
    NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
    """
    import requests
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {
        'User-Agent': 'alx-client/1.0'
    }
    data = requests.get(url, allow_redirects=False, headers=header)
    if (data.status_code == 200):
        hot_topics = data.json()["data"]["children"]
        for item in hot_topics:
            print(item["data"]["title"])
    else:
        print(None)
