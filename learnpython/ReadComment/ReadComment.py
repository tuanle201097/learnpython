import mss
from PIL import Image
import pytesseract
import cv2
from pytesseract import Output
import re

def CaptureScreen():
    # Khởi tạo đối tượng MSS
    with mss.mss() as sct:
        screenshot = None
        # Lấy ảnh chụp màn hình và lưu vào đường dẫn chỉ định
        screenshot = sct.shot(output=r"D:\python\learnpython\ReadComment\captures\screenshot.png")
        print("Đã chụp ảnh màn hình và lưu vào file screenshot.png")
    
    # Cấu hình đường dẫn tới Tesseract (nếu bạn dùng Windows, thay thế đường dẫn sau)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Mở hình ảnh
    image = Image.open(screenshot)

    # Lấy danh sách ngôn ngữ có sẵn
    ngon_ngu = pytesseract.get_languages()
    print("Danh sách ngôn ngữ hỗ trợ:", ngon_ngu)

    custom_config = r'-l eng --psm 6'
    output = pytesseract.image_to_string(image, config=custom_config)


    print(output)

def DetectData(date_pattern,word_pattern):
    img = cv2.imread('D:\\python\\learnpython\\ReadComment\\captures\\Capture2.PNG')
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            text = d['text'][i]

            # Kiểm tra nếu từ trùng khớp với biểu thức chính quy ngày tháng
            if re.match(date_pattern, text):
                print(f"Ngày tháng phát hiện: {text}")
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Kiểm tra nếu từ trùng khớp với từ "File"
            if re.match(word_pattern, text, re.IGNORECASE):  # Thêm re.IGNORECASE để tìm cả "file" và "File"
                print(f"Từ 'File' phát hiện: {text}")
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Đổi màu cho từ 'File'

    # Hiển thị ảnh với các hình chữ nhật xung quanh từ nhận diện
    cv2.imshow('img', img)
    cv2.waitKey(0)
# CaptureScreen()
# Biểu thức chính quy tìm ngày tháng
date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
# Biểu thức chính quy tìm kiếm từ "File"
word_pattern = 'File'

DetectData('4','Tesseract')