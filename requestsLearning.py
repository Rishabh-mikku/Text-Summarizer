import requests
# response = requests.get("https://api.github.com")
# response.encoding = "UTF-8"
# print(response.json())
# print(response.headers)
# print(response.headers['content-type'])
# print(response.headers['X-GitHub-Request-Id'])

response = requests.get(
    "https://api.github.com/search/repositories",
    params={
        "q": "language:python",
        "sort": "stars",
        "order": "desc"
    })
json_response = response.json()
# print(json_response)
popular_repositories = json_response["items"]
# print(popular_repositories)

# Inspecting top three repositories
for repo in popular_repositories[:3]:
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}")
    print()
