import json
import requests

API_KEY = '58ea8000-55a2-4ebe-8d01-dc5e0c8c8a56'

def get_votes(): 

    sponsor_id_list = ['MOL000471', 'MOL000434', 'MO000386', 'MOL000465', 'MOL000389']

    for item in sponsor_id_list: 

        url = 'http://openstates.org/api/v1/bills/?state=mo&sponsor_id=' + item

        response = requests.get(url, headers={'X-API-KEY': API_KEY})

        if response.status_code == 200:
            # checks whether site exists and is running
            data = json.loads(response.content)
            print data, len(item)

            with open('boone_county.json', 'w') as output:
                json.dump(data, output)

get_votes()