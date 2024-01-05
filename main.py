from pytube import YouTube
import os

def download_from_youtube(url):
    try:
        video = YouTube(url)
        print(f'Name:{video.title}')
        print(f'Length:{video.length}sec.')
        print(f'Size of video:{video.streams.get_highest_resolution().filesize/1024**2:.2f}Mb')

        desktop_path = os.path.expanduser("~/Desktop")
        video.streams.get_highest_resolution().download(output_path=desktop_path)
        print('Video saved in your desktop.')
    except Exception as e:
        print(f'something went wrong: {e}')
    
