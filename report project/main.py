from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
# import librosa

wav_loc = "test.wav"
rate, data = wavfile.read(wav_loc)
data = data / 32768

