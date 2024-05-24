import spotipy
from spotify.spotify_auth import get_spotify_client

def pause_spotify():
    sp = get_spotify_client()
    sp.pause_playback()

def play_spotify():
    sp = get_spotify_client()
    sp.start_playback()
