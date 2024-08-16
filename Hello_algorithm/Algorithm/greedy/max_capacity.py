def max_capacity(ht:list[int])->int:
    """最大容量：贪心"""
    # 初始化i,j,使其分列数组两端
    i,j =0,len(ht)-1
    # 初始最大容量为0
    res = 0
    # 循环贪心选择，直至两板相遇
    while i<j:
        # 更新最大容量
        cap = min(ht[i],ht[j])*(j-i)
        res = max(res,cap)
        # 向内移到短板
        if ht[i]<ht[j]:
            i+=1
        else:
            j-=1
    return res