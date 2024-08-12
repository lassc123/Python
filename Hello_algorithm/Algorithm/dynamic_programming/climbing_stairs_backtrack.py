def backtrack(choices:list[int],state:int,n:int,res:list[int])->int:
    """回溯"""
    # 当爬到第n阶时，方案数量加一
    if state == n:
        res[0] += 1
    # 遍历所有选择
    for choice in choices:
        # 剪枝：不允许越过第n阶
        if state + choice > n:
            continue
        # 尝试：做出选择，更新状态
        backtrack(choices,state+choice,n,res)
        # 回退

def climbing_stairs_backtrack(n:int)->int:
    """爬楼梯：回溯"""
    choices = [1,2] # 可选择向上爬1阶或2阶
    state = 0 # 从第0阶开始爬
    res = [0] # 使用res[0]记录方案数量
    return res[0]