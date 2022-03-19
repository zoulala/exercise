#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     Sort_quick.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-12-29
# brief:    
#
# cmd>e.g:  
# *****************************************************

"""快速排序：
说白了就是给基准数据找其正确索引位置的过程，本质就是把基准数大的都放在基准数的右边,把比基准数小的放在基准数的左边,这样就找到了该数据在数组中的正确位置.
然后递归实现左边数组和右边数组的快排。
"""

def quick_sort(nums, st, et):
    if st>=et:
        return

    i,j = st, et

    # 设置基准数
    base = nums[i]
    # 如果列表后边的数比基准数大或相等,则前移一位直到有比基准数小的数
    while (i < j) and (nums[j] >= base):
        j = j - 1

    # 如找到,则把第j个元素赋值给第i个元素
    nums[i] = nums[j]

    # 同样的方式比较前半区
    while (i < j) and (nums[i] <= base):
        i = i + 1
    nums[j] = nums[i]

    # 做完第一轮比较之后,列表被分成了两个半区,并且i=j，此时找到基准值
    nums[i] = base

    # 递归前后半区
    # print(base, myList)
    quick_sort(nums, st, i - 1)
    quick_sort(nums, j + 1, et)


nums = [1,3,2,6,4,7,5]
quick_sort(nums,0,6)
print(nums)

