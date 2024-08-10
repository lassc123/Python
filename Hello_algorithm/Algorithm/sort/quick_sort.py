def median_three(nums:list[int],left:int,mid:int,right:int)->int:
    """选取三个候选元素的中位数"""
    l,m,r  = nums[left],nums[mid],nums[right]
    if (l<=m<=r) or (r<=m<=l):
        return mid # m在l和r之间
    if (m<=l<=r) or (r<=l<=m):
        return left # l在m和r之间
    return right

def partition(nums:list[int],left:int,right:int)->int:
    """哨兵划分(三数取中值)"""
    # 以nums[left]为基准数
    med = median_three(nums,left,(left+right)//2,right)
    # 将中位数交换至数组最左端
    nums[left],nums[med] = nums[med],nums[left]
    # 以nums[left]为基准数
    i,j = left,right
    while i<j:
        while i<j and nums[j]>=nums[left]:
            j -= 1 # 从右向左找首个小于基准数的元素
        while i<j and nums[i]<=nums[left]:
            i += 1 # 从左向右找首个大于基准数的元素
        # 元素交换
        nums[i],nums[j] = nums[j],nums[i]
        # 将基准数交换至双子数组的分界线
        nums[i],nums[left] = nums[left],nums[i]
        return i # 返回基准数的索引

def quick_sort(nums:list[int],left:int,right:int):
    """快速排序(尾递归优化)"""
    # 子数组长度为1时终止递归
    if left>=right:
        return
    # 哨兵划分
    pivot = partition(nums,left,right)
    # 对两个子数组中较短的那个执行快速排序
    if pivot-left < right -pivot:
        quick_sort(nums,left,pivot-1) # 递归排序左子数组
        left = pivot + 1 # 剩余未排序区间为[pivot+1,right]
    else:
        quick_sort(nums,pivot+1,right) # 递归排序右数组
        right = pivot - 1 # 剩余未排序区间为 [left, pivot - 1]
