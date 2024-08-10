def digit(num:int,exp:int)->int:
    """获取元素num的第k位，其中exp=10^(k-1)"""
    #传入exp而非k可以避免在此重复执行昂贵的次方计算
    return (num//exp)%10

def counting_sort_digit(nums:list[int],exp:int):
    """计数排序（根据nums第k位排序）"""
    # 十进制的位范围为0~9，因此需要长度为10的桶数组
    counter = [0]*10
    n = len(nums)
    # 统计0~9各数字的出现次数
    for i in range(n):
        d = digit(nums[i],exp) # 获取nums[i]第k位，记为d
        counter[d] += 1
    # 求前缀和，将“出现个数”转换为“数组索引”
    for i in range(1,10):
        counter[i] += counter[i-1]
    # 倒序遍历，根据桶内统计结果，将各元素填入res
    res = [0]*n
    for i in range(n-1,-1,-1):
        d =digit(nums[i],exp)
        j = counter[d]-1 # 获取d在数组中的索引j
        res[j] = nums[i] # 将当前元素填入索引j
        counter[d] -= 1 # 将d的数量减1
    # 使用结果覆盖原数组nums
    for i in range(n):
        nums[i] = res[i]

def radix_sort(nums:list[int]):
    """基数排序"""
    # 获取数组的最大元素，用于判断最大位数
    m = max(nums)
    # 按照从低位到高位的顺序遍历
    exp = 1
    while exp<=m:
        # 对数组元素的第k位执行计数排序
        # k = 1->exp = 1
        # k = 2->exp = 10
        # 即exp = 10^(k-1)
        counting_sort_digit(nums,exp)
        exp *= 10