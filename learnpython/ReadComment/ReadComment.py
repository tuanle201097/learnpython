import mss
from PIL import Image
import pytesseract
import cv2
from pytesseract import Output
import re
import np
import easyocr
from paddleocr import PaddleOCR

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

def DetectData(date_pattern,word_pattern,path):
    img = cv2.imread(path)
    # Cắt ảnh theo ROI (Region of Interest)
    roi = (1580, 119, 337, 858)
    x, y, w, h = roi
    roi_image = img[y:y+h, x:x+w]
    # Tiền xử lý hình ảnh: chuyển sang thang độ xám và tăng độ tương phản
    gray_image = cv2.cvtColor(roi_image, cv2.COLOR_BGR2GRAY)
    enhanced_image = cv2.equalizeHist(gray_image)

    # Áp dụng OCR trên ảnh đã xử lý
    ocr_data = pytesseract.image_to_data(enhanced_image, output_type=Output.DICT)
    
    n_boxes = len(ocr_data['text'])
    for i in range(n_boxes):
        if int(ocr_data['conf'][i]) > 60:
            text = ocr_data['text'][i]
            print(text)
            # Kiểm tra nếu từ trùng khớp với biểu thức chính quy ngày tháng
            if re.match(date_pattern, text,re.IGNORECASE):
                print(f"Ngày tháng phát hiện: {text}")
                (x, y, w, h) = (ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i])
                # Điều chỉnh tọa độ để phù hợp với ảnh gốc
                adjusted_x = x + roi[0]
                adjusted_y = y + roi[1]

                img = cv2.rectangle(img, (adjusted_x, adjusted_y), (adjusted_x + w, adjusted_y + h), (0, 255, 0), 2)
            
            # Kiểm tra nếu từ trùng khớp với từ "File"
            if re.match(word_pattern, text, re.IGNORECASE):  # Thêm re.IGNORECASE để tìm cả "file" và "File"
                print(f"Từ 'File' phát hiện: {text}")
                (x, y, w, h) = (ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i])
                # Điều chỉnh tọa độ để phù hợp với ảnh gốc
                adjusted_x = x + roi[0]
                adjusted_y = y + roi[1]

                img = cv2.rectangle(img, (adjusted_x, adjusted_y), (adjusted_x + w, adjusted_y + h), (255, 0, 0), 2)

    # Hiển thị ảnh với các hình chữ nhật xung quanh từ nhận diện
    cv2.imshow('img', img)
    cv2.waitKey(0)
def read_vietnamese_text(image_path):
    reader = easyocr.Reader(['vi'])  # Chỉ định ngôn ngữ là tiếng Việt
    results = reader.readtext(image_path)

    for (bbox, text, confidence) in results:
        print(f"Detected text: {text}, Confidence: {confidence}")
        # Hiển thị bounding box trên ảnh
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        image = cv2.imread(image_path)
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.imshow("Detected Text", image)
        cv2.waitKey(0)
def read_text_paddleocr(image_path):
    img = cv2.imread(image_path)
    # Khởi tạo PaddleOCR với chế độ nhẹ
    ocr = PaddleOCR(use_angle_cls=False, lang='vi', use_gpu=False)  # use_gpu=False cho chế độ nhẹ
    roi = (1580, 119, 337, 858)
    x, y, w, h = roi
    roi_image = img[y:y+h, x:x+w]
    result = ocr.ocr(roi_image)

    for line in result[0]:
        if line[1][1] > 0.85:
            print(f"Detected: {line[1][0]}, Confidence: {line[1][1]}")
# CaptureScreen()
# Biểu thức chính quy tìm ngày tháng
date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
# Biểu thức chính quy tìm kiếm từ "File"
word_pattern = 'File'
path = r"D:\python\learnpython\ReadComment\captures\live-tiktok.PNG"

# DetectData('TR','Plaza',path)
# read_vietnamese_text(path)
# read_text_paddleocr(path)
text = "Máy tính của tôi có thể xử lý tiếng Việt tốt!"
print(text)