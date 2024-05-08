#!/usr/bin/python3

"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import sys
import requests

def top_ten(subreddit):
    if not subreddit or not isinstance(subreddit, str):
        print("Invalid subreddit name.")
        return

    user_agent = {'User-Agent': 'Your User Agent'}  # Specify a valid User-Agent
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=user_agent, params=params)

        if response.status_code == 200:
            results = response.json()
            posts = results.get('data', {}).get('children', [])

            if not posts:
                print(f"No posts found in subreddit '{subreddit}'.")
                return

            for post in posts:
                print(post['data']['title'])
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

        subreddit = sys.argv[1]
        top_ten(subreddit)

