import argparse

import librosa
import numpy as np
import scipy
import time

def find_offsets(within_file, find_file, window, start):
    #load the audio files
    y_within, sr_within = librosa.load(within_file, sr=None)
    y_find, _ = librosa.load(find_file, sr=sr_within)

    start_time = int(start * sr_within)

    c = scipy.signal.correlate(y_within[start_time:], y_find[:sr_within*window], mode='valid', method='fft')
    peaks, _ = scipy.signal.find_peaks(c, height=np.max(c) * 0.5, distance=sr_within)  # Adjust height using a fraction of the maximum correlation value

    offsets = [(round((peak + start_time) / sr_within, 2)) for peak in peaks if c[peak] > 90]  # Convert peak indices to time offsets

    return offsets


