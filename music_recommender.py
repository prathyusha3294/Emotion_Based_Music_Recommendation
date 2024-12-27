import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def get_music_recommendations(emotion):
    # Map emotions to genres
    emotion_genre_mapping = {
        "happy": "pop",
        "sad": "classical",
        "angry": "rock",
        "neutral": "chill",
        "fear": "ambient",
        "surprise": "electronic",
        "disgust": "jazz"
    }
    
    genre = emotion_genre_mapping.get(emotion.lower(), "pop")  # Default to pop
    print(f"Fetching {genre} music for the '{emotion}' emotion...")
    
    # Set up Spotify client
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    ))
    
    # Search for tracks in the given genre
    results = sp.search(q=f'genre:{genre}', type='track', limit=5)
    return results['tracks']['items']
