class ArrayDeque:
    """基于环形数组实现的双向队列"""

    def __init__(self,capacity:int):
        """构造方法"""
        self._nums:list[int] = [0]*capacity
        self._front:int = 0
        self._size:int = 0

    def capacity(self)->int:
        """获取双向队列的容量"""
        return len(self._nums)
    
    def size(self)->int:
        """获取双向队列的长度"""
        return self._size
    
    def is_empty(self)->bool:
        """判断双向队列是否为空"""
        return  self._size == 0
    
    def index(self,i:int)->int:
        """计算环形数组索引"""
        # 通过取余操作实现数组首尾相连
        # 当i越过数组尾部后，回到头部
        # 当i越过数组头部后，回到尾部
        return (i+self.capacity())%self.capacity()
    
    def push_first(self,num:int):
        """队首入队"""
        if self._size == self.capacity():
            raise IndentationError("双向队列已满")
        # 队首指针向左移动一位
        # 通过取余操作实现front越过数组头部后回到尾部
        self._front = self.index(self._front-1)
        # 将num添加至队首
        self._nums[self._front] = num
        self._size += 1

    def push_last(self,num:int):
        """队尾入队"""
        if self._size == self.capacity():
            raise IndentationError("双向队列已满")
        # 计算队尾指针，指向队尾索引+1
        rear = self.index(self._front+self._size)
        # 将num添加至队尾
        self._nums[rear] = num
        self._size += 1

    def pop_first(self)->int:
        """队首出队"""
        num = self.peek_first()
        # 队首指针向后移动一位
        self._front = self.index(self._front+1)
        self._size -= 1
        return num
    
    def pop_last(self)->int:
        """队尾出队"""
        num = self.peek_last()
        self._size -=1
        return num
    
    def peek_first(self)->int:
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        return self._nums[self._front]
    
    def peek_last(self)->int:
        """访问队尾元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        
    def to_array(self)->list[int]:
        """返回数组用于打印"""
        # 仅转换有效长度范围内的列表元素
        res = []
        for i in range(self._size):
            res.append(self._nums[self.index(self._front+i)])
        return res