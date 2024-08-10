def binary_search(nums:list[int],target:int)->int:
    """二分查找（双闭区间）"""
    # 初始化双闭区间[0,n-1]，即i,j分别指向数组首元素，尾元素
    i,j = 0,len(nums)-1
    # 循环，当搜索区间为空时跳出（当i>j时为空）
    while i <= j:
        # 理论上，Python的数字可以无限大（取决于内存大小），无须考虑大数越界问题
        m = (i+j)//2 # 计算中点索引m
        if nums[m]<target:
            i = m+1 # 此情况说明target在区间[m+1,j]中
        elif nums[m]>target:
            j = m-1 # 此情况说明target在区间[i,m-1]中
        else:
            return m # 找到目标元素，返回其索引
    return -1 # 未找到目标元素，返回-1

def binary_search_lcro(nums:list[int],target:int)->int:
    """二分查找（左闭右开区间）"""
    # 初始化左闭右开区间[0,n)，即i,j分别指向数组首元素，尾元素+1
    i,j = 0,len(nums)
    # 循环，当搜索区间为空时跳出（当i=j时为空）
    while i < j:
        m = (i+j)//2 # 计算中点索引m
        if nums[m]<target:
            i = m+1 # 此情况说明target在区间[m+1,j)中
        elif nums[m]>target:
            j = m  # 此情况说明target在区间[i,m)中
        else:
            return # 找到目标元素，返回其索引
    return -1 # 未找到目标元素，返回-1

def binary_search_insertion_simple(nums:list[int],target:int)->int:
    """二分查找插入点（无重复元素）"""
    i,j = 0 ,len(nums)-1 # 初始化双闭区间[0,n-1]
    while i<=j:
        m = (i+j)//2 # 计算中点索引m
        if nums[m]<target:
            i = m+1 # target在区间[m+1,j]中
        elif nums[m]>target:
            j = m-1 # target在区间[i,m-1]中
        else:
            return m # 找到target.返回插入点m
    # 未找到target，返回插入点 i
    return i 

def binary_search_insertion(nums:list[int],target:int)->int:
    """二分查找插入点（存在重复元素）"""
    i,j = 0,len(nums)-1
    while i <= j:
        m = (i+j)//2 # 计算中点索引m
        if nums[m]<target:
            i = m+1 # target在区间[m+1,j]中
        elif nums[m]>target:
            j = m-1 # target在区间[i,m-1]中
        else:
            j =m-1 # 首个小于target的元素在区间[i,m-1]中
        # 返回插入点i
        return i 
    
def binary_search_left_edge(nums:list[int],target:int)->int:
    """二分查找最左一个target"""
    # 等价于查找target的插入点
    i = binary_search_insertion(nums,target)
    # 未找到target，返回-1
    if i >= len(nums) or nums[i] != target:
        return -1
    # 找到target，返回索引i
    return i
def binary_search_right_edge(nums:list[int],target:int)->int:
    """二分查找最右一个target"""
    # 转换为查找最左一个target+1
    i = binary_search_insertion(nums,target+1)
    # j指向最右一个target，i指向首个大于target的元素
    j = i-1
    # 未找到target，返回-1
    if j == -1  or nums[j] != target:
        return -1
    # 找到target，返回索引j
    return j 