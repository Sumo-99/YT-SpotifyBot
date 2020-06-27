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
import youtube_agent
from youtube_agent import api_setup,get_pl_id,extract_info
import spotify_agent
from spotify_agent import get_token,extract_youtube_info,create_playlist
#from credentials import user_id
#```SET ENVIRONMENT VARRIABLES```
c1 = "SET SPOTIPY_CLIENT_ID='d6abe18b73e24c508a7b6eed91f42112'"
c2 = "SET SPOTIPY_CLIENT_SECRET='dde2d8819bda49b48e8ed17e9e08fe89'"
c3 = "SET SPOTIPY_REDIRECT_URI='http://localhost:8888/'"
os.system(c1)
os.system(c2)
os.system(c3)

#```SCRIPT```
def main():

    #youtube_agent work
    youtube=api_setup()
    """
    pl_id=get_pl_id(youtube)
    info=extract_info(youtube,pl_id)

    #transfer the queries
    #sp,username=get_token(user_id) logically here , but done before to invoke extract_youtube_info
    # sp,username=get_token(user_id)
    # extract_youtube_info(sp,info) logically here for tranfer of quey list

    #spotify_agent work
    user_id="ku6oj81vy1ix4lmr7njd7wz2b"
    sp,username=get_token(user_id)
    track_uri_list=extract_youtube_info(info,sp)
    playlist_name="Youtube Imported Playlist"
    create_playlist(sp,username,playlist_name,track_uri_list)

    print()
    print("Play list created check your spotify library!!")
"""
