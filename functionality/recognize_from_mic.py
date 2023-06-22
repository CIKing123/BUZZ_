import json

from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("../buzz.cnf") as f:
    config = json.load(f)

if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)
    secs = 10
    results = djv.recognize(MicrophoneRecognizer, seconds=secs)
    if results is None:
        print("Nothing recognized -- did you play the song out loud so your mic could hear it? :)")
    else:
        print(f"From mic with {secs} seconds we recognized: {results}\n")
        # best_result = max(results[0], key=lambda x: x['input_confidence'])
        # print(str(best_result['song_name']).split("'")[1])
