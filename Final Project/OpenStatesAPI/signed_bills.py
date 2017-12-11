import json
import requests


# output_file = open('sponsor.csv', 'w')
# writer = csv.writer(output_file)

API_KEY = '58ea8000-55a2-4ebe-8d01-dc5e0c8c8a56'

url = 'https://openstates.org/api/v1/bills/?state=mo&type=bill&search_window=session:2012&fields=title,created_at,updated_at,id,chamber,state,session,type,subjects,bill_id,actions,sponsors'

response = requests.get(url, headers={'X-API-KEY': API_KEY})

bill_list = json.loads(response.content)

action_signed_bill_list = []

for bill in bill_list:
	
	action_list = bill['actions']

	for action in action_list:

		action_signed = action['action']

		if action_signed == "Signed by Governor" or action_signed == "Delivered to Secretary of State (G)" or action_signed == "Legislature voted to override Governor's veto":

			action_signed_bill_list.append(bill['sponsors'])
			action_signed_bill_list.append(bill['bill_id'])
			# writer.writerow(action_list)

print action_signed_bill_list
print len(action_signed_bill_list)

with open('signed_bills_12.json', 'w') as output:
    json.dump(action_signed_bill_list, output)


https://openstates.org/api/v1/bills/?state=mo&type=bill&search_window=session:2012&fields=title,created_at,updated_at,id,chamber,state,session,type,subjects,bill_id,actions,sponsors&apikey=58ea8000-55a2-4ebe-8d01-dc5e0c8c8a56