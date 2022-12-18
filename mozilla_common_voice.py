from datasets import load_dataset

dataset = load_dataset("joefox/Mozilla_Common_Voice_ru_test_noise")

dataset.save_to_disk("/Users/joseph/Desktop/myDataCommonVoice")