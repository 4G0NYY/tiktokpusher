import schedule
import time
import random
import os
from TikTokApi import TikTokApi

# Create an instance of the TikTok API
api = TikTokApi()

# Function to upload a random video
def upload_random_video():
    # TODO: Replace 'video_folder' with the path to your video folder
    video_folder = 'path/to/your/video/folder'
    
    # Get a list of all video files in the folder
    video_files = os.listdir(video_folder)
    
    # Choose a random video file
    random_video = random.choice(video_files)
    
    # Construct the full path to the selected video file
    video_path = os.path.join(video_folder, random_video)
    
    # TODO: Replace 'caption' with the desired caption for the video
    caption = 'Your video caption'
    
    # Upload the video
    api.upload_video(video_path, caption)

# Schedule the random video upload every 4 hours
schedule.every(4).hours.do(upload_random_video)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
