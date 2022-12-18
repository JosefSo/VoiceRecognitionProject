from __future__ import unicode_literals
import random
from youtubesearchpython import VideosSearch
import youtube_dl
import ffmpeg


def random_word_pick():
    word_list = []
    w_list = []
    with open("words_alpha.txt", "r") as file:
        for word in file:
            if len(word) >= 5:
                word = word[:-1]
                word_list.append(word)
    w_list = random.sample(word_list, 50)
    return w_list


def get_vid_links():
    vid_links = []
    all_words = []
    with open("words_alpha.txt", "r") as file:
        for word in file:
            all_words.append(word)
    random.shuffle(all_words)
    for word in all_words:
        if len(word) >= 5:
            word = word[:-1]
            search_results = VideosSearch(word, limit=100).result()["result"]
            for i in range(len(search_results)):
                print("searach result " + search_results[i]["duration"])
                if int(search_results[i]["duration"].split(":")[0]) < 1:
                    vid_links.append(search_results[i]["link"])
                    break
        if len(vid_links) == 50:
            return vid_links


def download_audio(vid_links: list):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio_youtube/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for vid in vid_links:
            ydl.download([vid])


if __name__ == '__main__':
    words = random_word_pick()
    print(words)
    vids = get_vid_links()
    print("got vid links")
    download_audio(vids)
    pass
