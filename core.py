import yt_dlp
import os
from moviepy.editor import VideoFileClip

DEFAULT_DOWNLOAD_FORMAT = 'bestvideo+bestaudio/best'

def is_valid_url(url):
    return url.strip().startswith(('http://', 'https://'))

def baixar_video_core(url, destino, progress_hook):
    """Lógica central de download."""
    ydl_opts = {
        'format': DEFAULT_DOWNLOAD_FORMAT,
        'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'nocheckcertificate': True,
        'quiet': True,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        title = info_dict.get("title", "video_sem_titulo")
        ext = info_dict.get("ext", "mp4")
        return os.path.join(destino, f"{title}.{ext}")

def converter_para_mp3_core(caminho_video):
    """Lógica central de conversão."""
    if not caminho_video or not os.path.exists(caminho_video):
        raise FileNotFoundError("Arquivo não encontrado.")

    mp3_path = os.path.splitext(caminho_video)[0] + ".mp3"
    with VideoFileClip(caminho_video) as video:
        if not video.audio:
            raise ValueError("O vídeo não contém áudio.")
        video.audio.write_audiofile(mp3_path)
    return mp3_path
