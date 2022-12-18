from datasets import load_dataset

dataset = load_dataset("common_voice", "ru")

dataset.save_to_disk("/Users/joseph/Desktop/myDataCommonVoice")