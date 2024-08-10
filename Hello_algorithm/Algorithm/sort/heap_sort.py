def sift_down(nums:list[int],n:int,i:int):
    """堆的长度为n,从节点i开始，从顶至底堆化"""
    while True:
        # 判断节点i,l,r中值最大的节点，记为ma
        l = 2*i+1
        r = 2*i+2
        ma = i
        if l<n and nums[l]>nums[ma]:
            ma = l
        elif r<n and nums[r]>nums[ma]:
            ma = r
        # 若节点i最大或索引l,r越界，则无须继续堆化，跳出
        if ma == i:
            break
        # 交换两节点
        nums[i],nums[ma] = nums[ma],nums[i]
        # 循环向下堆化
        i = ma

def heap_sort(nums:list[int]):
    """堆排序"""
    # 建堆操作：堆化除叶节点以外的其他所有节点
    for i in range(len(nums)//2-1,-1,-1):
        sift_down(nums,len(nums),i)
    # 从堆中提取最大元素，循环n-1轮
    for i in range(len(nums)-1,0,-1):
        # 交换根节点与最右叶节点（交换首元素和尾元素）
        nums[0],nums[i] = nums[i],nums[0]
        # 以根节点为起点，从顶至底堆化
        sift_down(nums,i,0)