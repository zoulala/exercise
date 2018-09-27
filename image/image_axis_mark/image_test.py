# -*- coding: utf-8 -*-
# 找出图中图标位置数据

import cv2
import numpy

lena = cv2.imread('beijing (1).png')
img = lena


# grb转灰度图像，二值化处理
def gray_binarizing(img, threshold):
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    value = [0] * 3
    gray_img = numpy.zeros([height, width], numpy.uint8)

    for row in range(height):
        for column in range(width):
            for chan in range(channels):
                value[chan] = img[row, column, chan]
            R = value[2]
            G = value[1]
            B = value[0]
            # new_value = 0.2989 * R + 0.5870 * G + 0.1140 * B
            new_value = 0.2989 * R + 0.5870 * G + 0.1140 * B  # 转为灰度像素
            if new_value < threshold:
                gray_img[row, column] = 0
            else:
                gray_img[row, column] = 255
    return gray_img

# 找到行线位置
def find_row(img):
    height = img.shape[0]
    width = img.shape[1]
    row_index_list = []
    for i in range(height):
        line = img[i]
        if sum(line)/(255*width)<0.3:
            row_index_list.append(i)  # 行线位置
    row_index_list = sorted(row_index_list, reverse=True)
    return row_index_list

# 找到列线位置
def find_column(img):
    height = img.shape[0]
    width = img.shape[1]
    column_index_list = []
    for i in range(width):
        line = img[:,i]
        if sum(line)/(255*height)<0.3:
            column_index_list.append(i)  # 列线位置
    return column_index_list

# 找到特定图标位置
def find_axes(img):
    height = img.shape[0]
    width = img.shape[1]
    row_index_list = []
    for i in range(height):
        line = img[i]
        if sum(line)/(255*width)<0.3:
            row_index_list.append(i)  # 行线位置
    row_index_list = sorted(row_index_list,reverse=True)
    flags = {}
    for i in range(len(row_index_list)):
        j = row_index_list[i]
        flags[i+1] = []
        k_list = []
        for k in range(width):
            if img[j+4][k] == 0:
                k_list.append(k)
            else:
                if len(k_list)>4:
                    flags[i+1].append(sum(k_list)//len(k_list))
                k_list = []
    return flags

# 数组位置转换为原点坐标
def yx_xy_norm(axes_y_to_x):
    axes_xy = []
    for y in axes_y_to_x:
        for x in axes_y_to_x[y]:
            axes_xy.append((x, y))
    axes_sort = sorted(axes_xy, key=lambda x: x[0])

    x_axes = [x for x, y in axes_sort]
    x_set = sorted(set(x_axes))

    axes_tuple = [(x_set.index(x) + 1, y) for x, y in axes_sort]
    return axes_tuple


if __name__ == "__main__":
    gray_img = gray_binarizing(img, threshold=208)

    axes_y_to_x = find_axes(gray_img)

    axes_x_to_y = yx_xy_norm(axes_y_to_x)



    print(axes_x_to_y)
    print(len(axes_x_to_y))

    # print(find_column(gray_img))
    cv2.imshow('gray image', gray_img)
    cv2.waitKey(0)
    # cv2.imwrite('gray_lena.jpg', gray_img)