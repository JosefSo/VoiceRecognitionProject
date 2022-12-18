import os
import wave
import numpy as np

import os, random




path_of_the_directory_noise = 'audio_youtube'
path_of_the_directory_data = 'data'

ext = ('.wav')
idx = 0;
for dataFiles in os.listdir(path_of_the_directory_data):
    if dataFiles.endswith(ext):
        randomFile = random.choice(os.listdir('audio_youtube'))  # change dir name to whatever
        print("dataFiles: " + dataFiles)
        print("randomFile: " + randomFile)


        # load two files you'd like to mix
        fnames =[f"data/{dataFiles}", f"audio_youtube/{randomFile}"]
        wavs = [wave.open(fn) for fn in fnames]
        frames = [w.readframes(w.getnframes()) for w in wavs]

        # here's efficient numpy conversion of the raw byte buffers
        # '<i2' is a little-endian two-byte integer.
        samples = [np.frombuffer(f, dtype='<i2') for f in frames]
        samples = [samp.astype(np.float64) for samp in samples]

        # mix as much as possible
        n = min(map(len, samples))
        mix = samples[0][:n] + samples[1][:n]

        # Save the result

        mix_wav = wave.open(f"./mixData/mix{idx}.wav", 'w')
        idx = idx+1
        mix_wav.setparams(wavs[0].getparams())

        # before saving, we want to convert back to '<i2' bytes:
        mix_wav.writeframes(mix.astype('<i2').tobytes())
        mix_wav.close()

