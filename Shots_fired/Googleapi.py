import json
import requests
import csv

API_KEY = 'AIzaSyAFKZBpWsSn3geoliJ8hNNRUMvTZO69slg'

f = open('address_apartment.csv')
csv_f = csv.reader(f)

for item in csv_f:

	# Opens the csv

	str1 = ''.join(item)

	# turns the list into a string that I can put in the url 

	url = 'https://maps.googleapis.com/maps/api/geocode/json?address' + str1 + 'MO'

	response = requests.get(url, headers={'X-API-KEY': API_KEY})

	raw_coordinates_list = json.loads(response.content)

	coordinates_list = raw_coordinates_list['results']

# coordinates_list = []

	for result in coordinates_list:

    		geometry = result['geometry']['location']

    		# This nested loop pulls only the lat and lng items from the location dict

    # coordinates_list_.append(geometry['lat']) 
    # coordinates_list_.append(geometry['lng'])

	# # print coordinates_list

with open('test.json', 'w') as output:
    	json.dump(geometry, output)

    	



