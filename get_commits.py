"""Get commits.

Usage:
  get_commits.py [PATH] [--since=<date>] [--token=<github-token>] [--user=<github-usernamae>]
  get_commits.py (-h | --help)
  get_commits.py --version

Options:
  -h --help                    Show this screen.
  --version                    Show version.
  -s <date> , --since <date>   Commits since date(ISO 8601).
  -t <token>, --token <token>  Token to access GitHub API.
  -u <user> , --user  <user>   Github username

"""
from docopt import docopt
import requests
import json
from datetime import datetime, timedelta

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Get Commits 1.0')

    # declarations

    owner = 'helm'
    repo = 'charts'
    token = arguments['--token']
    username = arguments['--user']
    path = arguments['PATH']
    since = arguments['--since']

    # validations
    if username is None:
        raise Exception('Github username is required')

    if token is None:
        raise Exception('Github token is required')

    # defaults
    if since is None:
        yesterday = datetime.now() - timedelta(1)
        since = yesterday.isoformat()
    
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    if path is None:
        payload = {'since': since}
    else:
        payload = {'path': path, 'since': since}

    r = requests.get(url, auth=(username, token), params=payload)

    if r.status_code != 200:
        raise Exception('Request to GitHub API failed')

    commits = json.loads(r.text)

    print("{} new commits.\n".format(len(commits)))

    if commits:
        for c in commits:
            msg = c['commit']['message']
            subject = msg.splitlines()[0].strip()
            print(subject)