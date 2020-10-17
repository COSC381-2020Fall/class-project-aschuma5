import pprint
import json
from googleapiclient.discovery import build
import config

my_api_key = config.data_keys['api_key']
my_cse_id = config.data_keys['cse_key']

my_search_topic = config.data_keys['my_search_topic']

resource = build("customsearch", 'v1', developerKey=my_api_key).cse()

output = []

for i in range(1, 100, 10):
    result = resource.list(q = my_search_topic , cx=my_cse_id, start = i).execute()
    output += result['items']


for i in output:
    pprint.pprint(i)


