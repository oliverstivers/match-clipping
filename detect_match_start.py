import argparse

import librosa
import numpy as np
import scipy
import time
import matplotlib.pyplot as plt


# detects the start indexes of match start sound in input_file, returns the start indexes in seconds, outputting an array of start indexes
# pass in start time to appropriately calculate the offset with an audio file that doesn't start when the stream
# for example, if you clip the audio file starting at 300 seconds, pass in 300 seconds to start to apporpirately calulate the offsets
import librosa
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

def find_offsets(within_file, find_file, window, start):
    # load the audio files
    start_offset = 0
    offsets = []
    for i in range(5):
        print("loading big. offset: " + str(start_offset) + " seconds.")
        y_within, sr_within = librosa.load(within_file, sr=14000, offset=start_offset, duration=7200)
        print("loading small")
        y_find, _ = librosa.load(find_file, sr=sr_within)

        print("processing")
        c = scipy.signal.correlate(y_within, y_find[:sr_within*window], mode='valid', method='fft')
        peaks, _ = scipy.signal.find_peaks(c, height=np.max(c) * 0.1, distance=sr_within)  # Adjust height using a fraction of the maximum correlation value

        offsets += [(round(peak / sr_within, 2)) + start_offset for peak in peaks if c[peak] > 50]  # Convert peak indices to time offsets

        

        start_offset += 7200


    # Plot the concatenated correlation array
    return offsets




