class Item:
    """物品"""

    def __init__(self,w:int,v:int):
        self.w = w # 物品重量
        self.v = v # 物品价值

def fractional_knapsack(wgt:list[int],val:list[int],cap:int)->int:
    """分数背包：贪心"""
    # 创建物品列表，包含两个属性：重量，价值
    items = [Item(w,v) for w,v in zip(wgt,val)]
    # 按照单位价值item.v/item.w从高到低进行排序
    items.sort(key=lambda item:item.v/item.w,reverse=True)
    # 循环贪心选择
    res = 0
    for item in items:
        if item.w<=cap:
            # 若剩余容量充足，则将当前物品整个装进背包
            res += item.v
            cap -= item.w
        else:
            # 若剩余容量不足，则将当前物品的一部分装进背包
            res += (item.v/item.w)*cap
            # 若已无剩余容量，因此跳出循环
            break
    return res