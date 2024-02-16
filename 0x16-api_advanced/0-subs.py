#!/usr/bin/python3
"""Module to retrieve the number of subscribers for a subreddit"""


def number_of_subscribers(subreddit):
    """
    Write a function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given, the
    function should return 0.

    Hint: No authentication is necessary for most features of the Reddit
    API. If you’re getting errors related to Too Many Requests, ensure you’re
    setting a custom User-Agent.

    Requirements:

    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
    NOTE: Invalid subreddits may return a redirect to search results. Ensure
    that you are not following redirects.
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        'User-Agent': 'alx-client/1.0'
    }

    data = requests.get(url, headers=header, allow_redirects=False)
    status_code = data.status_code
    if (status_code == 200):
        return data.json()["data"]["subscribers"]
    return 0
