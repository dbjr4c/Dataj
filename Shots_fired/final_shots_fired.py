import json
import requests
import pandas as pd
import numpy as np

API_KEY = 'AIzaSyAFKZBpWsSn3geoliJ8hNNRUMvTZO69slg'


def get_coordinates():

	df1 = pd.read_csv("address_apartment.csv", index_col="Address_Apartment")

	for item in df1:

		url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + item + 'MO'

		response = requests.get(url, headers={'X-API-KEY': API_KEY})

		raw_coordinates_list = json.loads(response.content)

		coordinates_list = raw_coordinates_list['results']

		for result in coordinates_list:

		    geometry = result['geometry']['location']

	    # # for coordinates in results_list:

	    # # 	exact_coordinates = coordinates['location']
	
    # coordinates_list_fuck.append(geometry['lat']) 
	    # coordinates_list_fuck.append(geometry['lng'])

		print geometry, len(item)

		# with open('test.json', 'w') as output:
  #   		json.dump(geometry, output)

    	



