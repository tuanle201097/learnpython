import os
import yt_dlp

download_cmd = f'yt-dlp -f 398+140 --merge-output-format mp4  https://www.youtube.com/watch?v=Zjl2vmy02As'
os.system(download_cmd)
#rename file da tai
os.rename(r'D:\python\learnpython\A Day in the Life of a Software Engineer... WFH [Zjl2vmy02As].f140.m4a', r'D:\python\learnpython\audio.m4a')
os.rename(r'D:\python\learnpython\A Day in the Life of a Software Engineer... WFH [Zjl2vmy02As].f398.mp4', r'D:\python\learnpython\video.mp4')

# #Đường dẫn tuyệt đối tới thư mục chứa file ffmpeg.exe
ffmpeg_dir = r'D:\python\learnpython\ffmpeg-master-latest-win64-gpl-shared\bin'
# Chuyển đến thư mục chứa ffmpeg.exe
os.chdir(ffmpeg_dir)
audio_file = r'D:\python\learnpython\audio.m4a'
video_file = r'D:\python\learnpython\video.mp4'
input_file = r'D:\python\learnpython\input.mp4'

cmd_merge = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac "{input_file}"'

os.system(cmd_merge)

# Lệnh cmd để chạy ffmpeg (ví dụ: cắt video)
output_file = r'D:\python\learnpython\output.mp4'
cmd_split = f'ffmpeg -i "{input_file}" -ss 00:00:10 -to 00:00:20 -c:v copy -c:a copy "{output_file}"'

# Thực thi lệnh cmd
os.system(cmd_split)