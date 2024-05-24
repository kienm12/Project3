import scikit_build_example
 
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
 
def perform_dft(frames, sample_rate):
    # Convert frames to numpy array    signal = np.frombuffer(frames, dtype=np.int16)
    # Perform Fourier transform    
    N = len(frames)
    n = np.arange(N)  
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    dft_result = np.dot(e, frames)

    # Calculate the frequencies for the results
    freq = np.fft.rfftfreq(len(frames), 1/sample_rate)

    return freq, dft_result
  
arr, rate = read_wave('sample.wav')
freq, dft_result = perform_dft(arr, rate)
scikit_build_example.plot_dft(dft_result,"dft" ,"sample.wav", rate)
