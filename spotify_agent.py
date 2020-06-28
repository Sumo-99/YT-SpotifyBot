#imports
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials #w/o user
from spotipy.oauth2 import SpotifyOAuth # w user
import spotipy.util as util
import re


#username = ku6oj81vy1ix4lmr7njd7wz2b
def api_setup_without():
    #WITHOUT USER credentials
    #1. Set the client id and client_secret
        client_id = 'd6abe18b73e24c508a7b6eed91f42112'
        client_secret = '2fd662c1491b4beea8fca1ced491995d'
        ccm = SpotifyClientCredentials(client_id, client_secret)
    #2. Create a spotipy object using the above credentials
        sp = spotipy.Spotify(client_credentials_manager=ccm)
    #3. Return the object to be used for calls
        return sp

def api_setup_with(scope,username):

    token = util.prompt_for_user_token(username,
                                       scope,
                                       client_id='d6abe18b73e24c508a7b6eed91f42112',
                                       client_secret='dde2d8819bda49b48e8ed17e9e08fe89',
                                       redirect_uri='http://localhost:8888/')

    #creating the object
    sp=spotipy.Spotify(auth=token)
    return sp

class song(object):
    def __init__(self,track_name,artist_name):
        self.track_name=track_name
        self.artist_name=artist_name
    def show(self):
        print(self.track_name," by ",self.artist_name)

def song_extraction(sp):
    #temporary song song_list
    song_list=[song('old town road','Lil Nas X'),song('icon','Jaden'),song('Gang Gang','Migos')]
    #searching for a song
    track_uri_list=[]
    for i in song_list:
        q=i.track_name
        result=sp.search(q,1,0,'track')
        track_uri_list.append(result['tracks']['items'][0]['uri'])
        #result['tracks']['items'][0]['artist']['name']
    #print(track_uri_list)
    return track_uri_list

def extract_youtube_info(info,sp):
    query_list=[]
    for query in info:
        query_list.append(info[query]["search_query"])
    #searching for a song
    track_uri_list=[]
    for i in query_list:
        result=sp.search(i,1,0,'track')
        track_uri_list.append(result['tracks']['items'][0]['uri'])
        #result['tracks']['items'][0]['artist']['name']
    #print(track_uri_list)
    return track_uri_list



def create_playlist(sp,username,playlist_name,track_uri_list):
    # create a new playlist
    pl_obj=sp.user_playlist_create(username,playlist_name,public=False,description="Songs from YouTube!")
    #get details of a playlist --> get playlist object['id'] or #pl=sp.user_playlist(username)
    playlist_id=pl_obj['id']
    #add tracks to a playlist
    sp.user_playlist_add_tracks(username,playlist_id,track_uri_list)

def get_token(user_id):
    #username=sys.argv[1]
    scope = 'playlist-modify-private playlist-modify-public'
    sp=api_setup_with(scope,user_id)
    #setting up the api service object hence a user warning
    print("Spotify authentication processing...")
    return sp

def main():
        user_id="ku6oj81vy1ix4lmr7njd7wz2b"
        sp=get_token(user_id)
        track_uri_list=song_extraction(sp)
        playlist_name="test 5"
        create_playlist(sp,username,playlist_name,track_uri_list)






if __name__=="__main__":
    main()
