import scikit_build_example
from scipy.signal import butter, lfilter, filtfilt
from scipy import signal
import wave
import struct
import numpy as np
fs = 44100

f = 100

t = 60

samples = np.arange(t * fs)


signal = np.sin(2 * np.pi * f * samples)


signal *= 32767

signal = np.int16(signal)




scikit_build_example.plot_wave(signal,"sinus" ,"sample.wav", f)
