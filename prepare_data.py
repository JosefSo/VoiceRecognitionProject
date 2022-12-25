import torchaudio
import transformers

# Load the audio data and convert it to a tensor
audio_data, _ = torchaudio.load('audio_youtube/How Does The Derma Co. 2% Salicylic Acid Serum Help.wav')  # put here the data with noise
audio_tensor = audio_data.squeeze(0)

# Load the transcription and convert it to a sequence of tokens
tokenizer = transformers.CTRLTokenizer.from_pretrained('ctrl')
transcription = 'This is a transcription of the audio file'  # put here the transcription of the audio file
input_ids = tokenizer.encode(transcription, return_tensors='pt')
