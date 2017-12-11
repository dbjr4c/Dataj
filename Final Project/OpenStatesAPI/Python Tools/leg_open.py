import json
import requests

API_KEY = '58ea8000-55a2-4ebe-8d01-dc5e0c8c8a56'

def get_votes(): 

    data_list = []

    sponsor_id_list = ['MOL000471', 'MOL000434', 'MOL000386', 'MOL000465', 'MOL000398', 'MOL000030']

    for item in sponsor_id_list: 

        url = 'http://openstates.org/api/v1/bills/?state=mo&sponsor_id=' + item

        response = requests.get(url, headers={'X-API-KEY': API_KEY})

        if response.status_code == 200:
            # checks whether site exists and is running
            data = json.loads(response.content)

            data_list.append(data)
            
            # print data
            # you need to append each result to a bigger list becauase it will loop through all the id's in the sponsor list but it will only print the last one because you say "print data" instead of appending to a list and printing to a list 

        # else: 
        
        #     print "no information"

    # print data_list

    with open('bills.json', 'w') as output:
        json.dump(data_list, output)


get_votes()