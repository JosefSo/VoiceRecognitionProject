# I have probabilities of each noise and I want to put in on data in correct proportions
import os
import random
from merge2audio import merge

# map of different noises
mapOfNoises = {
    "talks": 0.7,
    "traffic_noise": 0.5,
    "aircraft_noise": 0.3,
    "construction_noise": 0.4,
    "animal_noise": 0.05,
    "thunderstorm_noise": 0.05,
    "rain_noise": 0.05,
    "wind_noise": 0.1,
    "birds_singing": 0.05,
    "leaves_rustling": 0.05,
    "office_noise": 0.3,
    "sports_activity_noise": 0.1
}

voiceDataDirectory = 'voiceData'


# count how much files in directory
def countFilesInDirectory(directory):
    sizeOfSamples = 0
    for file in os.listdir(directory):
        if file.endswith(".wav"):
            sizeOfSamples = sizeOfSamples + 1
    return sizeOfSamples

# calculate number of files I need to put noise according to probability
def calculateNumberOfFilesToPutNoise(probability, sizeOfSamples):
    return int(probability * sizeOfSamples)

# put noise on data in correct proportions
def putNoiseOnData(probability, directoryWithNoise, directoryWithData):
    sizeOfSamples = countFilesInDirectory(directoryWithData)
    numberOfFilesToPutNoise = calculateNumberOfFilesToPutNoise(probability, sizeOfSamples)
    print(numberOfFilesToPutNoise)
    num = sizeOfSamples - numberOfFilesToPutNoise
    # generate random number between 0 and num and put it into randomNumber
    randomNumber = random.randint(0, num)
    # from randomNumber to numberOfFilesToPutNoise - randomNumber put noise on data
    for i in range(randomNumber, numberOfFilesToPutNoise - randomNumber):
        print("put noise on data")
        # take file from directoryWithData on i position and put it into fileVoice
        fileVoice = os.listdir(directoryWithData)[i]
        # take file from directoryWithNoise that ends on .wav and put it into fileNoise
        fileNoise = [file for file in os.listdir(directoryWithNoise) if file.endswith(".wav")][0]
        # cut fileNoise to the same length as fileVoice and put it into fileNoise
        cuttedFileNoise = fileNoise[:len(fileVoice)]
        # use merge from merge2audio.py to merge fileNoise on fileVoice audios and put it into updatedFileVoice
        updatedFileVoice = merge(fileVoice, cuttedFileNoise)
        # save updatedFileVoice in noiseData directory
        updatedFileVoice.export(f"noiseData/{fileVoice}", format="wav")




# put noise on samples in voiceDataDirectory according map where key is name of noise and value is probability
def putNoiseOnSamples():
    for key, value in mapOfNoises.items():
        putNoiseOnData(value, key, voiceDataDirectory)

# I want to take random video of specific noise from youtube and put it on data
if __name__ == '__main__':
    putNoiseOnSamples()




