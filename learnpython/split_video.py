import os
import yt_dlp
import openpyxl
from vtt_to_srt.vtt_to_srt import ConvertFile

video_paths = {
    'dev_path': r'D:\videos_store\dev',
    'eng_path': r'D:\videos_store\english',
    'ourplanet_path': r'D:\videos_store\ourplanet',
    'student_path': r'D:\videos_store\student',
    'vancar_path': r'D:\videos_store\vancar'
}

#Đường dẫn tuyệt đối tới thư mục chứa file ffmpeg.exe
ffmpeg_dir = r'D:\python\learnpython\ffmpeg-master-latest-win64-gpl-shared\bin'

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
    
    download_cmd = f'yt-dlp --write-auto-sub --sub-lang "en.*" -P "{directory_to_clear}" "{cellurl_value}" -o "{cellname_value}"'
    os.system(download_cmd)

    subvtt_file = fr'{directory_to_clear}\{cellname_value}.en.vtt'
    # Kiểm tra và convert file VTT sang SRT nếu tồn tại
    try:
        # Kiểm tra xem file tồn tại hay không
        if os.path.exists(subvtt_file):
            convert_file = ConvertFile(subvtt_file, "utf-8")
            convert_file.convert()
        else:
            print(f"File {subvtt_file} does not exist. Skipping this task.")
    except FileNotFoundError:
        print(f"File not found: {subvtt_file}. Skipping this task.")

    download_cmd = f'yt-dlp -f 398+140 -P "{directory_to_clear}" --merge-output-format mp4  "{cellurl_value}" -o "{cellname_value}"'
    os.system(download_cmd)

    print(f"Vị trí directory_to_clear: {directory_to_clear}")
    # Chuyển đến thư mục chứa ffmpeg.exe
    os.chdir(ffmpeg_dir)
    audio_file = fr'{directory_to_clear}\{cellname_value}.f140.m4a'
    video_file = fr'{directory_to_clear}\{cellname_value}.f398.mp4'
    compile_file = fr'{directory_to_clear}\{cellname_value}.mp4'
    subsrt_file = fr'{directory_to_clear}\{cellname_value}.en.srt'
    input_file = fr'{directory_to_clear}\{cellname_value}_srt.mp4'

    #Ghep subtitles vao video truoc khi merge video va audio
    embedvideo_cmd = f'ffmpeg -i "{compile_file}" -vf subtitles="{subsrt_file}" "{input_file}"'
    os.system(embedvideo_cmd)

    cmd_merge = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac "{input_file}"'
    os.system(cmd_merge)

    # Lệnh cmd để chạy ffmpeg (ví dụ: cắt video)
    output_name = "output"
    output_file = fr'{directory_to_clear}\{output_name}.mp4'

    if i == 2:
        empty_cell_count = 0
        row_index = 2
        while True:
            cell_value = sheet.cell(row=row_index, column=6).value  # Lấy giá trị ô trong cột F
    
            if cell_value is None or cell_value == '':
                break  # Dừng lại khi gặp ô rỗng đầu tiên
            else:
                empty_cell_count += 1
    
            row_index += 1

        print(f"Số thứ tự của ô rỗng đầu tiên trong cột A là: {empty_cell_count}")
        if empty_cell_count > 0: 
            for j in range(empty_cell_count):   
                duration_position1 = f'F{j+2}'  # Tạo vị trí ô dạng 'F{i}'
                duration_position2 = f'F{j+2+1}'  # Tạo vị trí ô dạng 'F{i+1}'

                print(f"Vị trí duration_position1: {duration_position1}")
                print(f"Vị trí duration_position2: {duration_position2}")

                duration_value1 = sheet[duration_position1].value
                duration_value2 = sheet[duration_position2].value

                print(f"Vị trí duration_value2: {duration_value2}")
                if duration_value2 == None:
                    break
                cmd_split = f'ffmpeg -i "{input_file}" -ss {duration_value1} -to {duration_value2} -c:v copy -c:a copy "{output_file}"'
                # Thực thi lệnh cmd
                os.system(cmd_split)
                output_file = fr'{directory_to_clear}\{output_name}{j+1}.mp4'
    elif i == 3:
        empty_cell_count = 0
        row_index = 2
        while True:
            cell_value = sheet.cell(row=row_index, column=7).value  # Lấy giá trị ô trong cột G
    
            if cell_value is None or cell_value == '':
                break  # Dừng lại khi gặp ô rỗng đầu tiên
            else:
                empty_cell_count += 1
    
            row_index += 1

        print(f"Số thứ tự của ô rỗng đầu tiên trong cột A là: {empty_cell_count}")
        if empty_cell_count > 0: 
            for j in range(empty_cell_count):   
                duration_position1 = f'G{j+2}'  # Tạo vị trí ô dạng 'F{i}'
                duration_position2 = f'G{j+2+1}'  # Tạo vị trí ô dạng 'F{i+1}'

                print(f"Vị trí duration_position1: {duration_position1}")
                print(f"Vị trí duration_position2: {duration_position2}")

                duration_value1 = sheet[duration_position1].value
                duration_value2 = sheet[duration_position2].value

                print(f"Vị trí duration_value2: {duration_value2}")
                if duration_value2 == None:
                    break
                cmd_split = f'ffmpeg -i "{input_file}" -ss {duration_value1} -to {duration_value2} -c:v copy -c:a copy "{output_file}"'
                # Thực thi lệnh cmd
                os.system(cmd_split)
                output_file = fr'{directory_to_clear}\{output_name}{j+1}.mp4'
    elif i == 4:
        empty_cell_count = 0
        row_index = 2
        while True:
            cell_value = sheet.cell(row=row_index, column=8).value  # Lấy giá trị ô trong cột H
    
            if cell_value is None or cell_value == '':
                break  # Dừng lại khi gặp ô rỗng đầu tiên
            else:
                empty_cell_count += 1
    
            row_index += 1

        print(f"Số thứ tự của ô rỗng đầu tiên trong cột A là: {empty_cell_count}")
        if empty_cell_count > 0: 
            for j in range(empty_cell_count):   
                duration_position1 = f'H{j+2}'  # Tạo vị trí ô dạng 'F{i}'
                duration_position2 = f'H{j+2+1}'  # Tạo vị trí ô dạng 'F{i+1}'

                print(f"Vị trí duration_position1: {duration_position1}")
                print(f"Vị trí duration_position2: {duration_position2}")

                duration_value1 = sheet[duration_position1].value
                duration_value2 = sheet[duration_position2].value

                print(f"Vị trí duration_value2: {duration_value2}")
                if duration_value2 == None:
                    break
                cmd_split = f'ffmpeg -i "{input_file}" -ss {duration_value1} -to {duration_value2} -c:v copy -c:a copy "{output_file}"'
                # Thực thi lệnh cmd
                os.system(cmd_split)
                output_file = fr'{directory_to_clear}\{output_name}{j+1}.mp4'
    elif i == 5:
        empty_cell_count = 0
        row_index = 2
        while True:
            cell_value = sheet.cell(row=row_index, column=9).value  # Lấy giá trị ô trong cột I
    
            if cell_value is None or cell_value == '':
                break  # Dừng lại khi gặp ô rỗng đầu tiên
            else:
                empty_cell_count += 1
    
            row_index += 1

        print(f"Số thứ tự của ô rỗng đầu tiên trong cột A là: {empty_cell_count}")
        if empty_cell_count > 0: 
            for j in range(empty_cell_count):   
                duration_position1 = f'I{j+2}'  # Tạo vị trí ô dạng 'F{i}'
                duration_position2 = f'I{j+2+1}'  # Tạo vị trí ô dạng 'F{i+1}'

                print(f"Vị trí duration_position1: {duration_position1}")
                print(f"Vị trí duration_position2: {duration_position2}")

                duration_value1 = sheet[duration_position1].value
                duration_value2 = sheet[duration_position2].value

                print(f"Vị trí duration_value2: {duration_value2}")
                if duration_value2 == None:
                    break
                cmd_split = f'ffmpeg -i "{input_file}" -ss {duration_value1} -to {duration_value2} -c:v copy -c:a copy "{output_file}"'
                # Thực thi lệnh cmd
                os.system(cmd_split)
                output_file = fr'{directory_to_clear}\{output_name}{j+1}.mp4'
    else:
        empty_cell_count = 0
        row_index = 2
        while True:
            cell_value = sheet.cell(row=row_index, column=10).value  # Lấy giá trị ô trong cột J
    
            if cell_value is None or cell_value == '':
                break  # Dừng lại khi gặp ô rỗng đầu tiên
            else:
                empty_cell_count += 1
    
            row_index += 1

        print(f"Số thứ tự của ô rỗng đầu tiên trong cột A là: {empty_cell_count}")
        if empty_cell_count > 0: 
            for j in range(empty_cell_count):   
                duration_position1 = f'J{j+2}'  # Tạo vị trí ô dạng 'F{i}'
                duration_position2 = f'J{j+2+1}'  # Tạo vị trí ô dạng 'F{i+1}'

                print(f"Vị trí duration_position1: {duration_position1}")
                print(f"Vị trí duration_position2: {duration_position2}")

                duration_value1 = sheet[duration_position1].value
                duration_value2 = sheet[duration_position2].value

                print(f"Vị trí duration_value2: {duration_value2}")
                if duration_value2 == None:
                    break
                cmd_split = f'ffmpeg -i "{input_file}" -ss {duration_value1} -to {duration_value2} -c:v copy -c:a copy "{output_file}"'
                # Thực thi lệnh cmd
                os.system(cmd_split)
                output_file = fr'{directory_to_clear}\{output_name}{j+1}.mp4'
    i += 1
# Đóng workbook sau khi sử dụng
wb.close()