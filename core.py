import yt_dlp
import os

DOWNLOAD_DIR = "/tmp"

def download_media(url: str, media_format: str = "mp4") -> tuple[str, bool, str]:
    if "youtube.com" in url or "youtu.be" in url:
        return ("YouTube downloading is currently disabled due to provider restrictions.", False, "")

    try:
        if not os.path.exists(DOWNLOAD_DIR):
            os.makedirs(DOWNLOAD_DIR)

        options = {
            "quiet": True,
            "no_warnings": True,
            "ffmpeg_location": "./ffmpeg",
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
            "nocheckcertificate": True,
        }

        if media_format == "mp3":
            options.update({
                "format": "bestaudio/best",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            })
        else:
            options.update({"format": "best"})

        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            if media_format == "mp3":
                filename = filename.rsplit('.', 1)[0] + ".mp3"

        return ("Success", True, filename)
    except Exception as e:
        return (str(e), False, "")