import numpy as np
import soundfile as sf

# Load the voice recording and the noise files
voice, fs = sf.read('voice_recording.wav')
traffic_noise, _ = sf.read('traffic_noise.wav')
aircraft_noise, _ = sf.read('aircraft_noise.wav')
construction_noise, _ = sf.read('construction_noise.wav')
animal_noise, _ = sf.read('animal_noise.wav')
thunderstorm_noise, _ = sf.read('thunderstorm_noise.wav')
rain_noise, _ = sf.read('rain_noise.wav')
wind_noise, _ = sf.read('wind_noise.wav')
birds_singing, _ = sf.read('birds_singing.wav')
crickets_chirping, _ = sf.read('crickets_chirping.wav')
leaves_rustling, _ = sf.read('leaves_rustling.wav')
office_noise, _ = sf.read('office_noise.wav')
sports_activity_noise, _ = sf.read('sports_activity_noise.wav')

# Normalize the noise files to the same volume level as the voice recording
traffic_noise = traffic_noise / np.max(np.abs(traffic_noise)) * np.max(np.abs(voice))
aircraft_noise = aircraft_noise / np.max(np.abs(aircraft_noise)) * np.max(np.abs(voice))
construction_noise = construction_noise / np.max(np.abs(construction_noise)) * np.max(np.abs(voice))
animal_noise = animal_noise / np.max(np.abs(animal_noise)) * np.max(np.abs(voice))
thunderstorm_noise = thunderstorm_noise / np.max(np.abs(thunderstorm_noise)) * np.max(np.abs(voice))
rain_noise = rain_noise / np.max(np.abs(rain_noise)) * np.max(np.abs(voice))
wind_noise = wind_noise / np.max(np.abs(wind_noise)) * np.max(np.abs(voice))
