# YouTube-SpotifyBot
A simple Python script to transfer songs from a YouTube playlist of your choice into a new Spotify playlist

## SETUP
You will need
  *Youtube Data API credentials
  *Spotify Web API credentials

## YOUTUBE API SETUP
<ul>
<li>Follow <a href="https://developers.google.com/youtube/v3/getting-started/">this link</a> step by step to create the API requisites</li>
<li>next download the 'client_secrets.json' file.
It may downlaod with a different name,please rename it as above^</li>
</ul>

## SPOTIFY WEB API SETUP
<ul>
<li>Get your spotify user id in the <a href="https://www.spotify.com/us/account/overview/">Account Overview</a> section</li>
<li>Visit <a href="https://developer.spotify.com/dashboard/login">spotify developer console </a> and do the following:</li>
  <ul>
  <li> First login with your spotify account credentials</li>
  <li> Next click on 'create an app' name it as you wish , accept the terms and hit create</li>
  <li> Now you will be able to view client ID and client secret (click show client secret)</li>
  </ul>
<li>copy the client id , client secret and your user id into the 'spotify_secrets.py' file</li>
</ul>

## INSTALL
To install dependencies run
<code>pip install -r requirements.txt</code>




[this link]: <https://developers.google.com/youtube/v3/getting-started/>
[Account Overview]: <https://www.spotify.com/us/account/overview/>
[spotify developer console]: <https://developer.spotify.com/dashboard/login>
