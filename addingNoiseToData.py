"""
Noise source:	    Percentage adding to Data:
Traffic noise	    30-50%
Aircraft noise	    10-20%
Construction noise	10-20%
Animal noise	    10-20%
Thunderstorms	    5-10%
Rainfall	        5-10%
Wind	            5-10%
Birds singing	    5-10%
Crickets chirping	5-10%
Leaves rustling	    5-10%
Office noise	    30-50%
Sports noise        10-20%

TO_DO:  1. Calculate size of Data
        2. Divide noise data on needed percentage (%) according to Voice Data size
        3. (Calculate) Decide in what segment of Voice Data put the Noise Data
        4. Append Noise Data to Voice Data
"""



import numpy as np
import soundfile as sf
from scipy.signal import resample


def add_noise(voice_data, noise_data, noise_level):
    # Convert the voice data and noise data to numpy arrays
    voice_data = np.array(voice_data, dtype=np.float32)
    noise_data = np.array(noise_data, dtype=np.float32)

    # Normalize the noise data
    noise_data = noise_data / np.max(np.abs(noise_data))

    # Resample the noise data to match the sample rate of the voice data
    print(f"int(voice_data.shape[0]) {(voice_data.shape[0])}")
    print(f"noise_data.shape[0]) {noise_data.shape[0]}")
    print(f"int(voice_data.shape[0] / noise_data.shape[0]) {int(voice_data.shape[0] / noise_data.shape[0])}")
    noise_data = resample(noise_data, 1)

    # Trim the noise data to match the length of the voice data
    noise_data = noise_data[:voice_data.shape[0]]

    # Mix the noise and voice data, with the specified noise level
    mixed_data = voice_data + noise_level * noise_data

    return mixed_data


# Load the voice data and noise data
voice_data, _ = sf.read('voice_data/voice.wav')
noise_data, _ = sf.read('noise_data/noise.wav')

# Add noise to the voice data at various levels
mixed_data_1 = add_noise(voice_data, noise_data, 0.1)
mixed_data_2 = add_noise(voice_data, noise_data, 0.5)
mixed_data_3 = add_noise(voice_data, noise_data, 0.9)

# Save the mixed data to new audio files
sf.write('mixed_data/mixed_data_1.wav', mixed_data_1, 44100)
sf.write('mixed_data/mixed_data_2.wav', mixed_data_2, 44100)
sf.write('mixed_data/mixed_data_3.wav', mixed_data_3, 44100)
