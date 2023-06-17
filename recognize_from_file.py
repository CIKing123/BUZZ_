import json

from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)

    # results = djv.recognize(FileRecognizer, "test/audio.m4a")
    results = djv.recognize(FileRecognizer, "media/audio.mp3")
    print(f"From file we recognized: {results}\n")
    # best_result = max(results[0], key=lambda x: x['input_confidence'])
    # print(best_result['song_name'])

    # # Or use a recognizer without the shortcut, in anyway you would like
    # recognizer = FileRecognizer(djv)
    # results = recognizer.recognize_file("mp3/Pain.mp3")
    # print(f"No shortcut, we recognized: {results}\n")