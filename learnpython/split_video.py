import os
import yt_dlp
import openpyxl
from vtt_to_srt.vtt_to_srt import ConvertFile

import clear_directory
import getInfo_excel
import merge_video

video_paths = {
    # 'dev_path': r'D:\videos_store\dev',
    'eng_path': r'D:\videos_store\english',
    'ourplanet_path': r'D:\videos_store\ourplanet',
    'student_path': r'D:\videos_store\student',
    'vancar_path': r'D:\videos_store\vancar'
}

#Đường dẫn tuyệt đối tới thư mục chứa file ffmpeg.exe
ffmpeg_dir = r'D:\python\learnpython\ffmpeg-master-latest-win64-gpl-shared\bin'

# # Đọc dữ liệu từ file Excel
# # Chuyển đến thư mục chứa youtube_url.xlsx
# excel_dir = r'D:\python\learnpython'
# os.chdir(excel_dir)
file_path = fr'D:\python\learnpython\youtube_url.xlsx'  # Thay đổi đường dẫn tới file Excel của bạn

for key, value in video_paths.items():
    # Thay đổi thành đường dẫn thư mục mà bạn muốn xóa các tệp
    directory_to_clear = value
    # Gọi hàm để xóa các tệp trong thư mục
    clear_directory.clear_directory(directory_to_clear)
