import warnings
import os
import webbrowser
from deepface import DeepFace
import cv2
import tensorflow as tf
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings("ignore", category=UserWarning, message=".*sparse_softmax_cross_entropy.*")

print(tf.__version__)
hello = tf.constant('Hello, TensorFlow!')
print(hello)

# Spotify API Scope
SPOTIFY_SCOPE = "user-modify-playback-state user-read-playback-state"

def get_playlist_for_emotion(emotion):
    playlists = {
        "happy": "https://open.spotify.com/track/0ibgjKZZ56aoelJ76o7OW9?si=b6d2b4425b264928",  # Happy Hits
        "sad": "https://open.spotify.com/track/5MrLQeEVCWueDR4XejhFNG?si=bf9ea79383ad41e2",  # Sad Songs
        "angry": "https://open.spotify.com/track/2gKNWPBrI2IRBl2RRUtoEb?si=4aac31e5d2574d67",  # Angry Beats
        "surprise": "https://open.spotify.com/track/1eknwgCfzOXC0VRTst91l7?si=17b35c04ad55421a",  # Surprise Me
        "neutral": "https://open.spotify.com/track/0CdgYYq6fYOcg8RPUZl716?si=20da88d9660047f7"  # Calm & Neutral
    }
    return playlists.get(emotion.lower(), None)


def open_link_in_browser(link):
    try:
        webbrowser.open(link)
        print(f"Opening link: {link}")
    except Exception as e:
        print(f"Error opening the link: {e}")

def detect_emotion_and_play_music():
    # Open webcam
    cap = cv2.VideoCapture(0)
    print("Press 'q' to capture the emotion and exit.")

    emotion = None
    while True:
        ret, frame = cap.read()
        cv2.imshow("Webcam - Emotion Detection", frame)

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            try:
                # Analyze emotion
                analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                if isinstance(analysis, list):
                    analysis = analysis[0]

                emotion = analysis.get('dominant_emotion', None)
                if emotion:
                    print(f"Detected Emotion: {emotion}")

                    # Get playlist URL for the detected emotion
                    playlist_url = get_playlist_for_emotion(emotion)
                    if playlist_url:
                        print(f"Please open this link to listen to a playlist for {emotion}: {playlist_url}")
                        open_link_in_browser(playlist_url)
                    else:
                        print("No playlist available for this emotion.")
                else:
                    print("Unable to detect a dominant emotion.")
            except Exception as e:
                print("Error detecting emotion:", e)
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("Opening webcam for emotion detection...")
    detect_emotion_and_play_music()
