#TITLE

COSC 381 Git Hub Repository Homework
by
Alexander Schumacher

##Instalation
With you, the user, having this document I can assume you either cloned or copied all the files in the github repository.
From this point on I will be instructing you in the process of installing all necessary packages and creating a searchable whoosh
database.

1.) In your linux command line environment within the working directory run "python3 -m pip install -r requirements.txt".
    You may have to run it with sudo should you not have the appropriate power within your environment "sudo python3 -m pip install -r requirements.txt"	

2.) You now have the necessary packages intalled to begin.  Use an editor of your chosing and open 'config.py'  Here you will do 
    three things; type in your API key, CSE id, and the search term you desire to get data from youtude.  Follow the comments in 
    config.py if you need some careful guidance.

3.) Now you will be running cse.py.  Type into your command line "python3 cse.py > download_data.txt".  This will create 
    "download_data.txt"

4.) Now you will run this command in your terminal "grep "videoid" download_data.txt | awk -F ":" '{print $2}' | awk -F "'" '{print $2}' > video_id.txt"  
    This will create a document called "video_id.txt" which contains all the video id information for every single video in the search results.

5.) If you have a directory in you working directory called "youtube_data" you must remove it or change its name.  Type this command into your command line "bash download_youtube_data_batch.sh".  Please be patient till the program finishes.  This may take some time.

6.)Run in your command line "python3 create_data_for_indexing.py"  This will createa a json file.

7.)Run in your command line "python3 data_base_creation.py" 

##Operating Sytstem

To run a querey with the newly created whoosh data base type into your command line "python3 querey.py" and follow the prompts made by the program.

##Reseting for new searches

To search for a new data selection run Instalation step 2 through 7.


