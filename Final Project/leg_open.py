import json
import requests

API_KEY = '58ea8000-55a2-4ebe-8d01-dc5e0c8c8a56'

def get_votes(session): 

    sponsor_id_list = ['MO:00471', 'MOL00434', 'MO000386', 'MOL00465', "MOL000389"]

	for item in sponsor_id_list: 

		url = 'openstate.org/api/v1/bills/mo/{session}/{sponsor_id}'

	 	response = request.get(url, headers={'session': session, 'sponsor_id': item})

	 	if response.status_code == 200:
    		# checks whether site exists and is running
    		data = json.loads(response)
    		print data

    	else: 
    		print "no information"

