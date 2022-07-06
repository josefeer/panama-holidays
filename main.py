import csv
import json
import os
import requests

headers = {
	"X-RapidAPI-Key": os.environ['API_KEY'],
	"X-RapidAPI-Host": "public-holiday.p.rapidapi.com"
}

holidays = []

for i in range(2022, 2122):
	url = 'https://public-holiday.p.rapidapi.com/{}/PA'.format(i)
	response = requests.request("GET", url, headers=headers)
	print('url: {}; responde code: {}'.format(url, response.status_code))
	values = json.loads(response.text)
	holidays += values

with open('holidays.csv', 'w') as csvfile:
	fieldnames = ['date', 'name', 'countryCode']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for holiday in holidays:
		writer.writerow({'date': holiday['date'], 'name': holiday['name'], 'countryCode': holiday['countryCode']})

print('done')

"""
	References
	1. https://docs.rapidapi.com/docs/api-pricing
	2. https://rapidapi.com/theapiguy/api/public-holiday/
"""