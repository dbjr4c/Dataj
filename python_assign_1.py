import urllib2, csv
from bs4 import BeautifulSoup

output_file = open('highway.csv', 'w')
writer = csv.writer(output_file)

url = "https://www.mshp.dps.missouri.gov/HP68/search.jsp"

html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

table = soup.find('table', {'class': 'accidentOutput'})

for tr in table.find_all('tr'):

	td_list = tr.find_all('td')

	data = [cell.text for cell in td_list]

	writer.writerow(data)

