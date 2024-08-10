def bubble_sort(nums:list[int]):
    """冒泡区间"""
    n = len(nums)
    # 外循环：未排序区间未[0,i]
    for i in range(n-1,0,-1):
        flag = False
        # 内循环：将未排序区间[0,i]中的最大元素交换至该区间的最右端
        for j in range(i):
            if nums[j]>nums[j+1]:
                # 交换nums[j]与nums[j+1]
                nums[j],nums[j+1] = nums[j+1],nums[j]
                flag = True # 记录交换元素
        if not flag:
            break # 此轮“冒泡”未交换任何元素，直接跳出