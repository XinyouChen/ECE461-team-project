import requests
import json

session_with_login = requests.Session()
session_with_login.auth = ('', '')

OWNER = 'xingyizhou'
REPO = 'CenterNet'
TOKEN = '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'

def get_issues(owner, repo):
    endpoint = f"https://api.github.com/repos/{owner}/{repo}/issues?per_page=100"
    
    response = session_with_login.get(endpoint)
    
    if response.status_code == 200:

        data = json.loads(response.text)
        total = 0
        count = 0
        for issue in data:
            issue_endpoint = issue["comments_url"]
            issue_response = session_with_login.get(issue_endpoint)
            if issue_response.status_code == 200:
                total += 1
                if issue_response.text == '[]':
                    count += 1
            else:
                raise Exception(f"Request for issue events failed with status code {issue_response.status_code}")
        return total, count
    else:
        raise Exception(f"Request failed with status code {response.status_code}")

total, count = get_issues(OWNER, REPO)
score = 1 - count / total
print(round(score, 1))