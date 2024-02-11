import argparse

import librosa
import numpy as np
import scipy
import time


# detects the start indexes of match start sound in input_file, returns the start indexes in seconds, outputting an array of start indexes
# pass in start time to appropriately calculate the offset with an audio file that doesn't start when the stream
# for example, if you clip the audio file starting at 300 seconds, pass in 300 seconds to start to apporpirately calulate the offsets
def find_offsets(within_file, find_file, window, start):
    #load the audio files
    y_within, sr_within = librosa.load(within_file, sr=None)
    y_find, _ = librosa.load(find_file, sr=sr_within)

    

    c = scipy.signal.correlate(y_within, y_find[:sr_within*window], mode='valid', method='fft')
    peaks, _ = scipy.signal.find_peaks(c, height=np.max(c) * 0.5, distance=sr_within)  # Adjust height using a fraction of the maximum correlation value

    offsets = [(round(peak / sr_within, 2)) + start for peak in peaks if c[peak] > 90]  # Convert peak indices to time offsets

    return offsets


