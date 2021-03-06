#imports
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials #w/o user
from spotipy.oauth2 import SpotifyOAuth # w user
import spotipy.util as util
import re
import spotify_secrets
from spotify_secrets import client_id,client_secret



def api_setup_with(scope,username):

    token = util.prompt_for_user_token(username,
                                       scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
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
