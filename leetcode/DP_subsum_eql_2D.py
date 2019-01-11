""""
列表arr = [1,2,6,3,7,2,1,8]都为正整数， S=9
是否存在子元素集合，组成和刚好=S,存在返回True，否则返回False
"""
import numpy as np
"""
逻辑：
    Subset(arr,i , S)
    
    选 :return： Subset(arr, i-1, S-arr[i])
    不选 :return： Subset(arr, i-1, S)
    
出口：
    if S == 0:
        return True
    if i == 0:
        return arr[0]==S
    if arr[i]>S:
        return Subset(arr, i-1, S)
"""

# 递归方法
def rec_subset(arr, i, S):
    if S == 0:
        return True
    elif i == 0:
        return arr[0]==S
    elif arr[i]>S:
        return rec_subset(arr, i-1, S)
    else:
        A = rec_subset(arr, i-1, S-arr[i])
        B = rec_subset(arr, i-1, S)
        return A or B


# 动态规划
def dp_subset(arr, S):
    # 多了一个变量S，所以dp为2维数组
    subset = np.zeros((len(arr), S+1), dtype=bool)  # 创建二维数组，保存True or False
    subset[:,0] = True
    subset[0,:] = False
    subset[0,arr[0]] = True

    for i in range(1,len(arr)):
        for s in range(1, S+1):
            if arr[i]>s:
                subset[i,s] = subset[i-1,s]
            else:
                A = subset[i - 1, s - arr[i]]
                B = subset[i - 1, s]
                subset[i,s] = A or B
    r,c = subset.shape
    return subset[r-1,c-1]

arr = [1,2,6,3,7,2,1,8]
S = 12
print(rec_subset(arr, len(arr)-1, S))
print(dp_subset(arr, S))






