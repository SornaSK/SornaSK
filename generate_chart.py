import matplotlib.pyplot as plt
import requests
from collections import Counter

# GitHub username and token
username = 'SornaSK'
token = ''  # Store securely in GitHub Secrets

# Fetch repositories data
response = requests.get(
    f'https://api.github.com/users/{username}/repos',
    auth=(username, token)
)
repos = response.json()

# Analyze tech stack based on language and keywords in topics
skills = Counter()
for repo in repos:
    language = repo['language']
    topics = repo.get('topics', [])
    
    if language:
        skills[language] += 1
    for topic in topics:
        skills[topic.capitalize()] += 1

# Generate pie chart
plt.figure(figsize=(8, 6))
plt.pie(skills.values(), labels=skills.keys(), autopct='%1.1f%%', startangle=140)
plt.title(f'{username}\'s Skill Distribution')
plt.savefig('skill_distribution.png')
