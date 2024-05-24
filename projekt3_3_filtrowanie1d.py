import scikit_build_example
from scipy.signal import butter, lfilter, filtfilt
from scipy import signal
import wave
import struct
import numpy as np
def read_wave(filename: str):  
  with wave.open(filename) as f:        
      rate = f.getframerate()
      frames = f.getnframes()
      duration = frames / float(rate)
      sampwidth = f.getsampwidth()
      print(f"duration:{duration} rate:{rate} frames:{frames} sampwidth:{sampwidth} chanels:{f.getnchannels()}")
     
      #czytamy 30 sek
      frames_to_read = round(rate * 0.3)
      if f.getnframes()*f.getnchannels() < frames_to_read:
            print(f"Plik {filename} jest krótszy niż 60 sek.")
            frames_to_read = f.getnframes()
   
      data = f.readframes(frames_to_read)        
      samples = list(struct.unpack('{n}h'.format(n=frames_to_read*f.getnchannels()), data) )  
      aa = samples[0::f.getnchannels()]#czytamy tylko kanał 0
      arr = np.array(aa)
  return arr, rate
 
def filter_1d(arr, cutoff_frequency, sample_rate):
    # Design the filter   
    nyquist_rate = sample_rate / 2.0  
    cutoff_frequency = cutoff_frequency / nyquist_rate   
    b, a = signal.butter(5, cutoff_frequency)

    # Apply the filter
    filtered_signal = signal.lfilter(b, a, arr)
    return filtered_signal

arr, rate = read_wave('sample.wav')
dft_result = filter_1d(arr,1000, rate)

scikit_build_example.plot_wave(dft_result,"filtr 1d" ,"sample.wav", rate)
