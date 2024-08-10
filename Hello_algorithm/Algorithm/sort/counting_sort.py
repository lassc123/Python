def counting_sort_naive(nums:list[int]):
    """计数排序"""
    # 简单实现，无法用于排序对象
    # 1.统计数组最大元素m
    m = 0
    for num in nums:
        m = max(m,num)
    # 2.统计各数字的出现次数
    # counter[num]代表num的出现次数
    counter = [0]*(m+1)
    for num in nums:
        counter[num] += 1
    # 3.遍历counter，将各元素填入原数组nums
    i = 0
    for num in range(m+1):
        for _ in range(counter[num]):
            nums[i] = num
            i += 1
    
def counting_sort(nums:list[int]):
    """计数排序"""
    # 完整实现，可排序对象，并且是稳定排序
    # 1.统计数组的最大元素m
    m = max(nums)
    # 2.统计各数字的出现次数
    # counter[num]代表num的出现次数
    counter = [0]*(m+1)
    for num in nums:
        counter[num] += 1
    # 3.求counter的前缀和，将“出现次数”转换为“尾索引”
    # 即counter[num]-1是num在res中最后一次出现的索引
    for i in range(m):
        counter[i+1] +=counter[i]
    # 4.倒序遍历nums，将各元素填入结果数组res
    # 初始化数组res用于记录结果
    n = len(nums)
    res = [0]*n
    for i in range(n-1,-1,-1):
        num = nums[i]
        res[counter[num]-1] = num # 将num放置到对应索引处
        counter[num] -= 1 # 令前缀和自减1，得到下次放置num的索引
    # 使用结果数组res覆盖原数组nums
    for i in range(n):
        nums[i] = res[i]