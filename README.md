# YT-SpotifyBot
A simple Python script to transfer songs from a YouTube playlist of your choice into a new Spotify playlist

## SETUP
You will need
  *Youtube Data API credentials
  *Spotify Web API credentials

## YOUTUBE API SETUP
  *Follow [this link] step by step to create the API requisites
  *next download the 'client_secrets.json' file. It may downlaod with a different name,please rename it as above^

## SPOTIFY WEB API SETUP
  *Get your spotify user id in the [Account Overview] section
  *Visit [spotify developer console] and do the following:
    ** First login with your spotify account credentials
    ** Next click on 'create an app' name it as you wish , accept the terms and hit create
    ** Now you will be able to view client ID and client secret (click show client secret)
  *copy the client id , client secret and your user id into the 'spotify_secrets.py' file


# INSTALL
To install dependencies run
  'pip install -r requirements.txt'




[this link]: <https://developers.google.com/youtube/v3/getting-started/>
[Account Overview]: <https://www.spotify.com/us/account/overview/>
[spotify developer console]: <https://developer.spotify.com/dashboard/login>
