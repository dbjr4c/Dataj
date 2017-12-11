import json
import requests

API_KEY = '58ea8000-55a2-4ebe-8d01-dc5e0c8c8a56'

url = 'https://openstates.org/api/v1/bills/?state=mo&type=bill&search_window=session:2017'

response = requests.get(url, headers={'X-API-KEY': API_KEY})

data = json.loads(response.content)

print len(data)