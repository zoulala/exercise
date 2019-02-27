""""
列表arr = [[1,3,1],
           [1,5,1],
           [4,2,1]] 都为整数
从左上角 走到右下角，路径和最短。只能走下、右
"""

"""
逻辑：
    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

出口：
    i=0
    j=0
"""


def minPathSum( grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    dp = grid[:]

    cs, rs = 0, 0
    for i in range(n):  # 获取第一行的dp值
        cs += grid[0][i]
        dp[0][i] = cs
    for i in range(m):  # 获取第一列的dp值
        rs += grid[i][0]
        dp[i][0] = rs

    for i in range(1, m):  # 获取剩下的dp值，并返回最后一个dp值即为所求
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]


