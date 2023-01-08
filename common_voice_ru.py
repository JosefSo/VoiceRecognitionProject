from datasets import load_dataset, Audio
import soundfile

dataset = load_dataset("common_voice", name="ru", split="train[:1000]")
#dataset.save_to_disk("/Users/user/Desktop/VoiceData")

dataset = dataset.train_test_split(test_size=0.2)
dataset = dataset.remove_columns(['client_id', 'path', 'up_votes', 'down_votes', 'age', 'gender', 'accent', 'locale', 'segment'])
print(dataset)

from transformers import AutoProcessor
processor = AutoProcessor.from_pretrained("facebook/wav2vec2-base")

dataset = dataset.cast_column("audio", Audio(sampling_rate=16_000))
print(dataset["train"])
print(dataset["train"])

# print from dataset train audio
print(dataset["train"]["audio"][0])

def uppercase(example):
    return {"sentence": example["sentence"].upper()}
dataset = dataset.map(uppercase)

def prepare_dataset(batch):
    audio = batch["audio"]
    batch = processor(audio["array"], sampling_rate=audio["sampling_rate"], text=batch["transcription"])
    batch["input_length"] = len(batch["input_values"][0])
    return batch

encoded_dataset = dataset.map(prepare_dataset, remove_columns=dataset.column_names["train"], num_proc=4)







# example = dataset["train"][0]
# print(example["path"])
#
# def add_noise(example):
#   # Add noise to the example['waveform'] tensor and return the modified example
#   # ...
#   return example
#
# noisy_dataset = dataset.map(add_noise)
