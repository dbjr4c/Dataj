import json
import requests
import csv

API_KEY = 'AIzaSyAFKZBpWsSn3geoliJ8hNNRUMvTZO69slg'

f = open('address_apartment.csv')
csv_f = csv.reader(f)

output_list = []
for item in csv_f:

    # Opens the csv

    # print item

    str1 = ''.join(item)

    # print str1

    # turns the list into a string that I can put in the url 

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + str1 + ' COLUMBIA, MO' + '&key=' + API_KEY

    response = requests.get(url)

    raw_coordinates_list = json.loads(response.content)

    coordinates_list = raw_coordinates_list['results']

    for result in coordinates_list:

            geometry = result['geometry']['location']

            lat = geometry['lat']
            lng = geometry['lng']

            output_list.append([str1, lat, lng])

    # print output

with open('test_2.json', 'w') as output:
    json.dump(output_list, output)


        



