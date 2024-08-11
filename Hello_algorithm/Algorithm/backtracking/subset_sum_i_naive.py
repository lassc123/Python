def backtrace(state:list[int],target:int,choices:list[int],start:int,res:list[list[int]]):
    """回溯算法:子集和I"""
    # 子集和等于target时，记录解
    if target == 0:
        res.append(list(state))
        return
    # 遍历所有选择
    # 剪枝二：从start开始遍历，避免产生重复子集
    for i in range(start,len(choices)):
        # 剪枝：若子集和超过target，则跳过该选择
        # 这是因为数组已排序，后边元素更大，子集和一定超过target
        if target - choices[i] < 0:
            continue
        # 尝试：做出选择，更新元素和total
        state.append(choices[i])
        # 进行下一轮选择
        backtrace(state,target,target-choices[i],choices,i,res)
        # 回退：撤销选择，恢复到之前的状态
        state.pop()

def subset_sum_i_naive(nums:list[int],target:int)->list[list[int]]:
    """求解子集和I（包含重复子集）"""
    state = [] # 状态（子集）
    nums.sort() # 对nums进行排序
    start = 0 # 遍历起始点
    res = [] # 结果列表（子集列表）
    backtrace(state,target,nums,start,res)
    return res
