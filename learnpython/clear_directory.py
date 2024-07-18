import os

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