i = 3
for key, value in video_paths.items():
    directory_to_clear = value

    cellurl_value,cellname_value = getInfo_excel.getInfor(file_path,i,1,None,None)
    
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
    #Đường dẫn tuyệt đối tới thư mục chứa file ffmpeg.exe
    ffmpeg_dir = r'D:\python\learnpython\ffmpeg-master-latest-win64-gpl-shared\bin'
    # Chuyển đến thư mục chứa ffmpeg.exe
    os.chdir(ffmpeg_dir)
    # download_cmd = f'yt-dlp -f "bv*[ext=webm]+ba[ext=webm]/b[ext=webm] / bv*+ba/b" -P "{directory_to_clear}" --merge-output-format webm  "{cellurl_value}" -o "{cellname_value}"'
    download_cmd = f'yt-dlp -f "248+251" -P "{directory_to_clear}" --merge-output-format webm  "{cellurl_value}" -o "{cellname_value}"'
    os.system(download_cmd)

    input_file = None
    input_srt = None
    # input_file = merge_video.merge_video(directory_to_clear,cellname_value)

    input_file = fr'{directory_to_clear}\{cellname_value}.webm'
    input_srt = fr'{directory_to_clear}\{cellname_value}.en.srt'

    print(f"Vị trí directory_to_clear: {directory_to_clear}")

    # Lệnh cmd để chạy ffmpeg (ví dụ: cắt video)
    output_name = cellname_value
    output_file = fr'{directory_to_clear}\{output_name}"-P1".webm'

    output_srt = cellname_value
    output_srt_file = fr'{directory_to_clear}\{output_name}"-P1".srt'

    if i == 2:
        empty_cell_count = 0
        row_index = 2
        while True:
            cell_value,name_value = getInfo_excel.getInfor(file_path,i,2,row_index,6)  # Lấy giá trị ô trong cột F
    
            if cell_value is None or cell_value == '':
                break  # Dừng lại khi gặp ô rỗng đầu tiên
            else:
                empty_cell_count += 1
    
            row_index += 1

        print(f"Số thứ tự của ô rỗng đầu tiên trong cột A là: {empty_cell_count}")
        if empty_cell_count > 0: 
            index = 2
            for j in range(empty_cell_count):
                duration_value1 = None
                duration_value2 = None
                duration_value1,duration_value2 = getInfo_excel.getInfor(file_path,i,3,index,6)  # Lấy giá trị ô trong cột F

                print(f"Vị trí duration_value2: {duration_value2}")
                if duration_value2 == None:
                    break
                cmd_split = f'ffmpeg -i "{input_file}" -ss {duration_value1} -to {duration_value2} -c:v copy -c:a copy -c:s mov_text "{output_file}"'
                # Thực thi lệnh cmd
                os.system(cmd_split)
                #Ghep subtitles vao video truoc khi merge video va audio
                splitsrt_cmd = f'ffmpeg -i {input_srt} -ss {duration_value1} -to {duration_value2} -c copy {output_srt_file}"'
                os.system(splitsrt_cmd)
                output_file = fr'{directory_to_clear}\{output_name}"-P"{j+2}.webm'
                output_srt_file = fr'{directory_to_clear}\{output_name}"-P"{j+2}.srt'
                index +=1
    elif i == 3:
        empty_cell_count = 0
        row_index = 2
        while True:
            cell_value,name_value = getInfo_excel.getInfor(file_path,i,2,row_index,7)  # Lấy giá trị ô trong cột G
    
            if cell_value is None or cell_value == '':
                break  # Dừng lại khi gặp ô rỗng đầu tiên
            else:
                empty_cell_count += 1
    
            row_index += 1

        print(f"Số thứ tự của ô rỗng đầu tiên trong cột A là: {empty_cell_count}")
        if empty_cell_count > 0: 
            index = 2
            for j in range(empty_cell_count):   
                duration_value1 = None
                duration_value2 = None
                duration_value1,duration_value2 = getInfo_excel.getInfor(file_path,i,3,index,7)  # Lấy giá trị ô trong cột F

                print(f"Vị trí duration_value2: {duration_value2}")
                if duration_value2 == None:
                    break
                cmd_split = f'ffmpeg -i "{input_file}" -ss {duration_value1} -to {duration_value2} -c:v copy -c:a copy -c:s mov_text "{output_file}"'
                # Thực thi lệnh cmd
                os.system(cmd_split)
                #Ghep subtitles vao video truoc khi merge video va audio
                splitsrt_cmd = f'ffmpeg -i {input_srt} -ss {duration_value1} -to {duration_value2} -c copy {output_srt_file}"'
                os.system(splitsrt_cmd)
                output_file = fr'{directory_to_clear}\{output_name}"-P"{j+2}.webm'
                output_srt_file = fr'{directory_to_clear}\{output_name}"-P"{j+2}.srt'
                index +=1
    elif i == 4:
        empty_cell_count = 0
        row_index = 2
        while True:
            cell_value,name_value = getInfo_excel.getInfor(file_path,i,2,row_index,8)  # Lấy giá trị ô trong cột H
    
            if cell_value is None or cell_value == '':
                break  # Dừng lại khi gặp ô rỗng đầu tiên
            else:
                empty_cell_count += 1
    
            row_index += 1

        print(f"Số thứ tự của ô rỗng đầu tiên trong cột A là: {empty_cell_count}")
        if empty_cell_count > 0: 
            index = 2
            for j in range(empty_cell_count):   
                duration_value1 = None
                duration_value2 = None
                duration_value1,duration_value2 = getInfo_excel.getInfor(file_path,i,3,index,8)  # Lấy giá trị ô trong cột F

                print(f"Vị trí duration_value2: {duration_value2}")
                if duration_value2 == None:
                    break
                cmd_split = f'ffmpeg -i "{input_file}" -ss {duration_value1} -to {duration_value2} -c:v copy -c:a copy -c:s mov_text "{output_file}"'
                # Thực thi lệnh cmd
                os.system(cmd_split)
                #Ghep subtitles vao video truoc khi merge video va audio
                splitsrt_cmd = f'ffmpeg -i {input_srt} -ss {duration_value1} -to {duration_value2} -c copy {output_srt_file}"'
                os.system(splitsrt_cmd)
                output_file = fr'{directory_to_clear}\{output_name}"-P"{j+2}.webm'
                output_srt_file = fr'{directory_to_clear}\{output_name}"-P"{j+2}.srt'
                index +=1
    elif i == 5:
        empty_cell_count = 0
        row_index = 2
        while True:
            cell_value,name_value = getInfo_excel.getInfor(file_path,i,2,row_index,9)  # Lấy giá trị ô trong cột I
    
            if cell_value is None or cell_value == '':
                break  # Dừng lại khi gặp ô rỗng đầu tiên
            else:
                empty_cell_count += 1
    
            row_index += 1

        print(f"Số thứ tự của ô rỗng đầu tiên trong cột A là: {empty_cell_count}")
        if empty_cell_count > 0: 
            index = 2
            for j in range(empty_cell_count):   
                duration_value1 = None
                duration_value2 = None
                duration_value1,duration_value2 = getInfo_excel.getInfor(file_path,i,3,index,9)  # Lấy giá trị ô trong cột F

                print(f"Vị trí duration_value2: {duration_value2}")
                if duration_value2 == None:
                    break
                cmd_split = f'ffmpeg -i "{input_file}" -ss {duration_value1} -to {duration_value2} -c:v copy -c:a copy -c:s mov_text "{output_file}"'
                # Thực thi lệnh cmd
                os.system(cmd_split)
                #Ghep subtitles vao video truoc khi merge video va audio
                splitsrt_cmd = f'ffmpeg -i {input_srt} -ss {duration_value1} -to {duration_value2} -c copy {output_srt_file}"'
                os.system(splitsrt_cmd)
                output_file = fr'{directory_to_clear}\{output_name}"-P"{j+2}.webm'
                output_srt_file = fr'{directory_to_clear}\{output_name}"-P"{j+2}.srt'
                index +=1
    else:
        empty_cell_count = 0
        row_index = 2
        while True:
            cell_value,name_value = getInfo_excel.getInfor(file_path,i,2,row_index,10)  # Lấy giá trị ô trong cột J
    
            if cell_value is None or cell_value == '':
                break  # Dừng lại khi gặp ô rỗng đầu tiên
            else:
                empty_cell_count += 1
    
            row_index += 1

        print(f"Số thứ tự của ô rỗng đầu tiên trong cột A là: {empty_cell_count}")
        if empty_cell_count > 0: 
            index = 2
            for j in range(empty_cell_count):   
                duration_value1 = None
                duration_value2 = None
                duration_value1,duration_value2 = getInfo_excel.getInfor(file_path,i,3,index,10)  # Lấy giá trị ô trong cột F

                print(f"Vị trí duration_value2: {duration_value2}")
                if duration_value2 == None:
                    break
                cmd_split = f'ffmpeg -i "{input_file}" -ss {duration_value1} -to {duration_value2} -c:v copy -c:a copy -c:s mov_text "{output_file}"'
                # Thực thi lệnh cmd
                os.system(cmd_split)
                #Ghep subtitles vao video truoc khi merge video va audio
                splitsrt_cmd = f'ffmpeg -i {input_srt} -ss {duration_value1} -to {duration_value2} -c copy {output_srt_file}"'
                os.system(splitsrt_cmd)
                output_file = fr'{directory_to_clear}\{output_name}"-P"{j+2}.webm'
                output_srt_file = fr'{directory_to_clear}\{output_name}"-P"{j+2}.srt'
                index +=1
    i += 1