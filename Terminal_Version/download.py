import yt_dlp
import os
import re

DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Desktop")

def sanitize_filename(s, max_length = 100):
    s = re.sub(r'[\\/*?:"<>|]', "_", s)
    if len(s) > max_length:
        s = s[:max_length]
    return s

def download_media(url: str, media_format: str = "mp4", progress_callback=None) -> tuple[str, bool]:
    try:
        if "http" not in url:
            return ("Invalid link", False)

        def progress_hook(d):
            if progress_callback:
                progress_callback(d)

        options = {
            "progress_hooks": [progress_hook],
            "quiet": False,
            "no_warnings" : True,
        }
        if media_format.lower() == "mp4":
            options.update({
                "format" : "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
            })
        elif media_format.lower() == "mp3":
            options.update({
                "format" : "bestaudio/best",
                "outtmpl" : os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
                "postprocessors" : [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:
            return (f"Unsupported media format: {media_format}", False)

        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download = False)
            title = sanitize_filename(info['title'], max_length = 100)
            options["outtmpl"] = os.path.join(DOWNLOAD_DIR, f"{title}.%(ext)s")
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
                title = sanitize_filename(info['title'], max_length = 100)
            filename = os.path.join(DOWNLOAD_DIR, f"{title}.{media_format.lower()}")
            return (f"Downloaded: {filename}", True)

    except Exception as e:
        return (f"Something went wrong: {e}", False)

if __name__ == "__main__":
    print("--- Video/Audio Downloader (Terminal Version) ---")
    link = input("Input link (URL): ").strip()
    choice = input("Do you want download ony MP3? (y/n): ").strip().lower()
    
    fmt = "mp3" if choice in ["y", "այո", "յ"] else "mp4"
    
    message, success = download_media(link, fmt)
    print(message)