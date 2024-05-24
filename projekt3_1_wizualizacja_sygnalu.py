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
     
      #czytamy 60 sek
      frames_to_read = round(rate * 0.6)
      if f.getnframes()*f.getnchannels() < frames_to_read:
            print(f"Plik {filename} jest krótszy niż 60 sek.")
            frames_to_read = f.getnframes()
   
      data = f.readframes(frames_to_read)        
      samples = list(struct.unpack('{n}h'.format(n=frames_to_read*f.getnchannels()), data) )  
      aa = samples[0::f.getnchannels()]#czytamy tylko kanał 0
      arr = np.array(aa)
  return arr, rate
 
arr, rate = read_wave('sample.wav')
 
scikit_build_example.plot_wave(arr,"Wizualizacja sample.wav kanal 0" ,"sample.wav", rate)