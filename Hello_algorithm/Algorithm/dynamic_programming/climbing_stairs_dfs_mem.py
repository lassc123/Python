def dfs(i:int,mem:list[int])->int:
    """记忆化搜索"""
    # 已知dp[1]和dp[2]，返回之
    if i == 1 or i == 2:
        return i
    # 若存在记录dp[i],则直接返回之
    if mem[i] != -1:
        return mem[i]
    # dp[i] = dp[i-1]+dp[i-2]
    count = dfs(i-1,mem)+dfs(i-2,mem)
    # 记录dp[i]
    mem[i] = count
    return count

def climbing_stairs_dfs_mem(n:int)->int:
    """爬楼梯：记忆化搜索"""
    # mem[i]记录爬到第i阶的方案总数，-1代表无记录
    mem = [-1]*(n+1)
    return dfs(n,mem)