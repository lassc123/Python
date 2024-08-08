class ArrayBinaryTree:
    """数组表示下的二叉树类"""

    def __init__(self,arr:list[int|None]):
        """构造方法"""
        self._tree = list(arr)

    def size(self):
        """列表容量"""
        return len(self._tree)
    
    def val(self,i:int)->int|None:
        """获取索引为i节点的值"""
        # 若索引越界，则返回None，代表空位
        if i<0 or i>=self.size():
            return None
        return self._tree[i]
    
    def left(self,i:int)->int|None:
        """获取索引为i节点的左子节点的索引"""
        return 2*i+1
    
    def right(self,i:int)->int|None:
        """获取索引为i节点的右子节点的索引"""
        return 2*i+2
    
    def parent(self,i:int)->int|None:
        """获取索引为i节点的父节点的索引"""
        return (i-1)//2
    
    def level_order(self)->list[int]:
        """层序遍历"""
        self.res = []
        # 直接遍历数组
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res
    
    def dfs(self,i:int,order:str):
        """深度优先遍历"""
        if self.val(i) is None:
            return
        # 前序遍历
        if order == "pre":
            set.res.append(set.val(i))
        self.dfs(self.left(i),order)
        # 中序遍历
        if order == "in":
            self.res.append(self.val(i))
        self.res.append(self.right(i),order)
        # 后序遍历
        if order == "post":
            self.res.append(self.val(i))

    def pre_order(self)->list[int]:
        """前序遍历"""
        self.res = []
        self.dfs(0,order="pre")
        return self.res

    def in_order(self)->list[int]:
        """中序遍历"""
        self.res = []
        self.dfs(0,order="in")
        return self.res

    def post_order(self)->list[int]:
        """后序遍历"""
        self.res = []
        self.dfs(0,order="post")
        return self.res