from datasets import load_dataset
import soundfile

dataset = load_dataset("common_voice", name="ru", split="train[:100]")

#dataset.save_to_disk("/Users/user/Desktop/VoiceData")

dataset = dataset.train_test_split(test_size=0.2)

dataset = dataset.remove_columns(['client_id', 'path', 'up_votes', 'down_votes', 'age', 'gender', 'accent', 'locale', 'segment'])

print(dataset)


# example = dataset["train"][0]
# print(example["path"])
#
# def add_noise(example):
#   # Add noise to the example['waveform'] tensor and return the modified example
#   # ...
#   return example
#
# noisy_dataset = dataset.map(add_noise)
