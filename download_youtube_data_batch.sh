#!/bin/bash
  

if [ ! -d youtub_data ]; then
   mkdir youtube_data
fi


while read p; do
        touch youtube_data/$p.json
        python3 download_youtube_data.py $p  youtube_data/$p.json
done < video_id.txt






