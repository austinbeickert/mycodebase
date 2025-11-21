import spotipy
from spotipy.oauth2 import SpotifyOAuth

debug = 1

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="fc51f5d456fc44cfb4da9fd831b0d309",
    client_secret="a6d7ab2fb06946d69f463193cdf9d3fb",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-modify-playback-state user-read-playback-state"
))

def play_playlist(playlist_uri):
    if debug:
        print(f"Playback requested: {playlist_uri}")

    devices = sp.devices()
    if not devices["devices"]:
        print("No devices found.")
        return

    device_id = devices["devices"][0]["id"]

    sp.start_playback(device_id=device_id, context_uri=playlist_uri)
    if debug:
        print(f"Now playing: {playlist_uri}")

def pause_playlist():
    try:
        devices = sp.devices()
        if devices["devices"]:
            sp.pause_playback(device_id=devices["devices"][0]["id"])
    except Exception as e:
        print(f"Error while pausing: {e}")

if debug:
    link = 'https://open.spotify.com/album/0ZbnBDVUkpegVOfgPFr1wr?si=flKonIl0TLSqbYIpTi5cVA'
    play_playlist(link)