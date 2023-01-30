import requests

session_with_login = requests.Session()
session_with_login.auth = ('qing0git', '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')

OWNER = 'xingyizhou'
REPO = 'CenterNet'
url = f'https://api.github.com/repos/{OWNER}/{REPO}/contents'

def get_lines_of_code(url):
    response = session_with_login.get(url)
    files = response.json()
    num_syntax_error = 0

    for file in files:
        if file['type'] == 'file' and '.py' in file['name']:
            #check syntax
            file_url = file["download_url"]
            file_response = requests.get(file_url)
            file_content = file_response.text
            try:
                exec(file_content)
            except Exception as e:
                if 'invalid syntax' in str(e):
                    print(str(e))
                    num_syntax_error += 1
        elif file['type'] == 'dir':
            url = file['url']
            num_syntax_error += get_lines_of_code(url)
    return num_syntax_error

num_syntax_error = 0
num_syntax_error = get_lines_of_code(url)
print(f'Total syntax error: {num_syntax_error}')