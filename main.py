import schedule
import time
from TikTokApi import TikTokApi

# Create an instance of the TikTok API
api = TikTokApi()

# Function to upload the video
def upload_video():
    # TODO: Replace 'video_path' with the actual path of your video file
    video_path = 'C:/Users/ramon/Desktop/Project Nexoswave/tiktoks/kanon.mp4'
    
    # TODO: Replace 'caption' with the desired caption for the video
    caption = 'Get it now, link in bio! #tiktokmademebuyit #nexoswave #summer'
    
    # Upload the video
    api.upload_video(video_path, caption)

# Schedule the video upload every 4 hours
schedule.every(4).hours.do(upload_video)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
