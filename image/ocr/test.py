
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def main():
    image = Image.open("w20.jpg")
    # image.show() #打开图片1.jpg
    text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
    # print(text)
    with open("output.txt", "w", encoding='utf8') as f:  # 将识别出来的文字存到本地
        print(text)
        f.write(str(text))

if __name__ == '__main__':
    main()