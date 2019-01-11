""""
列表arr = [1,2,6,3,7,2,0,8]
选择不相邻的元素，组成和最大,返回和
"""
import numpy as np
"""
逻辑：
    opt(i)=max(选：opt(i-2)+arr[i], 不选:opt(i-1))
出口：
    opt(0) = arr[0]
    opt(1) = max(arr[0], arr[1])
"""

# 递归方法
def rec_opt(arr, i):
    if i ==0:
        return arr[0]
    elif i ==1:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr, i-2)+arr[i]
        B = rec_opt(arr, i-1)
        return max(A,B)



# 动态规划
def dp_opt(arr):
    ls = len(arr)
    if ls ==0:
        return 0
    if ls ==1:
        return arr[0]
    if ls ==2:
        return max(arr[0],arr[1])

    opt = np.zeros(ls)
    opt[0] = arr[0]
    opt[1] = max(arr[0],arr[1])
    for i in range(2, ls):
        A = opt[i-2]+arr[i]
        B = opt[i-1]
        opt[i] = max(A,B)
    return opt[ls-1]


arr = [1,2,6,3,7,2,0,8]
print(rec_opt(arr,len(arr)-1))
print(dp_opt(arr))
