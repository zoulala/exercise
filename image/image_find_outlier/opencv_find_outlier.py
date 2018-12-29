import time
import cv2
from matplotlib import pyplot as plt

start = time.time()
# 1、获得鸭子同等大小的王思聪 —— resize（OpenCV）
'''
这个部分主要是数据的预处理，说得很专业，
其实就是用电脑自带的截图工具，截取一个小鸭子，
他的大小大约为 36*36。我们就相应地把王思聪 resize 到和小鸭子同等大小，
这里采用了插值 inter_cubic 的方式来进行重采样。
'''
image_file = 'mr_w.jpg'
template = cv2.imread(image_file)

template = cv2.resize(template,(40,40), interpolation=cv2.INTER_CUBIC)
plt.imshow(template)
plt.show()

# 2、在原图全局搜索，匹配王思聪所在的位置 —— matchTemplate （opencv）
'''
OpenCV 作为一个比较全能的图像处理库，能够提供较为许多图像处理的基础，比如边缘监测函数可以直接用于监测图像的边界（OpenCV 也提供了 canny 算子、sobel 算子等）。

这里我们使用 模版匹配算法（matchTemplate），他帮助算法在一副图像中找到特定的目标。该函数需要四个参数，
原图 Image
监测目标 detect
匹配结果图 result
匹配衡量方式 method
CV_TM_SQDIFF，平方差
CV_TM_SQDIFF_NORMED，平方差归一化
CV_TM_CCORR，相关度
CV_TM_CCORR_NORMED，相关度归一化
CV_TM_CCOEFF，相关系数
CV_TM_CCOEFF_NORMED，相关系数归一化

因此，该搜索主要是以像素级别的匹配，不会进行缩放；

我们目前的任务中王思聪的色调并没有改变，因此任何一种方法的差异并不是很大。
'''


mul_image_file = 'multis.jpg'
img = cv2.imread(mul_image_file)

# Apply template matching
res = cv2.matchTemplate(img, template, eval('cv2.TM_CCOEFF'))

# get the size of template
w, h = template[:,:,0].shape[::-1]

# 3、在王思聪周围画个红框 —— minMaxLoc（OpenCV）；
'''
matchTemplate 函数得到的结果是一个灰度数值图，给出的是图像中每一个 detect 范围的匹配程度，灰度数值越大，则相似度越高。

为了画出这个最有可能出现思聪王的位置，我们使用 OpenCVv 的 minMaxLoc 函数来得到思聪王边框的具体位置，并进一步使用 OpenCV 的 rectangle 函数来画出这个框。
'''

# get anchor for templatematch result
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# draw rectangle
top_left = max_loc
bottom_right = (top_left[0]+w, top_left[1]+h)
imgplt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.rectangle(imgplt, top_left, bottom_right, 255, 2)

end = time.time()
print('耗时：',end-start)
# show image
plt.imshow(imgplt)
plt.title('detected results'), plt.xticks([]), plt.yticks([])
plt.show()


'''
PS，👆是为了展示一下 OpenCV 的风采。因此使用了传统的模式匹配流程。如果我们在实际应用中，面对雷同的问题。

首先分析认为，王思聪的脸部颜色和鸭子不一样，且他的脸部颜色只有他独有的；
可以使用 滴管 功能来得到 王思聪脸部颜色的 RGB；
在图中搜索有 脸部颜色 RGB 的部分 并 高亮；
找到 王思聪！
'''


