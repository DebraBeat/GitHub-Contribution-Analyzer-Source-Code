import requests
from datetime import datetime
from pprint import pprint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

username = input("Input github username: ")
user_event_str = f"https://api.github.com/users/{username}/events"

response = requests.get(user_event_str, headers=headers) # Added headers here just in case
response.raise_for_status()

events_data = response.json()

print(f"--- Commit History for {username} ---\n")

for event in events_data[:5]: # Checking more than one in case the first isn't a push
    if event['type'] == 'PushEvent':
        created_at = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        repo_name = event['repo']['name']
        
        # Use 'head' as the commit SHA
        commit_sha = event['payload'].get('head')
        
        if commit_sha:
            # Construct the URL using the repo name provided in the event
            commit_url = f"https://api.github.com/repos/{repo_name}/commits/{commit_sha}"
            
            commit_res = requests.get(commit_url, headers=headers)
            if commit_res.status_code == 200:
                commit_data = commit_res.json()
                
                print(f"Repo:       {repo_name}")
                print(f"SHA:        {commit_sha[:7]}") # Shortened for readability
                print(f"datetime:   {created_at}")
                print(f"Message:    {commit_data['commit']['message'].splitlines()[0]}")
                print("-" * 40)
            else:
                print(f"Could not fetch commit details for {repo_name}")
