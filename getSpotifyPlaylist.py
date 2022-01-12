#! python3

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
client_id = "f4d2453ddee7421687dc03a085854be8"
client_secret = "954be9186f6f49478082542d4f0bea0a"
redirect_uri = "http://localhost:8080"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))


def get_playlist_tracks(playlist_id):
    result = sp.playlist_items(playlist_id)
    tracks = result['items']
    while result['next']:
        result = sp.next(result)
        tracks.extend(result['items'])

    return tracks


def get_name_and_artist(tracks):
    musics = []
    for track in tracks:
        track_info = track['track']
        track_name = track_info['name']
        track_artist = track_info['artists'][0]['name']
        musics.append(track_name + " - " + track_artist)

    return musics


if __name__ == "__main__":
    songs = get_playlist_tracks("61AB5QRJWEg9Ld9wVqTgQl")
    for i in get_name_and_artist(songs):
        print(i)
