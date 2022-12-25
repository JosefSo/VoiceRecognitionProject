import torchaudio
import transformers

# Load the trained model
model = transformers.CTRLModel.from_pretrained('path/to/trained/model')

# Generate transcriptions for a list of audio files
transcriptions = []
for audio_file in audio_files:
    # Load audio data from file
    audio_data, _ = torchaudio.load(audio_file)
    audio_tensor = audio_data.squeeze(0)

    # Encode audio data as input for the model
    input_ids = model.encode(audio_tensor, return_tensors='pt')

    # Generate transcription using the model
    transcription = model.generate(input_ids)
    transcriptions.append(transcription)
