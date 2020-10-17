
import pprint
from googleapiclient.discovery import build
import sys
import json
import config


my_api_key = config.data_keys['api_key']
#my_cse_id = config.data_keys['cse_key']

#my_api_key = 'AIzaSyCw4PJQ81FLtSkl-dQdoaPBnCmHHW2pO2g'

#my_cse_id = 'e614e3f79d9c3a3fd'



def youtube_data(video_id):
    service = build("youtube", "v3", developerKey = my_api_key)
    result = service.videos().list(part='snippet',id=video_id).execute()
    return result


if __name__ == '__main__':
    result = youtube_data(sys.argv[1])
    with open(sys.argv[2], "w") as outfile:
        json.dump(result, outfile)
