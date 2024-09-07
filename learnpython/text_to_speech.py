from gtts import gTTS
from pydub import AudioSegment
import os
import pyttsx3
#Đường dẫn tuyệt đối tới thư mục chứa file ffmpeg.exe
ffmpeg_dir = r'D:\python\learnpython\ffmpeg-master-latest-win64-gpl-shared\bin'

def text_to_speech1(text_file,mp3_filename):
    # Chuyển đến thư mục chứa ffmpeg.exe
    os.chdir(ffmpeg_dir)
    # Khởi tạo engine
    engine = pyttsx3.init()
    # Đặt tốc độ đọc (từ 0 đến 1)
    engine.setProperty('rate', 200)  # Tốc độ mặc định là 200

    # Đặt giọng đọc (sử dụng index)
    voices = engine.getProperty('voices')  # Lấy danh sách các giọng đọc hiện có
    for voice in voices:
        print(voice)
    engine.setProperty('voice', voices[2].id)  # Chọn một giọng đọc (index 1 là giọng đọc nam)
    # Đọc nội dung từ file text
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
        # Chuyển đổi văn bản thành giọng nói
        engine.say(text)
        engine.save_to_file(text,mp3_filename)
        # Chờ engine đọc xong
        engine.runAndWait()
def text_to_speech2(text_file, output_audio_file):
    # Đọc nội dung từ file text
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    # Chuyển đổi văn bản thành giọng đọc AI
    tts = gTTS(text, lang='vi', slow=False)  # 'vi' là mã ngôn ngữ cho tiếng Việt

    # Lưu giọng đọc thành file âm thanh
    tts.save(output_audio_file)
    print("Done")

# Đặt tên file đầu ra
wav_filename = "D:\python\learnpython\output.wav"
mp3_filename = "D:\python\learnpython\output.mp3"
# Đường dẫn đến file text và file âm thanh đầu ra
text_file = "D:\python\learnpython\subtitles.txt"
output_audio_file = 'output_audio.mp3'
text_file2 = "Xin chào, đây là một ví dụ về chuyển đổi văn bản thành giọng nói bằng pyttsx3."

#Gọi hàm để chuyển đổi và lưu file âm thanh
text_to_speech2(text_file, output_audio_file)
# Gọi hàm để chuyển đổi và lưu file âm thanh
# text_to_speech1(text_file, mp3_filename)


# #Đường dẫn tuyệt đối tới thư mục chứa file ffmpeg.exe
# ffmpeg_dir = r'D:\python\learnpython\ffmpeg-master-latest-win64-gpl-shared\bin'
# # Chuyển đến thư mục chứa ffmpeg.exe
# os.chdir(ffmpeg_dir)

# cmd_speed = 'ffmpeg -i D:\python\learnpython\output_audio.mp3 -filter:a "atempo=1.7" D:\python\learnpython\output.mp3'
# # Thực thi lệnh cmd
# os.system(cmd_speed)