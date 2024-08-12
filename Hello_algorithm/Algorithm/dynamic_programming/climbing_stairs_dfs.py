def dfs(i:int)->int:
    """搜索"""
    # 已知 dp[1]和dp[2]，返回之
    if i==1 or i==2:
        return i
    # dp[i] = dp[i-1]+dp[i-2]
    count = dfs(i-1)+dfs(i-2)
    return count

def climbing_stairs_dfs(n:int)->int:
    """爬楼梯：搜索"""
    return dfs(n)