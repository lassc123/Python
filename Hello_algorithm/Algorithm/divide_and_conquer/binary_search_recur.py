def dfs(nums:list[int],target:int,i:int,j:int)->int:
    """二分查找：问题f（i,j）"""
    # 若区间为空，代表无目标元素，则返回-1
    if i>j:
        return -1
    # 计算中点索引m
    m = (i+j)//2
    if nums[m] < target:
        # 递归子问题f（m+1，j）
        return dfs(nums,target,m+1,j)
    elif nums[m] > target:
        # 递归子问题f（i，m-1）
        return dfs(nums,target,i,m-1)
    else:
        # 找到目标元素，返回其索引
        return m

def binary_search(nums:list[int],target:int)->int:
    """二分查找"""
    n = len(nums)
    # 求解问题f(0,n-1)
    return dfs(nums,target,0,n-1)