import json
import requests

API_KEY = '58ea8000-55a2-4ebe-8d01-dc5e0c8c8a56'

def get_boone_votes():

	output_list = []

	boone_id_list = ['MOL000471', 'MOL000434', 'MOL000386', 'MOL000465', 'MOL000398', 'MOL000101', 'MOL000339', 'MOL000030', 'MOL000186']

	for item in boone_id_list:

		url = 'http://openstates.org/api/v1/bills/?state=mo&sponsor_id=' + item + '&fields=bill_id,sponsors'

		response = requests.get(url, headers={'X-API-KEY': API_KEY})

		if response.status_code == 200:

				data = json.loads(response.content)

				output_list.append(data)

				print len(data)

    		# print data

	with open('all_boone_bills.json', 'w') as output:
		json.dump(output_list, output)


get_boone_votes()















# https://openstates.org/api/v1/bills/?state=mo&sponsor_id=MOL000101&fields=session,bill_id,sponsors&apikey=58ea8000-55a2-4ebe-8d01-dc5e0c8c8a56
