class ArrayQueue:
    """基于环形数组实现的队列"""

    def __init__(self,size:int):
        """构造方法"""
        self._nums:list[int] = [0]*size # 用于存储队列元素的数组
        self._front:int = 0 # 队首指针，指向队首元素
        self._size:int = 0 # 队列长度

        def capacity(self)->int:
            """获取队列的容量"""
            return len(self._nums)
        
        def size(self)->int:
            """获取队列的长度"""
            return self._size
        
        def is_empty(self)->bool:
            """判断队列是否为空"""
            return self._size == 0
        
        def push(self,num:int):
            """入队"""
            if self._size == self.capacity():
                raise IndexError("队列已满")
            # 计算队尾指针，指向队尾索引+1
            # t通过取余操作实现rear越过数组尾部后回到头部
            rear:int = (self._front+self._size)% self.capacity()
            # 将num添加至队尾
            self._nums[rear] = num
            self._size += 1

        def pop(self)->int:
            """出队"""
            num:int = self.peek()
            # 队首指针向后移动一位，若超过尾部则返回数组头部
            self._front = (self._front+1)%self.capacity()
            self._size -= 1
            return num
        
        def peek(self)->int:
            """访问队首元素"""
            if self.is_empty():
                raise IndexError("队列为空,无法执行出队操作")
            return self._nums[self._front]
        
        def to_list(self)->list[int]:
            """返回列表用于打印"""
            res = [0]*self.size()
            j:int = self._front
            for i in range(self.size()):
                res[i] = self._nums[(j%self.capacity())]
                j += 1
            return res