import yt_dlp
import os

DOWNLOAD_DIR = "/tmp" 

def download_media(url: str, media_format: str = "mp4") -> tuple[str, bool, str]:
    try:
        if not os.path.exists(DOWNLOAD_DIR):
            os.makedirs(DOWNLOAD_DIR)

        options = {
            "quiet": True,
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        }

        if media_format == "mp3":
            options.update({
                "format": "bestaudio/best",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                }],
            })
        else:
            options.update({"format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"})

        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            if media_format == "mp3":
                filename = filename.rsplit('.', 1)[0] + ".mp3"

        return ("Success", True, filename)
    except Exception as e:
        return (str(e), False, "")