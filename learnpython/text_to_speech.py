from gtts import gTTS

def text_to_speech(text_file, output_audio_file):
    # Đọc nội dung từ file text
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Chuyển đổi văn bản thành giọng đọc AI
    tts = gTTS(text, lang='en')  # 'vi' là mã ngôn ngữ cho tiếng Việt

    # Lưu giọng đọc thành file âm thanh
    tts.save(output_audio_file)
    print("Done")

# Đường dẫn đến file text và file âm thanh đầu ra
text_file = 'english.txt'
output_audio_file = 'output_audio.mp3'

# Gọi hàm để chuyển đổi và lưu file âm thanh
text_to_speech(text_file, output_audio_file)
