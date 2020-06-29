"""
`PLAN`
-get the playlist_name
-go to that playlist thru API and youtube account credentials
-make a song_list from that playlist
-access spotify account thru API and spotify account credentials
-create new playlist in spotify
-add songs from song_list to new spotify playlist

req->items->snippet->title

"""


import os
import youtube_dl
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import re


def api_setup():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"
# Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    print("Done!")
    return youtube

def get_pl_id(youtube):

        #The following HTTP requestobject contains the list of the users playlists
        request = youtube.playlists().list(
            part="snippet,contentDetails",
            #channelId="UCqCyJk5sH5B9G9C0sJPyUsQ",
            mine="true",
            maxResults=50
            )
        response = request.execute()
        i=1
        for item in response['items']:
            print(i,'.',item['snippet']['title'])
            i+=1
        playlist_name=input("Which playlist would you like to transfer?\t")
        #get playlist id
        for item in response['items']:
            temp_id=item['id']
            if item['snippet']['title']==playlist_name:
                pl_id=temp_id
        return pl_id

def extract_info(youtube,pl_id):

    #get into that playlist
    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=pl_id,
        maxResults=50
    )
    response = request.execute()
    info={} # empty dict to store the song,artist info
    #get url and video title
    for item in response['items']:
        video_title = item["snippet"]["title"]
        video_url = "https://www.youtube.com/watch?v={}".format(item["snippet"]["resourceId"]["videoId"])
        details = youtube_dl.YoutubeDL({}).extract_info(video_url, download=False)
        track_name = details["track"]
        artist_name = details["artist"]
        if track_name is not None and artist_name is not None:
            #store detials in info dictioanry
            info[video_title]={
                "track_name":track_name,
                "artist_name":artist_name,
                "search_query":None
            } #remove the word explicit from track_name using re.sub or using string.split("(")[0]
            #info[video_title]['track_name']=re.sub("\(Explicit\)","",info[video_title]['track_name'])
            info[video_title]['track_name']=info[video_title]['track_name'].split("(")[0]
            #generate the search_query
            if "feat" not in info[video_title]['track_name']:
                search_query=info[video_title]['track_name']+" "+info[video_title]['artist_name']
            else:
                search_query=info[video_title]['track_name']
            info[video_title]['search_query']=search_query
        else:
            print("\n Could not add ",video_title,"  Please use an official video\n")
    #testing conents
    print("\n The following songs will be added!\n")
    for i in info:
        #print(info[i]["track_name"],":",info[i]["artist_name"])
        print("video title ",i,"query: ",info[i]['search_query'])

    return info
