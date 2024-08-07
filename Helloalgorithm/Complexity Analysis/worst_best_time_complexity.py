import random
def random_numbers(n: int)-> int:
    """生成一个数组,元素为:1,2,...,n,顺序被打乱"""
    # 生成数据 nums =：1，2，3，。。。，n
    nums = [i for i in range(1,n+1)]
    # 随机打乱数组元素
    random.shuffle(nums)
    return nums

def find_one(nums:list[int])-> int:
    """查找数组 nums 中数字 1 所在索引"""
    for i in range(len(nums)):
        # 当元素 1 在数组头部时，达到最佳时间复杂度O(1)
        # 当元素 1 在数组尾部时，达到最差时间复杂度O(n)
        if nums[i] ==1:
            return i
    return -1