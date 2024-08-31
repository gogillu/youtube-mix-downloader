import yt_dlp

def download_youtube_mix(mix_url, download_path="downloads"):
    # yt-dlp options for extracting audio and converting it to mp3
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'ignoreerrors': True,  # Skip errors to keep downloading
        'noplaylist': False,  # Ensure the entire playlist (mix) is downloaded
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([mix_url])

if __name__ == "__main__":
    mix_url = input("Enter the YouTube Mix URL: ")
    download_youtube_mix(mix_url)
