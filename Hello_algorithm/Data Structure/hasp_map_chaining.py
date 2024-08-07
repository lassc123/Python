class HashMapChaining:
    """链式地址哈希表"""

    def __init__(self):
        """构造方法"""
        self.size = 0 # 键值对数量
        self.capacity = 4 # 哈希表容量
        self.load_thres = 2.0/3.0 # 触发扩容的负载因子阈值
        self.extend_ratio = 2 # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)] # 桶数组