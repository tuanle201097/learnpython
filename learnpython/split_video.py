import os
import yt_dlp
import openpyxl

video_paths = {
    'dev_path': r'D:\videos_store\dev',
    'eng_path': r'D:\videos_store\english',
    'ourplanet_path': r'D:\videos_store\ourplanet',
    'student_path': r'D:\videos_store\student',
    'vancar_path': r'D:\videos_store\vancar'
}

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

for key, value in video_paths.items():
    # Thay đổi thành đường dẫn thư mục mà bạn muốn xóa các tệp
    directory_to_clear = value
    # Gọi hàm để xóa các tệp trong thư mục
    clear_directory(directory_to_clear)
i = 2
for key, value in video_paths.items():
    directory_to_clear = value
    # Đọc dữ liệu từ file Excel
    # Chuyển đến thư mục chứa youtube_url.xlsx
    excel_dir = r'D:\python\learnpython'
    os.chdir(excel_dir)
    file_path = 'youtube_url.xlsx'  # Thay đổi đường dẫn tới file Excel của bạn
    # Load workbook (bảng tính)
    wb = openpyxl.load_workbook(file_path)

    # Chọn sheet cụ thể (nếu cần)
    sheet = wb['Sheet1']  # Thay 'Sheet1' bằng tên của sheet bạn muốn đọc
    # Đọc dữ liệu từng ô
    # Ví dụ: Đọc giá trị từ ô c2
    cellurl_position = f'C{i}'  # Tạo vị trí ô dạng 'C{i}'
    cellname_position = f'E{i}'  # Tạo vị trí ô dạng 'E{i}'

    print(f"Vị trí ô: {cellurl_position}")
    print(f"Vị trí name: {cellname_position}")

    cellurl_value = sheet[cellurl_position].value
    cellname_value = sheet[cellname_position].value

    download_cmd = f'yt-dlp -f 398+140 -P "{directory_to_clear}" --merge-output-format mp4  "{cellurl_value}" -o "{cellname_value}"'
    os.system(download_cmd)

    print(f"Vị trí directory_to_clear: {directory_to_clear}")
    #Đường dẫn tuyệt đối tới thư mục chứa file ffmpeg.exe
    ffmpeg_dir = r'D:\python\learnpython\ffmpeg-master-latest-win64-gpl-shared\bin'
    # Chuyển đến thư mục chứa ffmpeg.exe
    os.chdir(ffmpeg_dir)
    audio_file = fr'{directory_to_clear}\{cellname_value}.f140.m4a'
    video_file = fr'{directory_to_clear}\{cellname_value}.f398.mp4'
    input_file = fr'{directory_to_clear}\{cellname_value}.mp4'

    cmd_merge = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac "{input_file}"'
    os.system(cmd_merge)

    # Lệnh cmd để chạy ffmpeg (ví dụ: cắt video)
    output_file = fr'{directory_to_clear}\output.mp4'

    cmd_split = f'ffmpeg -i "{input_file}" -ss 00:00:00 -to 00:01:58 -c:v copy -c:a copy "{output_file}"'
    # Thực thi lệnh cmd
    os.system(cmd_split)    

    i += 1
# Đóng workbook sau khi sử dụng
wb.close()