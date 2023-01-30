import requests
import re
from bs4 import BeautifulSoup

session_with_login = requests.Session()
session_with_login.auth = ('qing0git', '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')

OWNER = 'xingyizhou'
REPO = 'CenterNet'
url = f'https://api.github.com/repos/{OWNER}/{REPO}/contents'

def get_lines_of_code(url):
    response = session_with_login.get(url)
    files = response.json()
    slocs = 0

    for file in files:
        if file['type'] == 'file' and '.py' in file['name']:
            html_source_code = requests.get(file['html_url'])
            soup = BeautifulSoup(source_code.text, 'html.parser')
            string_contain_sloc = soup.findAll(string=re.compile(r'\(\d+ sloc\)'))[0]
            slocs += int(re.findall(r"\d+", string_contain_sloc)[1])
        elif file['type'] == 'dir':
            url = file['url']
            slocs += get_lines_of_code(url)
    return slocs

slocs = 0
slocs = get_lines_of_code(url)
print(f'Total lines of code: {slocs}')