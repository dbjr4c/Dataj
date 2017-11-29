import json
import requests

API_KEY = '58ea8000-55a2-4ebe-8d01-dc5e0c8c8a56'

url = 'https://openstates.org/api/v1/bills/?state=mo&type=bill&search_window=session:2014&fields=title,created_at,updated_at,id,chamber,state,session,type,subjects,bill_id,actions'

def get_signed_bills():

    response = requests.get(url, headers={'X-API-KEY': API_KEY})

    data = json.loads(response.content)

    for bill in response:

        for action in bill['actions']:

    	    if action == 'governor:signed':

    		    return data

            else:

                return "there's nothing here"

get_signed_bills()
