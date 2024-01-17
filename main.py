import schedule
import time
import random
import os
from TikTokApi import TikTokApi

api = TikTokApi()

def upload_random_video():
    # Change this to your specific Folder with Random Videos.
    video_folder = 'path/to/your/video/folder'
    video_files = os.listdir(video_folder)
    random_video = random.choice(video_files)
    video_path = os.path.join(video_folder, random_video)
    # change 'Your video caption' to your desired caption (will be put on every single video)
    caption = 'Your video caption'
    api.upload_video(video_path, caption)

# schedule, change the number to however many hours it will repeat
schedule.every(4).hours.do(upload_random_video)

# run an infinite loop
while True:
    schedule.run_pending()
    time.sleep(1)
