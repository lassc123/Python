def merge(nums:list[int],left:int,mid:int,right:int):
    """合并左子树组和右子树组"""
    # 左子树组区间为[left,mid],有子数组区间为[mid+1,right]
    # 创建一个临时数组tmp，用于存放合并后的结果
    tmp = [0]*(right-left+1)
    # 初始化左子数组和右子数组的起始索引
    i,j,k = left,mid+1,0
    # 当左右子数组都还有元素时，进行比较并将较小的元素复制到临时数组中
    while i<=mid and j<=right:
        if nums[i]<=nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[i]
            j += 1
        k += 1
    # 将左子树组和右子树组的剩余元素复制到临时数组中
    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1
    while j<=right:
        tmp[k] = nums[j]
        j += 1
        k += 1
    # 将临时数组tmp中的元素复制回原数组nums的对应区间
    for k in range(0,len(tmp)):
        nums[left+k] = tmp[k]
    
def merge_sort(nums:list[int],left:int,right:int):
    """归并排序"""
    # 终止条件
    if left >= right:
        return # 当子数组长度为1时终止递归
    # 划分阶段
    mid = (left+right)//2 # 计算中点
    merge_sort(nums,left,mid) # 递归左子数组
    merge_sort(nums,mid+1,right)# 递归右子数组
    # 合并阶段
    merge(nums,left,mid,right)