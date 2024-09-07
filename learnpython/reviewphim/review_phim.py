import os
import yt_dlp
import openpyxl
from vtt_to_srt.vtt_to_srt import ConvertFile
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
from pydub import AudioSegment
import pyttsx3

#Đường dẫn tuyệt đối tới thư mục chứa file ffmpeg.exe
ffmpeg_dir = r'D:\python\learnpython\ffmpeg-master-latest-win64-gpl-shared\bin'
output_path = r'D:\videos_store\review'
#Tai video mp4 ve
# Chuyển đến thư mục chứa ffmpeg.exe
os.chdir(ffmpeg_dir)
download_cmd = f'yt-dlp -f bestvideo[ext=mp4] "https://www.youtube.com/watch?v=gmqlNXgh3rQ" -P "{output_path}" -o "output_video.mp4"'
os.system(download_cmd)

#Tai subtitle va chuyen thanh audio
os.chdir(output_path)
# Đường dẫn đến file text và file âm thanh đầu ra
text_file = 'subtitles.txt'
output_audio_file = 'output_audio.mp3'

def text_to_speech2(text_file, output_audio_file):
    # Đọc nội dung từ file text
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    # Chuyển đổi văn bản thành giọng đọc AI
    tts = gTTS(text, lang='vi', slow=False)  # 'vi' là mã ngôn ngữ cho tiếng Việt

    # Lưu giọng đọc thành file âm thanh
    tts.save(output_audio_file)
    print("Done")
#Gọi hàm để chuyển đổi và lưu file âm thanhy
text_to_speech2(text_file, output_audio_file)

# Chuyển đến thư mục chứa ffmpeg.exe
os.chdir(ffmpeg_dir)

cmd_speed = 'ffmpeg -i "D:/videos_store/review/output_audio.mp3" -filter:a "atempo=1.7" "D:/videos_store/review/output.mp3"'
# Thực thi lệnh cmdy
os.system(cmd_speed)

cmd_merge = 'ffmpeg -i "D:/videos_store/review/output_video.mp4" -i "D:/videos_store/review/output.mp3" -c:v copy -c:a aac -strict experimental "D:/videos_store/review/output_complex.mp4"'
# Thực thi lệnh cmd
os.system(cmd_merge)