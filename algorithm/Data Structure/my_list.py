class MyList:
    """列表类"""
    
    def __init__(self):
        """构造方法"""
        self._capacity:int = 10 # 列表容量
        self._arr:list[int] = [0]*self._capacity # 数组（存储列表元素）
        self._size:int = 0 # 列表长度（当前元素数量）
        self._extend_ratio:int = 2 # 每次列表扩容的倍数

    def size(self)-> int:
        """获取列表的长度（当前元素数量）"""
        return self._size
    
    def capacity(self)-> int:
        """获取列表容量"""
        return self._capacity
    
    def get(self,index:int)-> int:
        """访问元素"""
        # 索引如果越界，则抛出异常，下同
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]
    
    def set(self,num:int,index:int):
        """更新元素"""
        if index < 0 or index >=self._size:
            raise IndexError
        self._arr[index] = num

    def add(self,num:int):
        """在尾部添加元素"""
        # 元素数量超出容量时，触发扩容机制
        if self._size == self._capacity:
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self,num:int ,index:int):
        """在中间插入元素"""
        if self._size == self._capacity:
            self.extend_capacity()
        # 将索引index 以及之后的元素都向后移动一位
        