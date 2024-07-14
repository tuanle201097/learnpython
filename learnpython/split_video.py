import os
import yt_dlp

def clear_directory(directory):
    # Kiểm tra xem thư mục tồn tại không
    if not os.path.exists(directory):
        print(f"Thư mục '{directory}' không tồn tại.")
        return
    
    # Lặp qua các tệp trong thư mục
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        try:
            # Kiểm tra nếu là tệp tin thì xóa
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Đã xóa '{file_path}' thành công.")
            # Nếu là thư mục thì bỏ qua
            elif os.path.isdir(file_path):
                print(f"'{file_path}' là một thư mục, không xóa.")
        except Exception as e:
            print(f"Lỗi khi xóa '{file_path}': {e}")

# Thay đổi thành đường dẫn thư mục mà bạn muốn xóa các tệp
directory_to_clear = r'D:\python\learnpython\output_video'

# Gọi hàm để xóa các tệp trong thư mục
clear_directory(directory_to_clear)

download_cmd = f'yt-dlp -f 398+140 -P "{directory_to_clear}" --merge-output-format mp4  https://www.youtube.com/watch?v=Zjl2vmy02As'
os.system(download_cmd)
#rename file da tai
os.rename(r'D:\python\learnpython\output_video\A Day in the Life of a Software Engineer... WFH [Zjl2vmy02As].f140.m4a', r'D:\python\learnpython\output_video\audio.m4a')
os.rename(r'D:\python\learnpython\output_video\A Day in the Life of a Software Engineer... WFH [Zjl2vmy02As].f398.mp4', r'D:\python\learnpython\output_video\video.mp4')

# #Đường dẫn tuyệt đối tới thư mục chứa file ffmpeg.exe
ffmpeg_dir = r'D:\python\learnpython\ffmpeg-master-latest-win64-gpl-shared\bin'
# Chuyển đến thư mục chứa ffmpeg.exe
os.chdir(ffmpeg_dir)
audio_file = r'D:\python\learnpython\output_video\audio.m4a'
video_file = r'D:\python\learnpython\output_video\video.mp4'
input_file = r'D:\python\learnpython\output_video\input.mp4'

cmd_merge = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac "{input_file}"'

os.system(cmd_merge)

# Lệnh cmd để chạy ffmpeg (ví dụ: cắt video)
output_file = r'D:\python\learnpython\output_video\output.mp4'
cmd_split = f'ffmpeg -i "{input_file}" -ss 00:02:42 -to 00:03:35 -c:v copy -c:a copy "{output_file}"'

# Thực thi lệnh cmd
os.system(cmd_split)