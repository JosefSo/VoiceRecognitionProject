from pydub import AudioSegment

# fileVoice = "3.wav"
# fileNoise = "4.wav"

def merge(fileVoice, fileNoise):

    # Load the audio files
    audio1 = AudioSegment.from_wav(fileVoice)
    audio2 = AudioSegment.from_wav(fileNoise)

    # Set the sample rate of both audio files to 44100 Hz
    audio1 = audio1.set_frame_rate(44100)
    audio2 = audio2.set_frame_rate(44100)

    # Mix the audio files
    mixed_audio = audio1.overlay(audio2)

    # You can also specify the starting position for the overlay using the position parameter.
    # For example, to start the overlay at 2 seconds into audio1, you can do:
    # mixed_audio = audio1.overlay(audio2, position=2000)

    return mixed_audio

    # Save the mixed audio to a file
    # mixed_audio.export("mixed_audio.wav", format="wav")

# merge(fileVoice, fileNoise)


