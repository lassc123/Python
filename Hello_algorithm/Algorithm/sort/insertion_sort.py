def insertion_sort(nums:list[int]):
    """插入排序"""
    # 外排序：已排序区间为[0,i-1]
    for i in range(1,len(nums)):
        base = nums[i]
        j = i-1
        # 内循环：将base插入到已排序区间[0,i-1]中的正确位置
        while j>=0 and nums[j]>base:
            nums[j+1] =nums[j] # 将nums[j]向右移动一位
            j -= 1
        nums[j+1] = base  # 将base赋值到正确位置