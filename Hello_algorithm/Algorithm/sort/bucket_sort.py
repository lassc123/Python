def bucket_sort(nums:list[float]):
    """桶排序"""
    # 初始化k=n/2个桶，预期向每个桶里分配两个元素
    k = len(nums)//2
    buckets = [[] for _ in range(k)]
    # 1.将数组元素分配到各个桶中
    for num in nums:
        # 输入范围为[0,1),使用num*k映射到索引范围[0,k-1]
        i = int(num*k)
        # 将num添加进桶i
        buckets[i].append(num)
    # 2.堆各个桶执行排序
    for bucket in buckets:
        # 使用内置排序函数，也可以替换成其他排序算法
        bucket.sort()
    # 3.遍历桶合并结果
    i = 0
    for bucket in buckets:
        for num in bucket:
            nums[i] = num
            i += 1