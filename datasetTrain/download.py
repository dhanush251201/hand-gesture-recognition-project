from pytube import YouTube
import json
from moviepy.editor import VideoFileClip

import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
FINAL_PATH = "/Users/dhanush/Documents/D/college/sem7/project/datasetTrain"
TRAIN_PATH="/Users/dhanush/Documents/D/college/sem7/project/MSASL_train.json"
TMP_PATH = "/Users/dhanush/Documents/D/college/sem7/project/tmp"
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=TMP_PATH)
    except:
        print("An error has occurred")
    print(f"Downloaded {link}")


# Download("https://www.youtube.com/watch?v=I_QDeKcyvns")

def F():
    with open(TRAIN_PATH, "r") as json_file:
        json_string = json_file.read()
    data = json.loads(json_string)
    c = 0
    count = 0
    for i in data:
        count+=1
        if c==1:
            exit()
        # print(dict(i)['url'])
        Download(dict(i)['url'])

        input_video_path = TMP_PATH+'/'+os.listdir(TMP_PATH)[0]
        print(input_video_path)
        output_video_path = f"/Users/dhanush/Documents/D/college/sem7/project/datasetTrain/{dict(i)['clean_text']}/{count}.mp4"
        start_time = dict(i)['start_time']
        end_time = dict(i)['end_time']
        clip = VideoFileClip(input_video_path).subclip(start_time, end_time)
        clip.write_videofile(output_video_path, codec="mpeg4")
        os.remove(input_video_path)

        c+=1

F()

