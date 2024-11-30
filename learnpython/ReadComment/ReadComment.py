import mss
from PIL import Image
import pytesseract
import cv2
from pytesseract import Output
import re

def CaptureScreen():
    # Khởi tạo đối tượng MSS
    with mss.mss() as sct:
        # Lấy ảnh chụp màn hình và lưu vào đường dẫn chỉ định
        screenshot = sct.shot(output=r"D:\python\learnpython\ReadComment\captures\screenshot.png")
        print("Đã chụp ảnh màn hình và lưu vào file screenshot.png")
    
    # Cấu hình đường dẫn tới Tesseract (nếu bạn dùng Windows, thay thế đường dẫn sau)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Mở hình ảnh
    image = Image.open(r"D:\python\learnpython\ReadComment\captures\screenshot.png")

    # Lấy danh sách ngôn ngữ có sẵn
    ngon_ngu = pytesseract.get_available_languages()
    print("Danh sách ngôn ngữ hỗ trợ:", ngon_ngu)

    # Sử dụng Tesseract để nhận diện chữ
    text = pytesseract.image_to_string(image)
    # In kết quả nhận diện
    print("Văn bản nhận diện được:", text)

# Gọi hàm CaptureScreen
CaptureScreen()

def DetectData():
    img = cv2.imread('D:\python\learnpython\ReadComment\captures\Capture2.PNG')
    # d = pytesseract.image_to_data(img, output_type=Output.DICT)
    # keys = list(d.keys())

    # date_pattern1 = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
    # date_pattern2 = '111-222-333'

    # n_boxes = len(d['text'])
    # for i in range(n_boxes):
    #     if int(d['conf'][i]) > 60:
    #         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    #         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    	    # if re.match(date_pattern2, d['text'][i]):
	        #     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        #     img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    custom_config = r'-l vie+eng --psm 6'
    output = pytesseract.image_to_string(img, config=custom_config)
    print(output)

CaptureScreen()