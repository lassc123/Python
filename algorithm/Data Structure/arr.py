import random
# 初始化数组
arr: list[int] = [0] * 5 # [0,0,0,0,0]
nums: list[int] = [1,3,2,4,5]

def random_access(nums:list[int])-> int:
    """随机访问元素"""
    # 在区间[0,len(nums)-1]中随机抽取一个数字
    random_index = random.randint(0,len(nums)-1)
    # 获取并返回随机元素
    random_num = nums[random_index]
    return random_num

def insert(nums:list[int],num: int,index: int):
    """在数组的索引 index 处插入元素num"""
    # 把索引 index 以及之后的所有元素向后移动一位
    for i in range(len(nums)-1,index,-1):
        nums[i]=nums[i-1]
    # 将 num 赋给 index 处的元素
    nums[index] = num

def remove(nums:list[int],index:int):
    """删除索引 index 处的元素"""
    # 把索引 index 之后的元素全部向前移一位
    for i in range(index,len(nums)-1):
        nums[i]=nums[i+1]
print(len(nums))
remove(nums,1)
print(nums)