import requests
import subprocess

session_with_login = requests.Session()
session_with_login.auth = ('', '')

OWNER = 'xingyizhou'
REPO = 'CenterNet'

def get_contributors_activity(owner, repo):
    headers = {'Accept': 'application/vnd.github+json'}
    url = f'https://api.github.com/repos/{owner}/{repo}/stats/contributors'
    response = session_with_login.get(url, headers=headers)
    return response.json()

contributors_activity = get_contributors_activity(OWNER, REPO)
score = len(contributors_activity) / 100
print(round(score, 1))