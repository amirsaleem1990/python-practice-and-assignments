import json
import pprint

with open('info.json') as data_file:    
    data = json.load(data_file)
pprint(data)

