from datasets import load_dataset
import soundfile

dataset = load_dataset("common_voice", "ru")

dataset.save_to_disk("/Users/user/Desktop/VoiceData")