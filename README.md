Video downloader from almost every web-page (doesn't support youtube due to youtube's restrictions)
Visit: https://video-downloader-python.onrender.com

For youtube and others use the terminal version of code. Please note that you need to install libraries from "libraries.txt".

```
import yt_dlp
import os
import re

DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Desktop")

def sanitize_filename(s, max_length=100):
    s = re.sub(r'[\\/*?:"<>|]', "_", s)
    return s[:max_length]

def download_media(url: str, media_format: str = "mp4"):
    try:
        if "http" not in url:
            return ("Invalid Link!", False)

        options = {
            "quiet": False,
            "no_warnings": True,
            "nocheckcertificate": True,
            "ffmpeg_location": r"C:\ffmpeg\bin\ffmpeg.exe" if os.path.exists(r"C:\ffmpeg\bin\ffmpeg.exe") else "ffmpeg",
        }

        if media_format.lower() == "mp3":
            options.update({
                "format": "bestaudio/best",
                "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title).100s.%(ext)s"),
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            })
        else:
            options.update({
                "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title).100s.%(ext)s"),
            })

        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            title = sanitize_filename(info.get('title', 'video'), max_length=100)
            ext = "mp3" if media_format.lower() == "mp3" else "mp4"
            final_path = os.path.join(DOWNLOAD_DIR, f"{title}.{ext}")
            
            return (f"Done! File saved on your desktop {title}.{ext}", True)

    except Exception as e:
        return (f"Something went wrong: {e}", False)

if __name__ == "__main__":
    print("--- Video/Audio Downloader (Terminal Version) ---")
    link = input("Input link (URL): ").strip()
    choice = input("Do you want download ony MP3? (y/n): ").strip().lower()
    
    fmt = "mp3" if choice in ["y", "այո", "յ"] else "mp4"
    
    message, success = download_media(link, fmt)
    print(message)
```
