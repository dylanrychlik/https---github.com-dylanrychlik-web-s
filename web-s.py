#import json and request
import json
import requests

#load the url you want to scrap
url = 'https://www.visitnh.gov/BusinessListingService.asmx/GetUsers'
#enter the search paramters to gather the data
search_params = {"searchParams":{"ResultsPerPage":15,"BusinessType":"attraction","SubcategoryID":25}}
#load the data into the json
data = json.loads(requests.post(url, json=search_params).json()['d'])

# print the json
#print(json.dumps(data, indent=4))




#print the data
for result in data['Results']:
    print(result['BusinessName'])
    print(result['Address'])
    print(result['Phone'])
    print('-' * 80)

with open('restraunts.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

	


