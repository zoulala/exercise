
import sys

import time
time1 = time.time()
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


###########二值化算法
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


###########去除干扰线算法
def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img


########身份证号码识别
def identity_OCR(pic_path):
    #####身份证号码截图
    img1=Image.open(pic_path)
    w,h=img1.size
    ##将身份证放大3倍
    out=img1.resize((w*3,h*3),Image.ANTIALIAS)
    region = (125*3,200*3,370*3,250*3)
    #裁切身份证号码图片
    cropImg = out.crop(region)
    # 转化为灰度图
    img= cropImg.convert('L')
    # 把图片变成二值图像。
    img1=binarizing(img,100)
    img2=depoint(img)
    code = pytesseract.image_to_string(img2)
    print ("识别该身份证号码是:"+str(code))



if __name__ == '__main__':
    import cv2
    # id_img = Image.open("id.jpg")
    id_img = cv2.imread("id.jpg")
    gray = cv2.cvtColor(id_img, cv2.COLOR_BGR2GRAY)
    code = pytesseract.image_to_string(gray)
    pic_path="w4.jpg"
    identity_OCR(pic_path)
    time2 = time.time()
    print (u'总共耗时：' + str(time2 - time1) + 's')

