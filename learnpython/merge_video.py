import os
import yt_dlp
from vtt_to_srt.vtt_to_srt import ConvertFile
#Đường dẫn tuyệt đối tới thư mục chứa file ffmpeg.exe
ffmpeg_dir = r'D:\python\learnpython\ffmpeg-master-latest-win64-gpl-shared\bin'

def merge_video(directory_path,name_video):
    # Chuyển đến thư mục chứa ffmpeg.exe
    os.chdir(ffmpeg_dir)
    
    audio_file = fr'{directory_path}\{name_video}.f140.m4a'
    video_file = fr'{directory_path}\{name_video}.f398.mp4'
    compile_file = fr'{directory_path}\{name_video}.webm'
    subsrt_file = fr'{directory_path}\{name_video}.en.srt'
    input_file = fr'{directory_path}\{name_video}_srt.mp4'

    # #Ghep subtitles vao video truoc khi merge video va audio
    # embedvideo_cmd = f'ffmpeg -i "{compile_file}" -vf subtitles="{subsrt_file}" "{input_file}"'
    # os.system(embedvideo_cmd)
    # cmd_merge = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac "{compile_file}"'
    # os.system(cmd_merge)
    return compile_file