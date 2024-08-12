def climbing_stairs_dp(n:int)->int:
    """爬楼梯：动态规划"""
    if n == 1 or n == 2:
        return n
    # 初始化dp表，用于存储子问题的解
    dp = [0]*(n+1)
    # 初始状态：预设最小子问题的的解
    dp[1],dp[2] = 1,2
    # 状态转移：从较小子问题逐步求解较大子问题
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]