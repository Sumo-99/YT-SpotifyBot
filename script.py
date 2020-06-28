#```IMPORTS```
import os
import youtube_dl
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import re
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials #w/o user
from spotipy.oauth2 import SpotifyOAuth # w user
import spotipy.util as util
import youtube_agent as y
from youtube_agent import api_setup,get_pl_id,extract_info
import spotify_agent as s
from spotify_agent import get_token,extract_youtube_info,create_playlist
import spotify_secrets
from spotify_secrets import user_id,client_secret,client_id
#```SET ENVIRONMENT VARRIABLES```
c1 = "SET SPOTIPY_CLIENT_ID=" + client_id
c2 = "SET SPOTIPY_CLIENT_SECRET="+ client_secret
c3 = "SET SPOTIPY_REDIRECT_URI='http://localhost:8888/'"
os.system(c1)
os.system(c2)
os.system(c3)

#```SCRIPT```
def main():

    #youtube_agent work
    print('hi')
    youtube=api_setup()
    pl_id=y.get_pl_id(youtube)
    info=y.extract_info(youtube,pl_id)

    #transfer the queries
    #sp,username=get_token(user_id) logically here , but done before to invoke extract_youtube_info
    # sp=get_token(user_id)
    # extract_youtube_info(sp,info) logically here for tranfer of quey list

    #spotify_agent work
    sp=s.get_token(user_id)
    track_uri_list=s.extract_youtube_info(info,sp)
    playlist_name="Youtube Imported Playlist"
    s.create_playlist(sp,user_id,playlist_name,track_uri_list)

    print()
    print("Youtube Imported Playlist created , check your spotify library!!")

if __name__ == "__main__":
    main()
