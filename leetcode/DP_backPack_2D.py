""""
列表arr = [1,2,6,3,7,2,1,8]都为正整数， S=9
寻找子元素集合，组成和最接近S且不大于S,返回和
"""
import numpy as np

def backPack(m, A):
    # write your code here
    #dp = [[0 for j in range(m + 1)] for i in range(0, len(A))]
    dp = np.zeros((len(A), m + 1),dtype=int)

    dp[:, 0] = 0
    dp[0, :] = A[0]
    dp[0, :A[0]] = 0

    for i in range(1, len(A)):
        for j in range(1, m + 1):
            if A[i] > j:
                dp[i, j] = dp[i - 1, j]
            else:
                sub1 = dp[i - 1, j]
                sub2 = dp[i - 1, j - A[i]] +A[i]
                dp[i, j] = max(sub1, sub2)
    return dp[-1, -1]


A = [2, 3, 5, 7]
m = 12
print(backPack(m,A))