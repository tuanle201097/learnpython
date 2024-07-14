import yt_dlp
import subprocess

def cut_video(video_url, start_time, end_time, output_filename):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict.get('url')
        ffmpeg_command = [
            'ffmpeg', '-i', video_url,
            '-ss', start_time,
            '-to', end_time,
            '-c', 'copy',
            output_filename
        ]
        subprocess.run(ffmpeg_command, capture_output=True)

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=Zjl2vmy02As"
    start_time = "00:01:00"
    end_time = "00:02:00"
    output_filename = "output.mp4"

    cut_video(video_url, start_time, end_time, output_filename)
