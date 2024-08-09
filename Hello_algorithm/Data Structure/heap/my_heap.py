class MaxHeap():
    """大顶堆"""

    def __init__(self,nums:list[int]):
        """构造方法,根据输入列表建堆"""
        # 将列表元素原封不动添加进堆
        self.max_heap = nums
        # 堆化除叶节点以外的其他所有节点
        for i in range(self.parent(self.size()-1),-1,-1):
            self.sift_down(i)

    def size(self):
        """获取堆的长度"""
        return len(self.max_heap)
    
    def is_empty(self)->bool:
        """判断堆是否为空"""
        return self.size() == 0
    
    def left(sel,i:int)->int:
        """获取左子节点的索引"""
        return 2*i+1
    
    def right(self,i:int)->int:
        """获取右子节点的索引"""
        return 2*i+2
    
    def parent(self,i:int)->int:
        """获取父节点的索引"""
        return (i-1)//2 # 向下整除
    
    def peek(self)->int:
        """访问堆顶元素"""
        return self.max_heap[0]
    
    def swap(self,i,p):
        """交换父子节点的值"""
        self.max_heap[i],self.max_heap[p] = self.max_heap[p],self.max_heap[i]

    
    def push(self,val:int):
        """元素入堆"""
        # 添加节点
        self.max_heap.append(val)
        # 从底至顶堆化
        self.sift_up(self.size()-1)

    
    def sift_up(self,i:int):
        """从节点i开始，从底至顶堆化"""
        while True:
            # 获取节点i的父节点
            p = self.parent(i)
            # 当“越过根节点”或“节点无须修复”时，结束堆化
            if p<0 or self.max_heap[i] <= self.max_heap[p]:
                break
            # 交换两节点
            self.swap(i,p)
            # 循环向上堆化
            i = p

    def pop(self)->int:
        """元素出堆"""
        # 判空处理
        if self.is_empty():
            raise IndexError("堆为空")
        # 交接根节点与最右叶节点（交换首元素和尾元素）
        self.swap(0,self.size()-1)
        # 删除节点
        val = self.max_heap.pop()
        # 从顶至底堆化
        self.sift_down(0)
        # 返回堆顶元素
        return val
    
    def sift_down(self,i:int):
        """从节点i开始，从顶至底堆化"""
        while True:
            """判断节点i,l,r中值最大的节点，记为ma"""
            l,r,ma = self.left(i),self.right(i),i
            if l<self.size() and self.max_heap[l]>self.max_heap[ma]:
                ma = l
            if r<self.size() and self.max_heap[r]>self.max_heap[ma]:
                ma = r
            # 若节点i最大或索引l,r越界，则无须继续堆化，跳出
            if ma == i:
                break
            # 交换两节点
            self.swap(ma,i)
            # 循环向下堆化
            i = ma

    