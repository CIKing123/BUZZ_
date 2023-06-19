import json
import acoustid
from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from acrcloud.recognizer import ACRCloudRecognizer

SPOTIFY_URL = "https://open.spotify.com/"
audio_file = "../media/audio.mp3"

# load config from a JSON file (or anything outputting a python dictionary)
with open("../buzz.cnf") as f:
    config = json.load(f)


def send_to_acr_cloud(audio):
    config = {
        "host": "identify-us-west-2.acrcloud.com",
        "access_key": "32e8b4a17a8e54e6dae651348bca2759",
        "access_secret": "roU98fiFDzlWEWntK4LR9ccmM3QAAf6ywoqu9J6D",
        "timeout": 10
    }
    re = ACRCloudRecognizer(config)
    results = re.recognize_by_file(audio, 0)
    return results


def display_results(data):
    response = json.loads(data)
    print(response)

    if "status" in response and response["status"].get("msg") == "Success":
        print("Music found successfully:\n")

        metadata = response.get("metadata", {})
        if "music" in metadata:
            music = metadata["music"][0]

            if "external_metadata" in music and "spotify" in music["external_metadata"]:
                spotify = music["external_metadata"]["spotify"]

                if "genres" in music and music["genres"]:
                    genre = music["genres"][0]["name"]
                else:
                    genre = "Unknown"
                label = music.get("label")
                release_date = music.get("release_date", "")[:4]

                # Print Spotify details
                spotify_track = spotify["track"]
                spotify_album = spotify["album"]
                spotify_artists = spotify["artists"]

                print(f"Track ID: {SPOTIFY_URL + 'track/' + spotify_track['id']}")
                print(f"Track Name: {spotify_track['name']}")
                print(f"Album Name: {spotify_album['name']}")
                print(f"Album ID: {SPOTIFY_URL + 'album/' + spotify_album['id']}")

                if len(spotify_artists) == 1:
                    print("Artist:")
                else:
                    print("Artists:")
                for artist in spotify_artists:
                    print(f" - ID: {SPOTIFY_URL + 'artist/' + artist['id']}, Name: {artist['name']}")

                print(f"Genre: {genre}")
                print(f"Record Label: {label}")
                print(f"Released: {release_date}")
            else:

                album_name = music["album"]["name"]
                artists = music["artists"]
                song_name = music["title"]
                if "genres" in music and music["genres"]:
                    genre = music["genres"][0]["name"]
                else:
                    genre = "Unknown"
                label = music.get("label")
                release_date = music.get("release_date", "")[:4]

                # Print default details
                print(f"Song Name: {song_name}")
                print(f"Album: {album_name}")
                if artists:
                    if len(artists) == 1:
                        print(f"Artist: {artists[0]['name']}")
                    else:
                        print("Artists:")
                        for artist in artists:
                            print(f" - {artist['name']}")
                else:
                    print("Artist: Unknown")
                print(f"Genre: {genre}")
                print(f"Record Label: {label}")
                print(f"Released: {release_date}")
                print("\nFinished!")
        else:
            print("No music information found.")
    else:
        print("Song not found.")

if __name__ == '__main__':
    # create a Dejavu instance
    djv = Dejavu(config)

    results = djv.recognize(FileRecognizer, audio_file)
    if results:
        print(f"From file we recognized: {results}\n")
        display_results(send_to_acr_cloud(audio_file))
    # best_result = max(results[0], key=lambda x: x['input_confidence'])
    # print(best_result['song_name'])

    # # Or use a recognizer without the shortcut, in anyway you would like
    # recognizer = FileRecognizer(djv)
    # results = recognizer.recognize_file("mp3/Pain.mp3")
    # print(f"No shortcut, we recognized: {results}\n")
