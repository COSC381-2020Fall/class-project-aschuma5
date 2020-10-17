from pathlib import Path
import json

paths = [str(x) for x in Path('./youtube_data').glob('**/*.json')]
results = []
for path in paths:
    with open(path, 'r') as f:
        data = json.load(f)
        #insert code here
        identity = data["items"][0]["id"]
        title = data["items"][0]["snippet"]["title"]
        desc = data["items"][0]["snippet"]["description"]
        diction = {"video id": identity, "title": title, "description": desc}
        results.append(diction)
        #print(data["items"][0]["id"])
        # insert your code here

with open('data_for_indexing.json', 'w') as dump_file:
    json.dump(results, dump_file)
