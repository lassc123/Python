def  two_sum_brute_froce(nums:list[int],target:int)->list[int]:
    """方法一：暴力枚举"""
    # 双层循环，时间复杂度为O(n^2)
    for i  in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []

def two_sum_hash_table(nums:list[int],target:int)->list[int]:
    """方法二：辅助哈希表"""
    # 辅助哈希表，空间复杂度为O(n)
    dic = {}
    # 单层循环，时间复杂度为O(n)
    for i in range(len(nums)):
        if target-nums[i] in dic:
            return [dic[target-nums[i]],i]
        dic[nums[i]] = i
    return []