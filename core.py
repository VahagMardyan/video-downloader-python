import yt_dlp
import os
import re

DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Desktop")

def sanitize_filename(s, max_length=100):
    s = re.sub(r'[\\/*?:"<>|]', "_", s)
    return s[:max_length]

def download_media(url: str, media_format: str = "mp4") -> tuple[str, bool]:
    try:
        if not url.startswith("http"):
            return ("Invalid link", False)

        options = {
            "quiet": True,
            "no_warnings": True,
        }

        if media_format == "mp4":
            options.update({
                "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
            })
        elif media_format == "mp3":
            options.update({
                "format": "bestaudio/best",
                "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            })
        else:
            return ("Unsupported format", False)

        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            title = sanitize_filename(info["title"])

        return (f"Downloaded: {title}", True)

    except Exception as e:
        return (str(e), False)
