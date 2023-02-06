import requests
import json

session_with_login = requests.Session()
session_with_login.auth = ('', '')

OWNER = 'xingyizhou'
REPO = 'CenterNet'
url = f'https://api.github.com/repos/{OWNER}/{REPO}/contents'

# def get_pull_requests(repo, token):
#     # Define the API endpoint and headers
#     endpoint = "https://api.github.com/graphql"
#     headers = {
#         "Authorization": f"bearer {token}",
#         "Content-Type": "application/json"
#     }
    
#     # Define the GraphQL query
#     query = """
#     query {
#       repository(name: "REPO_NAME", owner: "OWNER_NAME") {
#         pullRequests(first: 100, states: [OPEN]) {
#           edges {
#             node {
#               title
#             }
#           }
#         }
#       }
#     }
#     """
#     query = query.replace("REPO_NAME", repo.split("/")[1]).replace("OWNER_NAME", repo.split("/")[0])
    
#     # Send a POST request to the endpoint with the query in the request body
#     response = requests.post(endpoint, headers=headers, json={"query": query})
    
#     # If the request was successful, parse the JSON response
#     if response.status_code == 200:
#         data = json.loads(response.text)
#         pull_requests = [pr["node"]["title"] for pr in data["data"]["repository"]["pullRequests"]["edges"]]
#         return pull_requests
    
#     # If the request was not successful, raise an error
#     else:
#         raise Exception(f"Request failed with status code {response.status_code}")

def get_pull_requests(repo, num):
    endpoint = f"https://api.github.com/repos/{repo}/issues?per_page={num}"
    
    response = session_with_login.get(endpoint)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        pull_requests = [pr["title"] for pr in data]
        return pull_requests
    else:
        raise Exception(f"Request failed with status code {response.status_code}")
