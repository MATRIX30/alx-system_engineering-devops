#!/usr/bin/python3
"""Moddule to recursively get the list of titles of hot topics"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Write a recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should return
    None.

    Hint: The Reddit API uses pagination for separating pages of responses.

    Requirements:

    Prototype: def recurse(subreddit, hot_list=[])
    Note: You may change the prototype, but it must
 be able to be called with
    just a subreddit supplied. AKA you can add a counter,
 but it must work without
    supplying a starting value in the main.
    If not a valid subreddit, return None.
    NOTE: Invalid subreddits may return a redirect to search
 results. Ensure that
    you are not following redirects.
    Your code will NOT pass if you are using a loop and not
 recursively calling the
    function! This /can/ be done with a loop but the point is
 to use a recursive function. :)
    """

    if subreddit is None:
        return None
    if hot_list is None:
        hot_list = []

    header = {
        'User-Agent': 'alx-client/1.0'
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    param = {"after": after, "limit": 100}
    response = requests.get(
        url, headers=header, allow_redirects=False, params=param)

    if response.status_code != 200:
        return None

    data = response.json()

    if "data" not in data or data["data"]["children"] is None:
        return None
    for hot_topic in data["data"]["children"]:
        hot_list.append(hot_topic["data"]["title"])

    if "after" in data["data"] and data["data"]["after"] is not None:
        return recurse(subreddit, hot_list, data["data"]["after"])
    else:
        return hot_list
