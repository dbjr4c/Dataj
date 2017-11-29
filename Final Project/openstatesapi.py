import json
import requests

apikey = '58ea8000-55a2-4ebe-8d01-dc5e0c8c8a56'

url = 'https://openstates.org/api/v1/bills/?state=mo&type=bill&search_window=session:2014&fields=title,created_at,updated_at,id,chamber,state,session,type,subjects,bill_id,actions'

def load_results():

	response = requests.get(url).content

    data = json.loads(response)

    for bill in the response:
    
        for action in bill['actions']:
        
            if action == 'governor:signed':
                return data
            
            else:
        	    return "there's nothing here"

get load_results()

