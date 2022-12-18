from datasets import load_dataset


myData = load_dataset("common_voice", "ru")
myData.save_to_disk("/Users/joseph/Desktop/myDataCommonVoice")

