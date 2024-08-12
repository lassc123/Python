def min_cost_climbing_stairs_dp(cost:list[int])->int:
    """爬楼梯最小代价：空间优化后的动态规划"""
    n = len(cost) - 1
    if n == 1 or n == 2:
        return cost[n]
    a,b= cost[1],cost[2]
    # 状态转移：从较小子问题逐步求解较大子问题
    for i in range(3,n+1):
        a,b= b,min(a,b)+cost[i]
    return b