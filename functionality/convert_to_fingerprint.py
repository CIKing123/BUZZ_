import json
import acrcloud

from dejavu import Dejavu

with open("../buzz.cnf") as f:
    config = json.load(f)

if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)
    # Fingerprint all the mp3's in the directory we give it
    djv.fingerprint_directory("../music_dir", [".mp3"])