def backtrace(state:list[int],choices:list[int],selected:list[bool],res:list[list[int]]):
    """回溯算法：全排列I"""
    # 当状态长等于元素数量时，记录解
    if len(state) == len(choices):
        res.append(list(state))
        return
    # 遍历所有选择
    for i,choice in enumerate(choices):
        # 剪枝：不允许重复选择元素
        if not selected[i]:
            # 尝试：做出选择，更新状态
            selected[i] = True
            state.append(choice)
            # 进行下一轮选择
            backtrace(state,choices,selected,res)
            # 回退：撤销选择，恢复到之前的状态
            selected[i] = False
            state.pop()

def permutations_i(nums:list[int])->list[list[int]]:
    """全排列 I"""
    res = []
    backtrace(state=[],choices=nums,selected=[False]*len(nums),res=res)
    return res


